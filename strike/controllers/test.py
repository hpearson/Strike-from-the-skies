'''
Used to test the application
'''
from flask import render_template, session
from strike import app, storage
from strike.objects.game import Game
from strike.objects.mission import Mission
from strike.libraries import *
# from strike.models.store import *
import uuid


@app.route('/')
def hello_world():
    if not session.get('id'):
        session['id'] = str(uuid.uuid4())

    storage.send(session['id'], Mission())
    storage.retrieve(session['id']).mission_1()
    return render_template('home.html')


@app.route('/dashboard')
def dashboard():
    app.log.info('logged in successfully')
    return render_template('dashboard.html')
