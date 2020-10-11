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
# Load mock database
users = [
    User(0, 'Hunter', 'Pearson'),
    User(1, 'asd', 'asd')
]
#####################################
