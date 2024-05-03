# Entity
from dataclasses import dataclass , field
from pathlib import Path
from typing import List

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    type: str
    local_data_file: Path
    unzip_dir: Path



@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE: str
    ALL_REQUIRED_FOLDERS: List[Path] =  field(default_factory=list)