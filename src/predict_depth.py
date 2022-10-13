"""
Main file
"""
# Imports
import os
import logging.config
import pathlib
from google.oauth2 import service_account

# Load environment variables
ENVIRONMENT = os.environ.get('ENVIRONMENT')
LOGGING_ENV = os.environ.get('LOGGING_ENV')
CREDENTIALS_PATH = os.environ.get('CREDENTIALS_PATH')

config_dir = os.path.join(pathlib.Path(__file__).parent.parent.parent.resolve(), 'config')

# load configuration file for logging
logging.config.fileConfig(fname=os.path.join(config_dir, 'logging.conf'),
                          disable_existing_loggers=False)
logger = logging.getLogger(LOGGING_ENV)

if __name__ == "__main__":

    # Loading credentials
    logger.info("Uploading credentials")
    credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)
    logger.info("Credentials uploaded")

    #  Get the output_images to run (if you don't need to run output_images, delete this code)
    queries_dir = os.path.join(pathlib.Path(__file__).parent.resolve(), 'output_images')
    files = os.listdir(queries_dir)

    # Getting the output_images to run for the directory
    queries = {}
    for file in files:
        if file.endswith(".sql"):
            with open(os.path.join(queries_dir, file), 'r', encoding='UTF-8') as f:
                query = f.read()
            query_name = file.split('.')[0]
            queries[query_name] = [query, None]

    # Your code here
