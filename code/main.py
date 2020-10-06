'''
Bootstrap the game
'''
import os
from objects.game import Game

# Set the OS CWD to script location
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Start the game
Game()
