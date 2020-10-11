'''
Used to test the application
'''
import flask
import flask_login
from strike import app
from strike.libraries import *
from strike.models.users import User, users


# Prep for flask login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    flask_login.logout_user()
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='username' id='username' placeholder='username'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    username = flask.request.form['username']
    password = flask.request.form['password']

    for _ in users:
        if username == _.username and password == _.password:
            flask_login.login_user(_)
            return flask.redirect(flask.url_for('protected'))
    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + str(flask_login.current_user.id) + flask_login.current_user.username


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


# Reread the user session
@login_manager.user_loader
def user_loader(id):
    # User already signed in so reload DB
    user = users[int(id)]
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'
