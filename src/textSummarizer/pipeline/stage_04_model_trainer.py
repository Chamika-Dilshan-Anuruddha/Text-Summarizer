
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger

STAGE_NAME="Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(model_trainer_config)
        model_trainer.train()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<\n\n")
    except Exception as e:
        raise e