
from src.retentiveGuard.config.configuration import ConfigurationManager
from src.retentiveGuard.components.data_transformation import DataTransformation
from src.retentiveGuard.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from src.retentiveGuard import logger

STAGE_NAME='Data Transformation Stage'

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        
        config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH)
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.create_dataset()
        data_transformation.preprocessAndTokenizeData()




if __name__ == '__main__':
    # Run the data transformation pipeline
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        pipeline = DataTransformationPipeline()
        pipeline.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
