import os
import subprocess
import zipfile
from src.retentiveGuard import logger
from pathlib import Path

# Import necessary entities and utilities from your project
from src.retentiveGuard.utils.common import create_directories
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



        # # Iterate through each dataset in the configuration
        # for dataset_config in self.config.datasets:
        #     source_url = dataset_config.source_URL
        #     local_file_path = dataset_config.local_data_file
        #     unzip_dir = dataset_config.unzip_dir

        #     # Create necessary directories for the local data file and unzip directory
        #     create_directories([local_file_path.parent, unzip_dir])

        #     try:
        #         # Log the start of the download
        #         logger.info(f"Downloading data from {source_url} into {local_file_path}.")
                
        #         # Download the dataset using the Kaggle API
        #         if dataset_config.type == "competition":
        #             self.kaggle_api.competitions_download_files(source_url, path=str(local_file_path))
        #         else:
        #             self.kaggle_api.dataset_download_files(source_url, path=str(local_file_path))

        #         logger.info(f"Downloaded data from {source_url} into {local_file_path}.")
                
        #     except Exception as e:
        #         # Log the error if the download fails
        #         logger.error(f"Failed to download data from {source_url}: {e}")
        #         raise e
    
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



        # # Iterate through each dataset in the configuration
        # for dataset_config in self.config.datasets:
        #     local_file_path = dataset_config.local_data_file
        #     unzip_dir = dataset_config.unzip_dir

        #     try:
        #         # Log the start of the extraction
        #         logger.info(f"Extracting data from {local_file_path} to {unzip_dir}.")
                
        #         # Extract the ZIP file into the unzip directory
        #         with zipfile.ZipFile(local_file_path, 'r') as zip_ref:
        #             zip_ref.extractall(unzip_dir)
                
        #         logger.info(f"Extracted data from {local_file_path} to {unzip_dir}.")
                
        #     except Exception as e:
        #         # Log the error if the extraction fails
        #         logger.error(f"Failed to extract data from {local_file_path}: {e}")
        #         raise e
    
    # def run_data_ingestion(self):
    #     """
    #     Run the entire data ingestion process: download and extract datasets.
    #     """
    #     self.download_datasets()
    #     self.extract_datasets()


