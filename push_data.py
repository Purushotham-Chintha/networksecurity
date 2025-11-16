import os
import sys
import pandas as pd
import numpy as np
import json
import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from networksecurity.Exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from dotenv import load_dotenv
load_dotenv()

ca = certifi.where()

Mongo_db_url = os.getenv("Mongo_db_url")

# print(Mongo_db_url)

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection

            self.mongo_client = MongoClient(Mongo_db_url)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)

            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    file_path = "Network_Data/phisingData.csv"

    Database = "NetworkSecurity"
    Collection = "networkdata"

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=file_path)
    print(records)

    no_of_records = networkobj.insert_data_mongodb(records=records, database=Database, collection=Collection)
    print(no_of_records)
