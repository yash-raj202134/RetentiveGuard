
from src.retentiveGuard.config.configuration import ConfigurationManager
from src.retentiveGuard.components.data_ingestion import DataIngestion
from src.retentiveGuard import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        """
        Initialize the DataIngestionPipeline.
        """
        self.config_manager = ConfigurationManager(config_filepath='config/config.yaml',params_filepath='params.yaml')



    def main(self):
        """
        Main method to handle data ingestion.
        """
        try:
            data_ingestion_configs = self.config_manager.get_data_ingestion_config()

            for config in data_ingestion_configs:
                data_ingestion = DataIngestion(config=config)
                data_ingestion.download_datasets()
                data_ingestion.extract_datasets()

            # # Instantiate the configuration manager
            # config_manager = ConfigurationManager()
            # # Retrieve data ingestion configuration
            # data_ingestion_configs = config_manager.get_data_ingestion_config()

            # # Loop through each data ingestion configuration and perform data ingestion
            # for data_ingestion_config in data_ingestion_configs:
            #     # Initialize DataIngestion with the current configuration
            #     data_ingestion = DataIngestion(config=data_ingestion_config)
                
            #     # Run the data ingestion process
            #     logger.info(f"Processing data ingestion for source URL: {data_ingestion_config.source_URL}")
            #     data_ingestion.download_datasets()
            #     data_ingestion.extract_datasets()
            #     logger.info(f"Completed data ingestion for source URL: {data_ingestion_config.source_URL}")

        except Exception as e:
            # Handle exceptions and log the error
            logger.exception("Error during data ingestion pipeline", exc_info=True)
            raise e


if __name__ == '__main__':
    # Run the data ingestion pipeline
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        pipeline = DataIngestionPipeline()
        pipeline.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
