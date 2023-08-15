from signLanguage.logger import logging
from signLanguage.exception import *
from signLanguage.constant import *
import yaml
import subprocess

class DataIngestionTraining:
    def __init__(self):
        logging.info("initializing the Training and Validation path")
        self.train_path = TRAINING_DATA_PATH
        self.valid_path = VALID_DATA_PATH
        logging.info(f"Training_path : {self.train_path} and Validation path : {self.valid_path}")

    @staticmethod
    def Clone_Git_Repo():
        try:
            logging.info("initiating git cloning for YOLO5 Repository")
            repository_url = "https://github.com/ultralytics/yolov5.git"
            destination_folder = "yolov5"
            # Run the git clone command
            subprocess.run(["git", "clone", repository_url, destination_folder])
            logging.info("Repository cloned successfully.")
        except Exception as e:
            raise SignException(sys, e)

    def Write_Yaml(self):
        try:
            logging.info(f"writing project yaml file")

            data = {
                'train': f"{self.train_path}",
                'val': f"{self.valid_path}",
                'nc': NUMBER_OF_CLASS,
                'names': CLASS_LABEL_LIST
            }
            # Specify the file name you want to save to
            filename = 'data.yaml'
            with open(filename, 'w') as file:
                yaml.dump(data, file)

            logging.info(f"{filename} is created")
        except Exception as e:
            raise SignException(sys, e)

    @staticmethod
    def Updating_Yolo5_YAML():
        try:
            original_yolo5_yaml = "D:/msn/project/yolov5/models/yolov5s.yaml"
            updated_yolo_file = "D:/msn/project/yolov5/models/custom_yolov5s.yaml"

            # Read the YAML file
            logging.info(f"Reading {original_yolo5_yaml}")
            with open(original_yolo5_yaml, 'r') as file:
                data = yaml.safe_load(file)
            # Update the name in the YAML data
            data['nc'] = NUMBER_OF_CLASS

            # Write the updated data to a new YAML file
            logging.info(f"updating {original_yolo5_yaml} to {updated_yolo_file} ")
            with open(updated_yolo_file, 'w') as file:
                yaml.dump(data, file)
            logging.info("required setup :done")
            logging.info("model training initiated")
        except Exception as e:
            raise SignException(sys, e)
