
from src.retentiveGuard.config.configuration import ConfigurationManager
from src.retentiveGuard.components.base_model_configuration import BaseModel
from src.retentiveGuard.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from src.retentiveGuard import logger

STAGE_NAME='Base model Configuration Stage'

class BasemodelConfigurationPipeline:
    def __init__(self):
        pass

    def main(self):
        
        config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH)
        base_model_config = config.get_model_configuration_config()
        base_model = BaseModel(config=base_model_config)
        tokenizer = base_model.load_dataset()
        model = base_model.base_model_builder(tokenizer=tokenizer)
        base_model.save_base_model(model=model)




if __name__ == '__main__':
    # Run the data transformation pipeline
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        pipeline = BasemodelConfigurationPipeline()
        pipeline.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
