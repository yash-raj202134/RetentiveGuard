# Import necessary modules and classes
from pathlib import Path
from typing import List

# Replace cnnClassifier imports with appropriate imports from your project
from src.retentiveGuard.utils.common import read_yaml, create_directories
from src.retentiveGuard.entity.config_entity import DataIngestionConfig

# Define constants for configuration file paths
CONFIG_FILE_PATH = Path("config/config.yaml")  # Path to your config.yaml file
PARAMS_FILE_PATH = Path("params.yaml")  # Path to your params.yaml file (if used)

class ConfigurationManager:
    def __init__(self, config_filepath:Path, params_filepath:Path):
      
        # Load configuration files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath) if params_filepath else None

        # Create necessary directories
        # create_directories([self.config['artifacts_root']])

    def get_data_ingestion_config(self) -> List[DataIngestionConfig]:
        """
        Create and return a list of DataIngestionConfig instances based on the data_ingestion section
        in the config.yaml file.

        Returns:
            List[DataIngestionConfig]: A list of DataIngestionConfig instances.
        """
        data_ingestion = self.config['data_ingestion']
        root_dir = Path(data_ingestion['root_dir'])
        # datasets_config = data_ingestion_section['datasets']

        # # Create directories for each dataset if they don't already exist
        # for dataset in datasets_config:
        #     create_directories([dataset['unzip_dir']])

        # Create a list to hold DataIngestionConfig instances
        data_ingestion_configs = []

        # Iterate through each dataset in the config file
        for dataset in data_ingestion['datasets']:
            # Create a DataIngestionConfig instance for each dataset
            data_ingestion_config = DataIngestionConfig(
                root_dir=root_dir,
                source_URL=dataset['source_URL'],
                type = dataset['type'],
                local_data_file=Path(dataset['local_data_file']),
                unzip_dir=Path(dataset['unzip_dir'])
            )
            # Append the instance to the list
            data_ingestion_configs.append(data_ingestion_config)

        return data_ingestion_configs
