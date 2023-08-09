from coffee_cnn_Classifier.config import ConfigurationManager
from coffee_cnn_Classifier.components import Evaluation
from coffee_cnn_Classifier import logger


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()