'''
Bootstrap the application and set configs
'''
__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
import logging
import os
from datetime import datetime
import pickle

app = Flask('strike')
app.config['SECRET_KEY'] = 'Q3JlYXRlZCBieTogSHVudGVyIFBlYXJzb24='
app.debug = True
# Application configs
app.config['LOG_PATH'] = os.getcwd() + '\\strike\\log\\'
app.config['STORAGE'] = os.getcwd() + '\\strike\\storage\\'
app.config['CRED_STORAGE'] = os.getcwd() + '\\strike\\storage\\credentials\\'
# Database configs

# Dump in configurations
# Set flask logger to only show errors
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Setup for custom logger
app.log = logging.getLogger('Strike-from-the-skies')
logfile = app.config['LOG_PATH'] + datetime.now().strftime("%m.%d.%Y")+'.log'
text_format = '%(asctime)s | %(levelname)-10s | %(name)s | %(message)s'
time_format = "%m/%d/%Y %I:%M %p"
logging.basicConfig(filename=logfile, filemode='w', level=logging.INFO, format=text_format, datefmt=time_format)

# Flask setup settings (Debug)
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
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


class storage():
    def send(id, content):
        with open(f"{app.config['STORAGE'] + str(id)}.pkl", 'wb') as pickle_out:
            pickle.dump(content, pickle_out)

    def retrieve(id):
        with open(f"{app.config['STORAGE'] + str(id)}.pkl", 'rb') as pickle_in:
            unpickled_cucumber = pickle.load(pickle_in)
        return unpickled_cucumber


# app needs to be created before it can be used by the controllers
from strike.controllers import *  # noqa: E402 pylint: disable=C0413
