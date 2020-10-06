'''
Setup a class to hold the plane information
'''
from objects.crew import Crew
from objects.position import Position


class Plane():
    ''' Setup Game Vars '''
    def __init__(self):
        ''' Prep Init Values '''
        self.max_speed = 300
        self.cur_speed = 100

        self.positions = {
            'Bombardier Seat': Position('Bombardier Seat', Crew('Bombardier')),
            'Navigator Seat': Position('Navigator Seat', Crew('Navigator')),
            'Pilot Seat': Position('Pilot Seat', Crew('Pilot')),
            'CoPilot Seat': Position('CoPilot Seat', Crew('CoPilot')),
            'Engineer Pannel': Position('Engineer Seat', Crew('Engineer')),
            'Radio Seat': Position('Radio Seat', Crew('Radio')),
            # 'Ventral Turret': Position('Ventral Turret'),
            'Port Cheek': Position('Port Cheek'),
            'Starboard Cheek': Position('Starboard Cheek'),
            'Dorsal Turret': Position('Dorsal Turret'),
            'Dorsal': Position('Dorsal'),
            'Ventral Ball Turret': Position('Ventral Ball Turret', Crew('Radio')),
            'Port Waist': Position('Port Waist', Crew('Radio')),
            'Starboard Waist': Position('Starboard Waist', Crew('Radio')),
            'Tail Turret': Position('Tail Turret', Crew('Radio'))
        }
        self.sections = {
            'Nose': 10,
            'Pilot': 10,
            'Middle': 10,
            'Tail': 10,
            'Port': 10,
            'Starboard': 10
        }
