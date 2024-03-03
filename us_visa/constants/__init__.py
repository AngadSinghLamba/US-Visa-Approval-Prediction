import os
from datetime import date

DATABASE_NAME = "US_VISA"
"""
Specifies the name of the database where the data will be stored. In this case, it's "US_VISA".
"""

COLLECTION_NAME="visa_data"
"""
Defines the name of the collection within the database where visa data will be stored, which is "visa_data
"""

MONGODB_URL_KEY = "MONGODB_URL"
"""
Represents the key used to access the MongoDB URL where the data will be stored or accessed
"""

PIPELINE_NAME: str = "usvisa"
"""
 Indicates the name of the pipeline being used for the US visa project, which is "usvisa".
"""

ARTIFACT_DIR: str = "artifact"
"""
Specifies the directory where artifacts generated during the project will be stored, such as models and preprocessing objects.

"""

MODEL_FILE_NAME= "model.pkl"

"""
Defines the name of the file where the trained model will be saved, which is "model.pkl".
"""

TARGET_COLUMN = "case_status"
"""
 Represents the target column in the dataset, which is "case_status".
"""
CURRENT_YEAR = date.today().year
"""
Stores the current year using Python's date.today().year function.
"""
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
"""
 Specifies the name of the file where the preprocessing object will be saved, which is "preprocessing.pkl".
"""


FILE_NAME: str = "usvisa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

"""
These constants represent the names of files containing the entire dataset, training dataset, and testing dataset, respectively.
"""

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME

These constants are related to data ingestion processes, including the collection name, directory names, 
and file structure for storing ingested data and feature stores.
"""

DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2



"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""

"""
This will create a Data validation folder, drfit report file name along with the drift report.  

"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

"""
Data Transformation ralated constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed" # Here we will save the test and train.npy
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object" # Here we will save the preprocessed model.pkl file


"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")