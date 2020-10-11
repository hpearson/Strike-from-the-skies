'''
Used to interact with sqlite database
'''
import flask_login


class User(flask_login.UserMixin):
    pass


#####################################
# Load mock database
users = {'asd': {'password': 'asd'}}
#####################################
