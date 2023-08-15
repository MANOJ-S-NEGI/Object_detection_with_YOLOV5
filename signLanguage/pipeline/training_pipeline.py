from signLanguage.components.data_ingestion import DataIngestionTraining
from signLanguage.components.data_Training import Training
from signLanguage.exception import *


class DataValidation:
    def __init__(self):
        self.DataIngestionTraining = DataIngestionTraining()

    def IngestionModule(self):
        try:
            cloning_git = DataIngestionTraining.Clone_Git_Repo()
            write_yml = self.DataIngestionTraining.Write_Yaml()
            yolo_yaml = DataIngestionTraining.Updating_Yolo5_YAML()

        except Exception as e:
            raise SignException(sys, e)

    @staticmethod
    def TrainingModule():
        Training()


def Validation_Call():
    DataValidation().IngestionModule()
    DataValidation.TrainingModule()

















