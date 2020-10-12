'''
Use this libarie create console logs & print to file
'''
import flask_login
from strike import app


class Log():
    ''' Setup Log Vars '''
    def __init__(self, text):
        '''
        Setup and load logging configs
        '''
        # Add username if user is signed in
        if hasattr(flask_login.current_user, 'username'):
            text = f'{flask_login.current_user.username} | {text}'
        # Print to console
        print(text)
        # Save into the log
        app.log.info(text)
