import os
import sys
import pandas as pd
import numpy as np


"""
defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACTS_DIRECTORY: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"


TEST_FILE_NAME: str = "test.csv"
TRAIN_FILE_NAME: str = "train.csv"





"""
Data ingestion related constants start with DATA INGESTION followed by VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = "networkdata"
DATA_INGESTION_DATABASE_NAME: str = "NetworkSecurity"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR_NAME: str = "feature_store"
DATA_INGESTION_INGESTED_DIR_NAME: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
