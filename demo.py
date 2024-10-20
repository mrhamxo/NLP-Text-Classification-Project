from normal_hate.logger import logging
from normal_hate.exception import CustomException
import sys
#from normal_hate.configuration.gcloud_syncer import GCloudSync

#obj = GCloudSync()
#obj.sync_folder_from_gcloud("hate-speech2024", "dataset.zip", "download/dataset.zip")

#logging.info("welcome to our project")

try:
    a = 7 / 1178
    print(a)
except Exception as e:
    raise CustomException(e, sys) from e 
