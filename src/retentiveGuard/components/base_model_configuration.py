import os 
from pandas import read_csv ,concat
import json
from tensorflow.keras.layers import TextVectorization
import tensorflow as tf
from src.retentiveGuard import logger


from tensorflow.keras import Model, Sequential
from tensorflow.keras.layers import Input, Embedding, Dense, Flatten, Softmax, Dropout
from itertools import repeat


from src.retentiveGuard.entity.config_entity import BaseModelConfig
from models.model_architecture import *


class BaseModel:
    def __init__(self,config:BaseModelConfig) -> None:
        self.config = config

    
    def load_dataset(self):
        tokenizer_path = self.config.tokenizer_path

        with open(tokenizer_path, 'r') as config_file:
            tokenizer_config = json.load(config_file)
        

        loaded_tokenizer = TextVectorization.from_config(tokenizer_config)

        return loaded_tokenizer
    
    def base_model_builder(self,tokenizer):

        # Initializing the strategy
        strategy = tf.distribute.MirroredStrategy()

        
        with strategy.scope():
            inputs = Input((512, ))
            x = Embedding(len(tokenizer.get_vocabulary()), 32)(inputs)
            x = Sequential([*repeat(RetentionEncoder(32, 32//2), 1)])(x)#RNN(RecurrentRetention(32, 32))(x)
            z = Dropout(0.5)(x)
            x = Flatten()(x)
            x = Dense(1, activation='sigmoid')(x)
            model = Model(inputs=inputs, outputs=x)

            model.compile(
                    optimizer=tf.keras.optimizers.Adam(learning_rate=5e-4, weight_decay=0.1, clipvalue=3),
                    loss=tf.keras.losses.BinaryFocalCrossentropy(apply_class_balancing=True, label_smoothing=0.1),
                    metrics=[tf.keras.metrics.BinaryAccuracy(),
                            tf.keras.metrics.AUC(),
                            tf.keras.metrics.Recall(),
                            tf.keras.metrics.Precision()],
                )
        
        return model
    
    def save_base_model(self,model):

        model_save_path = self.config.base_model_path
        
        # Save the model
        tf.keras.models.save_model(model, model_save_path)
        
        # Log the action
        logger.info(f"Base model saved at: {model_save_path}")
            
        





    
    



    
