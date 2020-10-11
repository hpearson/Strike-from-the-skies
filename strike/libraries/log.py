'''
Use this libarie create console logs & print to file
'''
import logging
from datetime import datetime
from strike import app
import flask_login


class Log():
    ''' Setup Log Vars '''
    def __init__(self, text):
        '''
        Setup and load logging configs
        '''

        text = f'{flask_login.current_user.username} | {text}'


        # Print to console
        print(text)
        # Save into the log
        app.log.info(text)
