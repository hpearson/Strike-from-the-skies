'''
Used to test the application
'''
import flask_login
from flask import render_template
from strike import app, Storage
from strike.logic.mission import Mission
from strike.libraries import *


@app.route('/')
@flask_login.login_required
def index():
    ''' Route for 'hello_world' '''
    # Store the game object
    Storage.send(flask_login.current_user.id, Mission())
    # Read the game object
    mission = Storage.retrieve(flask_login.current_user.id)
    mission.mission_1()  # Calc the target
    mission.mission_2()  # Calc plane formation position
    mission.mission_3()  # Move the plane
    mission.mission_4()  # Calc the current weather
    mission.mission_5()  # Calculate stress to plane
    mission.mission_6()  # Spawn enemies
    mission.mission_7()  # Actions / Target enemies
    mission.mission_8()  # Enemies target
    mission.mission_9()  # Flak target
    mission.mission_10()  # Calculate damge to plane
    mission.mission_11()  # After round cleanup
    return render_template('home.html')


@app.route('/dashboard')
def dashboard():
    ''' Route for 'dashboard' '''
    return render_template('dashboard.html')
