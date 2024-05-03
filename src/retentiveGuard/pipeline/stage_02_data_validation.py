

from src.retentiveGuard.config.configuration import ConfigurationManager
from src.retentiveGuard.components.data_validation import DataValidation
from src.retentiveGuard.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from src.retentiveGuard import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        
        config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH)
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_folders_exist()




if __name__ == '__main__':
    # Run the data ingestion pipeline
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        pipeline = DataValidationPipeline()
        pipeline.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
