'''
Setup a class to hold the plane information
'''
from strike.logic.crew import Crew


class Plane():
    ''' Setup Game Vars '''
    def __init__(self):
        ''' Prep Init Values '''
        self.max_speed = 300
        self.cur_speed = 100
        self.seats = {
                        'Bombardier': Crew('Bombardier'),
                        'Navigator': Crew('Navigator'),
                        'Pilot': Crew('Pilot'),
                        'CoPilot': Crew('CoPilot'),
                        'Engineer': Crew('Engineer'),
                        'Radio': Crew('Radio'),
                        'Ball': Crew('Ball'),
                        'Port': Crew('Port'),
                        'Starboard': Crew('Starboard'),
                        'Tail': Crew('Tail')
        }
        self.sections = {
                            'Nose': 10,
                            'Pilot': 10,
                            'Middle': 10,
                            'Tail': 10,
                            'Port': 10,
                            'Starboard': 10
        }
