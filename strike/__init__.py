'''
Bootstrap the application and set configs
'''
__version__ = '0.1'
import logging
import os
import pickle
from datetime import datetime
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


app = Flask('strike')
app.config['SECRET_KEY'] = 'Q3JlYXRlZCBieTogSHVudGVyIFBlYXJzb24='
app.debug = True
# Application configs
app.config['LOG_PATH'] = os.getcwd() + '\\strike\\log\\'
app.config['STORAGE'] = os.getcwd() + '\\strike\\storage\\'
app.config['CRED_STORAGE'] = os.getcwd() + '\\strike\\models\\'
# Database configs

# Dump in configurations
# Set flask logger to only show errors
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Setup for custom logger
app.log = logging.getLogger('Strike-from-the-skies')
logging.basicConfig(
    filename=app.config['LOG_PATH'] + datetime.now().strftime("%m.%d.%Y")+'.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-10s | %(name)s | %(message)s',
    datefmt="%m/%d/%Y %I:%M %p"
)

# Flask setup settings (Debug)
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_PANELS'] = [
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
]


class Storage():
    ''' Used to send/retrieve pickle files '''
    @staticmethod
    def send(key, content):
        ''' Send python to pickle file '''
        with open(f"{app.config['STORAGE'] + key}.pkl", 'wb') as pickle_out:
            pickle.dump(content, pickle_out)

    @staticmethod
    def retrieve(key):
        ''' Read pickle file into python '''
        with open(f"{app.config['STORAGE'] + key}.pkl", 'rb') as pickle_in:
            unpickled_cucumber = pickle.load(pickle_in)
        return unpickled_cucumber


# app needs to be created before it can be used by the controllers
from strike.controllers import *  # noqa: E402 pylint: disable=C0413
