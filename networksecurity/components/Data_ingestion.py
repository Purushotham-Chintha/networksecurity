import os
import sys
from networksecurity.Exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
# Import data ingestion configuration
from networksecurity.entity.config_entity import DataIngestionconfig
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from typing import List

# import load_env and initialize it
from dotenv import load_dotenv
load_dotenv()




