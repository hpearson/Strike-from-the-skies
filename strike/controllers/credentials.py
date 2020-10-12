'''
Used to test the application
'''
import flask
import flask_login
from flask import render_template
from strike import app
from strike.libraries import *
from strike.models.users import users


# Prep for flask login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' Route for 'login' '''
    flask_login.logout_user()
    if flask.request.method == 'GET':
        return render_template('credentials/login.html')
    username = flask.request.form['username']
    password = flask.request.form['password']
    for _ in users:
        if username == _.username and password == _.password:
            flask_login.login_user(_)
            return flask.redirect(flask.url_for('protected'))
    return flask.redirect(flask.url_for('login'))


@app.route('/protected')
@flask_login.login_required
def protected():
    ''' Route for 'protected' '''
    return render_template('credentials/protected.html', flask_login=flask_login)


@app.route('/logout')
def logout():
    ''' Route for 'logout' '''
    flask_login.logout_user()
    return render_template('credentials/logout.html')


@app.route('/unauthorized')
@login_manager.unauthorized_handler
def unauthorized_handler():
    ''' Route for 'Unauthorized' '''
    return render_template('credentials/unauthorized.html')


@login_manager.user_loader
def user_loader(key):
    ''' reload DB from session '''
    for user in users:
        if user.id == key:
            return user
    return False
