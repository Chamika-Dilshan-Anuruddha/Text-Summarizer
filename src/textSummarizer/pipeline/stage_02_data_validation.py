
from textSummarizer.logging import logger
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation

STAGE_NAME='Data Validtion'

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(data_validation_config)
        data_validation.validate_all_files_exist()


if __name__=='__main__':
    try:
        logger.info(f">>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<\n\n")
    except Exception as e:
        raise e