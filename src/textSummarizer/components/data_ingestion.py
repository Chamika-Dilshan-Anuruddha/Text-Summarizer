import os
import urllib.request as request
from zipfile import ZipFile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig

class DataIgestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with following info: {headers}")
        else:
            logger.info(f"File already exists of size: {get_size(self.config.local_data_file)}")

    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with ZipFile(self.config.local_data_file, 'r') as f:
            f.extractall(unzip_path)
    
    