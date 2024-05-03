import os 
import sys
from src.retentiveGuard import logger

from src.retentiveGuard.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(self,config:DataValidationConfig) -> None:
        self.config = config
        
    
    def validate_all_folders_exist(self)-> bool:
        try:
            validation_status = True


            for folder in self.config.ALL_REQUIRED_FOLDERS:
                if not os.path.exists(folder):

                    validation_status = False
                    break

            with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
                
            return validation_status
        
        except Exception as e:
            raise logger.exception(e,sys)