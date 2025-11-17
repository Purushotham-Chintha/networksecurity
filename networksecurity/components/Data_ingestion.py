import os
import sys
from networksecurity.Exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
# Import data ingestion configuration
from networksecurity.entity.config_entity import DataIngestionconfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from typing import List
from pymongo.mongo_client import MongoClient

# import load_env and initialize it
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("Mongo_db_url")


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionconfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def extract_collection_as_dataframe(self):
        """
        Extract data from Mongo_db database
        :return: dataframe
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            pymongo_client = MongoClient(MONGO_DB_URL)
            collection = pymongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            # creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def split_data_as_a_train_test(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("Executed train_test_split on the dataframe")

            logging.info("Exited split data as train_test method of data ingestion class")

            dir_path = os.path.join(self.data_ingestion_config.data_ingested_dir)
            os.makedirs(dir_path, exist_ok=True)
            logging.info("Exporting train and test file path.")

            train_set.to_csv(self.data_ingestion_config.train_file_path, index=False, header=True)

            test_set.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)

            logging.info("Exported train and test file path.")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self):
        try:
            dataframe = self.extract_collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_a_train_test(dataframe)
            dataingestionartifact = DataIngestionArtifact(
                test_file_path=self.data_ingestion_config.test_file_path,
                trained_file_path=self.data_ingestion_config.train_file_path)

            return dataingestionartifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)


# if __name__ == "__main__":
#     dataingestion = DataIngestion(DataIngestionconfig(TrainingPipelineConfig()))
#     df = dataingestion.extract_collection_as_dataframe()
#     # print(df)
#     df = dataingestion.export_data_into_feature_store(df)
#     # print(df)
#     df = dataingestion.split_data_as_a_train_test(df)
#     print()