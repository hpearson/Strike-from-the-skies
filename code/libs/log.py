'''
Use this libarie create console logs & print to file
'''
import logging
import os
from datetime import datetime


class Log():
    ''' Setup Mission Vars '''
    def __init__(self, text):
        self.logger = None

        # Is logger already available (Loggers are global)?
        self.logger = logging.getLogger('Strike-from-the-skies')
        if not self.logger.handlers:
            # Setup and load logging configs
            logfile = os.getcwd() + '\\..\\log\\'  # Go up 1 DIR and into 'logs' folder
            logfile += datetime.now().strftime("%m.%d.%Y")+'.log'

            text_format = '%(asctime)s | %(levelname)-10s | %(name)s | %(message)s'
            time_format = "%m/%d/%Y %I:%M %p"

            logging.basicConfig(filename=logfile, filemode='w', level=logging.INFO, format=text_format, datefmt=time_format)

        # Create and info log
        print(text)
        self.logger.info(text)
