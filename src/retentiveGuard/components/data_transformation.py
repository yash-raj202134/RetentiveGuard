import os 
from pandas import read_csv ,concat
import json
from tensorflow.keras.layers import TextVectorization
import tensorflow as tf
from src.retentiveGuard import logger

from src.retentiveGuard.entity.config_entity import DataTransformationConfig




class DataTransformation:
    def __init__(self,config:DataTransformationConfig) -> None:
        self.config = config

    
    def create_dataset(self):

        try:
            logger.info("Reading the datasets")
                
            # Loading the train_data

            train_dataset = read_csv('artifacts/data_ingestion/data1/train_essays.csv')[['text', 'generated']].rename(columns={'generated' : 'label'})

            # Loading the curated datasets
            curated_dataset = read_csv('artifacts/data_ingestion/data6/train_drcat_01.csv')[['text', 'label']].reset_index(drop=True)
            curated_dataset1 = read_csv('artifacts/data_ingestion/data6/train_drcat_02.csv')[['text', 'label']].reset_index(drop=True)
            curated_dataset2 = read_csv('artifacts/data_ingestion/data6/train_drcat_03.csv')[['text', 'label']].reset_index(drop=True)
            curated_dataset3 = read_csv('artifacts/data_ingestion/data6/train_drcat_04.csv')[['text', 'label']].reset_index(drop=True)

            curated_dataset4 = read_csv('artifacts/data_ingestion/data3/machine-train.csv')[['text']].reset_index(drop=True).assign(label=1)
            curated_dataset5 = read_csv('artifacts/data_ingestion/data3/machine-test.csv')[['text']].reset_index(drop=True).assign(label=1)

            curated_dataset6 = read_csv('artifacts/data_ingestion/data2/ai_generated_train_essays.csv')[['text']].reset_index(drop=True).assign(label=1)
            curated_dataset7 = read_csv('artifacts/data_ingestion/data2/ai_generated_train_essays_gpt-4.csv')[['text']].reset_index(drop=True).assign(label=1)

            curated_dataset9 = read_csv('artifacts/data_ingestion/data4/daigt_external_dataset.csv')[['text']].reset_index(drop=True).assign(label=1)
            curated_dataset10 = read_csv('artifacts/data_ingestion/data5/llama_70b_v1.csv')[['generated_text']].rename(columns={'generated_text' : 'text'}).reset_index(drop=True).assign(label=1)

            curated_dataset11 = read_csv('artifacts/data_ingestion/data5/falcon_180b_v1.csv')[['generated_text']].rename(columns={'generated_text' : 'text'}).reset_index(drop=True).assign(label=1)

            curated_dataset12 = read_csv('artifacts/data_ingestion/data7/train_v2_drcat_02.csv')[['text', 'label']].reset_index(drop=True)
            curated_dataset13 = read_csv('artifacts/data_ingestion/data8/persuade15_claude_instant1.csv')[['essay_text']].rename(columns={'essay_text' : 'text'}).reset_index(drop=True).assign(label=1)
            curated_dataset14 = read_csv('artifacts/data_ingestion/data9/LLM_generated_essay_PaLM.csv')[['text', 'generated']].rename(columns={'generated' : 'label'})
            curated_dataset15 = read_csv('artifacts/data_ingestion/data10/train_essays_RDizzl3_seven_v2.csv')[['text', 'label']].reset_index(drop=True)
            curated_dataset16 = read_csv('artifacts/data_ingestion/data10/train_essays_RDizzl3_seven_v1.csv')[['text', 'label']].reset_index(drop=True)
            curated_dataset17 = read_csv('artifacts/data_ingestion/data10/train_essays_7_prompts_v2.csv')[['text', 'label']].reset_index(drop=True)
            curated_dataset18 = read_csv('artifacts/data_ingestion/data10/train_essays_7_prompts.csv')[['text', 'label']].reset_index(drop=True)
            logger.info("dataset loaded sucessfully")
        except Exception as e:
            logger.exception(e)

        train_dataset = concat([train_dataset, 
                        curated_dataset, 
                        curated_dataset1,
                        curated_dataset2,
                        curated_dataset3,
                        curated_dataset4, 
                        curated_dataset5, 
                        curated_dataset6, 
                        curated_dataset7, 
                        curated_dataset9, 
                        curated_dataset10, 
                        curated_dataset11,
                        curated_dataset12, 
                        curated_dataset13, 
                        curated_dataset14,
                        curated_dataset15,
                        curated_dataset16,
                        curated_dataset17, 
                        curated_dataset18])
        
        train_dataset.to_csv(os.path.join(self.config.root_dir,"train_dataset.csv"))
        logger.info('Curated datasets concatinated and saved sucessfully')



    def preprocessAndTokenizeData(self):
        try:
            train_dataset = read_csv(os.path.join(self.config.root_dir,"train_dataset.csv"))

            train_dataset.text = train_dataset.text.str.replace('\n', ' ')

            tokenizer = TextVectorization(output_mode='int', output_sequence_length=512, standardize=None, ngrams=1)

            tokenizer.adapt(train_dataset.text)

            tokenizer_config = tokenizer.get_config()
         
            tokenizer_path = os.path.join(self.config.root_dir, "tokenizer_config.json")

            with open(tokenizer_path, 'w') as config_file:
                json.dump(tokenizer_config, config_file)

            # tf.keras.models.save_model(tokenizer,os.path.join(self.config.root_dir, "tokenizer.keras"))
            logger.info("Sucessfully saved the token")

        except Exception as e:
            logger.exception(e)





    


