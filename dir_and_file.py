import os
import logging
from pathlib import Path

project_name = "signLanguage"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_predictor.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",

    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",

]
for i in list_of_files:
    file_path, file_name = os.path.split(i)

    if file_path != "":
        os.makedirs(file_path, exist_ok=True)
        logging.info(f"Creating directory: {file_path} for the file {file_name}")

    if (not os.path.exists(file_name)) or (os.path.getsize(file_name) == 0):
        with open(i, 'w') as f:
            pass
            logging.info(f"Creating empty file: {file_name}")

    else:
        logging.info(f"{file_name} is already created")


