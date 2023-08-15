from signLanguage.constant import *
import subprocess
from signLanguage.exception import *


# Define the YOLOv5 training command
yolov5_command = [
    "python", "D:/msn/project/yolov5/train.py",
    "--img", f"{IMAGE_SIZE}",
    "--batch", f"{BATCH_SIZE}",
    "--epochs", f"{NUMBER_OF_EPOCHS}",
    "--data", "D:/msn/project/data.yaml",
    "--cfg", "D:/msn/project/yolov5/models/custom_yolov5s.yaml",
    "--weights", "yolov5s.pt",
    "--name", "yolov5s_results",
    "--cache"
]


def Training():
    try:
        subprocess.run(yolov5_command)
    except Exception as e:
        raise SignException(sys, e)