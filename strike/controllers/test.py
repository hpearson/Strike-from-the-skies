'''
Used to test the application
'''
from flask import render_template, session
from strike import app
from strike.objects.game import Game
from strike.libraries import *


@app.route('/')
def hello_world():
    Game()
    return render_template('home.html')


@app.route('/dashboard')
def dashboard():
    app.log.info('logged in successfully')
    return render_template('dashboard.html')
