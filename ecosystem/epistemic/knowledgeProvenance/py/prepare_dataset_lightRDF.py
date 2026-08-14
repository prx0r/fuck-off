import gc

import lightrdf

from Logger import DebugLogger
import configparser
from datetime import datetime
import pandas as pd
from collections import defaultdict

from prepare_dataset.extract_coreKB_facts_lightRDF import extract_facts

# Logger
Logger = DebugLogger(name="preprocess",
                     path_to_properties="../properties/prepare_dataset.ini")

Logger.logger.info(f'-----\nBeginning of Dataset Preparation (run: {datetime.now()})\n-----')

# Instantiate configurations
properties_file = "../properties/prepare_dataset.ini"
config = configparser.ConfigParser()
config.optionxform = str
config.read(properties_file)

datadir = config["PATHS"]["datadir"]

# Load dump graph into memory
dump = lightrdf.RDFDocument(datadir+config["PATHS.DATASET"]["ttl"])

Logger.logger.info(f"+++ Extracting GCS facts and sentences from dump +++")
gcs, gcs_sentence = extract_facts(dump, Logger.logger)
Logger.logger.info(f"Finish test at {datetime.now()}")
Logger.logger.info(f"+++ Saving GCS facts in a CSV file +++")
gcs.to_csv(datadir+config["PATHS.OUTPUT"]["gcs"], index=False)

# delete GCS dataframe to reduce memory consumption
del gcs
gc.collect()

Logger.logger.info(f"+++ Saving sentences supporting GCS facts in a CSV file +++")
gcs_sentence.to_csv(datadir+config["PATHS.OUTPUT"]["gcs_sentence"], index=False)

Logger.logger.info(f'-----\nDataset preparation completed at {datetime.now()}\n-----')