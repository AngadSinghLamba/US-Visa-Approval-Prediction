import os
from us_visa.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
"""
This line generates a timestamp string representing the current date and time in the format "month_day_year_hour_minute_second".

"""

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP
"""
This defines a data class TrainingPipelineConfig with attributes pipeline_name, artifact_dir, and timestamp.
 Default values are provided for pipeline_name and artifact_dir. artifact_dir is set 
 to a combination of ARTIFACT_DIR (a constant) and the generated timestamp.
"""

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

"""
This line creates an instance of TrainingPipelineConfig class named training_pipeline_config.
"""
@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME

"""
This defines a data class DataIngestionConfig with attributes related to data ingestion.
 It uses training_pipeline_config.artifact_dir to construct file paths for data ingestion, 
 including feature store file path, training file path, and testing file path.
"""

@dataclass
class DataValidationConfig:
    pass
"""
This defines a data class DataValidationConfig without any attributes for now.
 It's a placeholder for future use.
 """

