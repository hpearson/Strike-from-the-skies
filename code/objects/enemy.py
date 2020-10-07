'''
Setup a class to hold the enemy information
'''
from libs.tools import roll_list


class Enemy():
    ''' Setup Mission Vars '''
    def __init__(self):
        ''' Prep Init Values '''
        self.type = roll_list(['Me 109', 'Me 101', 'Fw 190'])
        self.position = roll_list(['12:00', '1:30', '3:00', '4:30', '6:00', '7:30', '9:00', '10:30'])
        self.elevation = roll_list(['Low', 'Level', 'High'])
        self.alive = True
