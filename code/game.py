'''
Setup a class to hold the game information
'''

import mission


class Game():
    ''' Setup Game Vars '''
    def __init__(self):
        # Start at mission zero
        self.mission = 0
        # Gen a new Mission
        self.mission = mission.Mission()

        # Game Loop
        self.mission.mission_1()  # Calc target (Name, Location, Distance)
        self.mission.mission_2()  # Calc plane formation position
        # Loop
        while not self.mission.mission_ended:
            self.mission.mission_3()  # Calc the current weather
            self.mission.mission_4()  # Move the plane
            self.mission.mission_5()  # Spawn enemies
            self.mission.mission_6()  # Target enemies
            self.mission.mission_7()  # Enemies target
