'''
Used to test the application
'''
from flask import render_template, session
from strike import app, storage
from strike.objects.game import Game
from strike.objects.mission import Mission
from strike.libraries import *
# from strike.models.store import *

import flask_login


@app.route('/')
def hello_world():
    if not session.get('id'):
        session['id'] = str(uuid.uuid4())

    storage.send(session['id'], Mission())
    mission = storage.retrieve(session['id'])
    mission.mission_1()
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
@flask_login.login_required
def dashboard():
    app.log.info('logged in successfully')
    return render_template('dashboard.html')
