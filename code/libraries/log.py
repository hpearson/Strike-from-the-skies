'''
Use this libarie create console logs & print to file
'''
import logging
import os
from datetime import datetime

def log(log_info):
	'''
	Setup and load logging configs
	'''
	logfile = os.getcwd() + '\\..\\logs\\' # Go up 1 DIR and into 'logs' folder
	logfile += datetime.now().strftime("%m.%d.%Y_%H.%M.%S")+'.log'
	handler = logging.FileHandler(logfile)

	text_format = '%(asctime)s | %(levelname)-10s | %(name)s | %(message)s'
	time_format = "%m.%d.%Y %H.%M.%S"

	formatter = logging.Formatter(text_format, time_format)
	handler.setFormatter(formatter)
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.INFO)

	# Do not reattach a handle if there already is one.
	if not logger.handlers:
		logger.addHandler(handler)

	# Print to console
	print(log_info)
	# Print to log file
	logger.info(log_info)
