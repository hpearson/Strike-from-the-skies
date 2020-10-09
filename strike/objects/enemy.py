'''
Setup a class to hold the enemy information
'''
from strike.libraries import *


class Enemy():
    ''' Setup Mission Vars '''
    def __init__(self):
        ''' Prep Init Values '''
        self.type = roll_list(['Me 109', 'Me 101', 'Fw 190'])
        self.position = roll_list(['10:30', '12:00', '1:30', '3:00', '6:00', '9:00'])
        self.elevation = roll_list(['Low', 'Level', 'High'])
        self.alive = True
