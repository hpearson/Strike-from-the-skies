'''
Used to interact with sqlite database
'''
import flask_login
import json
from strike import app


class User(flask_login.UserMixin):
    ''' Setup Mission Vars '''
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


#####################################
# Load creds from JSON file
users = []
with open(app.config['CRED_STORAGE'] + 'users.json', 'r') as read_file:
    file = json.load(read_file)
    for _ in file['users']:
        users.append(User(_['id'], _['username'], _['password']))
#####################################
