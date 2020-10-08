'''
Setup a class to hold the game information
'''
import os
from objects.mission import Mission
# Set the OS CWD to script location
os.chdir(os.path.dirname(os.path.realpath(__file__)))


class Game():
    ''' Setup Game Vars '''
    def __init__(self):
        # Start at mission zero
        self.mission = 0
        # Gen a new Mission
        self.mission = Mission()

        # Game Loop
        self.mission.mission_1()  # Calc target (Name, Location, Distance)
        self.mission.mission_2()  # Calc plane formation position
        # Loop
        while not self.mission.mission_ended:
            self.mission.mission_3()  # Move the plane
            self.mission.mission_4()  # Calc the current weather
            self.mission.mission_5()  # Calculate stress to plane
            self.mission.mission_6()  # Spawn enemies
            self.mission.mission_7()  # Actions / Target enemies
            self.mission.mission_8()  # Enemies target
            self.mission.mission_9()  # Flak target
            self.mission.mission_10()  # Calculate damge to plane
            self.mission.mission_11()  # After round cleanup


# Start the game
# Game()
