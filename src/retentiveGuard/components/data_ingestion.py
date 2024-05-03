import os
import subprocess
import zipfile
from src.retentiveGuard import logger
from pathlib import Path

# Import necessary entities and utilities from your project
from src.retentiveGuard.entity.config_entity import DataIngestionConfig

# Import Kaggle API
from kaggle.api.kaggle_api_extended import KaggleApi


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initialize the DataIngestion class with a DataIngestionConfig instance.
        """
        self.config = config
        self.kaggle_api = KaggleApi()
        self.kaggle_api.authenticate()  # Authenticate with Kaggle using your API key

    def download_datasets(self):
        """
        Download all datasets specified in the DataIngestionConfig instance using the Kaggle API.
        """
        source_url = self.config.source_URL
        local_file_path = self.config.local_data_file

        if self.config.type == 'competition':
            command = f'kaggle competitions download -c {source_url} -p {local_file_path.parent}'
        
        else:
            command = f'kaggle datasets download -d {source_url} -p {local_file_path.parent}'

         # Run the Kaggle API command to download the data
        subprocess.run(command, shell=True, check=True)
        logger.info(f"Downloaded data from {source_url} into {local_file_path}")


    
    def extract_datasets(self):
        """
        Extract all downloaded ZIP files into their respective directories.
        """
        local_file_path = self.config.local_data_file
        unzip_path = self.config.unzip_dir

        # Create the unzip directory if it does not exist
        os.makedirs(unzip_path, exist_ok=True)

        # Unzip the file
        with zipfile.ZipFile(local_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted {local_file_path} into {unzip_path}")

        # Remove the local ZIP file to save disk space
        try:
            os.remove(local_file_path)
            logger.info(f"Removed local ZIP file: {local_file_path}")
        except Exception as e:
            logger.error(f"Failed to remove local ZIP file: {local_file_path}", exc_info=True)
            raise e



    
    # def run_data_ingestion(self):
    #     """
    #     Run the entire data ingestion process: download and extract datasets.
    #     """
    #     self.download_datasets()
    #     self.extract_datasets()


