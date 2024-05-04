import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
from pandas import read_csv
import json
from src.retentiveGuard.entity.config_entity import ModelTrainerConfig
from src.retentiveGuard import logger
import matplotlib.pyplot as plt
import pickle
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def train_model(self):
        strategy = tf.distribute.MirroredStrategy()

        # loading the stuffs
        train_dataset = read_csv(self.config.train_data_path)
        model = tf.keras.models.load_model(self.config.base_model_path)

        tokenizer_path = self.config.tokenizer_path
        with open(tokenizer_path, 'r') as config_file:
            tokenizer_config = json.load(config_file)

        tokenizer = TextVectorization.from_config(tokenizer_config)
        config_file.close()


        try:
            histories = []
            with strategy.scope():
                ds = tf.data.Dataset.from_tensor_slices((train_dataset.text, train_dataset.label))
                ds = ds.batch(128).map(lambda x, y: (tokenizer(x), y))
                ds = ds.shuffle(ds.cardinality())

                train_split = ds.take(int(len(ds)*0.8))
                val_split = ds.skip(int(len(ds)*0.8)).take(int(len(ds)*0.2))

                logger.info("Model training started")

                histories = model.fit(
                    train_split,
                    validation_data=[val_split],
                    epochs=self.config.num_train_epochs,
                    batch_size=self.config.train_batch_size
                    )
                
                model.save(self.config.trained_model_path)

                logger.info(f"model saved at {self.config.trained_model_path} sucessfully")
        except Exception as e:
            logger.exception(e)
            raise e
        
        # plots 
        training_loss = histories.history.get('loss')
        validation_loss = histories.history.get('val_loss')

        # Check if loss and validation loss exist in histories
        if training_loss is None or validation_loss is None:
            raise ValueError("Both training loss and validation loss must be available in the history object.")
        # Plot training and validation loss over epochs
        plt.figure(figsize=(10, 6))
        plt.plot(training_loss, label='Training Loss')
        plt.plot(validation_loss, label='Validation Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.title('Training and Validation Loss Over Epochs')
        plt.legend()

        # Save the plot to the specified file path
        plt.savefig(self.config.root_dir)
        plt.close()

        
        # Save histories to a file
        file_path = os.path.join(self.config.root_dir,"training_histories.pkl")
        with open(file_path, 'wb') as f:
            pickle.dump(histories.history, f)
        f.close()





        