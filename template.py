import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, # Sets the logging level to INFO (logs messages with INFO level and higher. eg. e.g., INFO, WARNING, ERROR, CRITICAL) 
    format='[%(asctime)s]: %(message)s:')  # Defines the format of the log messages (placeholder to be replaced with the timestamp of the log message in a human-readable format,and to be replaced with the actual log message content. )


project_name = "coffee_cnn_Classifier"

list_of_files = [
    ".github/workflows/.gitkeep",  # to ensure that an empty directory is not ignored or deleted by Git.
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # The File dir
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  #  exist_ok=True-->to avoid raising an error if the directory already exists.
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # The files
    # a file specified by  the path either does not exist or has a size of 0 (i.e., it is an empty file). If either condition is true, it creates an empty file at the specified path
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # create the file if it does not exist or truncate (empty) the file if it does exist.
        with open(filepath, 'w') as f: # open the file in write mode
            pass #creating an empty file only
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")




