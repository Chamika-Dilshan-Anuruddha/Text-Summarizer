from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIgestion
from textSummarizer.logging import logger


STAGE_NAME="Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIgestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<")
    except Exception as e:
        raise e