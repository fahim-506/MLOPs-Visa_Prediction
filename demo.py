# # from us_visa.logger import logging
# # from us_visa.exception import UsVisaException
# # import sys

# # logging.info("Welcome To Our Custom Log")

# # try:
# #     a = 2/0
# # except Exception as e:
# #     raise UsVisaException(e,sys)

# # changes
# import os
# from us_visa.constants import *
# mongo_db_url = MONGODB_URL_KEY
# print(mongo_db_url)
# # changes after pipeline train
from dotenv import load_dotenv
load_dotenv()

from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()