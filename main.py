# main file
from src.retentiveGuard import logger
from src.retentiveGuard.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.retentiveGuard.pipeline.stage_02_data_validation import DataValidationPipeline
from src.retentiveGuard.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.retentiveGuard.pipeline.stage_04_base_model_configuration import BasemodelConfigurationPipeline

STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    pipeline = DataTransformationPipeline()
    pipeline.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Base Model Building stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    pipeline = BasemodelConfigurationPipeline()
    pipeline.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e