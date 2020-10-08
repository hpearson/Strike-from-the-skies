'''
Bootstrap the application and set configs
'''
__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask('__name__')
app.config['SECRET_KEY'] = 'Q3JlYXRlZCBieTogSHVudGVyIFBlYXJzb24='
# Ensure that debug mode is *on*
app.debug = True

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

from flask import render_template

@app.route('/')
def hello_world():
    ''' Used to test Flask '''
    #return 'Hello, World!'
    return render_template('hello_world.html')
