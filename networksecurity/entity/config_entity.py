import os
from datetime import datetime
from networksecurity.constant import traininig_pipeline

# print(traininig_pipeline.PIPELINE_NAME)


class TrainingPipelineConfig:
    def __int__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%M_%d_%Y_%H_%M_%S")
        self.pipeline_name = traininig_pipeline.PIPELINE_NAME
        self.artifact_name = traininig_pipeline.ARTIFACTS_DIRECTORY
        self.artifact_dir = os.path.join(self.artifact_name,timestamp)
        self.timestamp: str = timestamp


class DataIngestionconfig:
    def __init__(self,training_pipeline_config : TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir, traininig_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path = os.path.join(
            self.data_ingestion_dir, traininig_pipeline.DATA_INGESTION_FEATURE_STORE_DIR_NAME,
            traininig_pipeline.FILE_NAME
        )
        self.train_file_path = os.path.join(
            self.data_ingestion_dir,traininig_pipeline.DATA_INGESTION_INGESTED_DIR_NAME,
            traininig_pipeline.TRAIN_FILE_NAME
        )
        self.test_file_path = os.path.join(
            self.data_ingestion_dir, traininig_pipeline.DATA_INGESTION_INGESTED_DIR_NAME,
            traininig_pipeline.TEST_FILE_NAME
        )

        self.train_test_split_ratio: float = traininig_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name: str = traininig_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = traininig_pipeline.DATA_INGESTION_DATABASE_NAME
