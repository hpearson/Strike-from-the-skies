'''
Bootstrap the game
'''
import os
import game
from libs.log import Log

# Set the OS CWD to script location
os.chdir(os.path.dirname(os.path.realpath(__file__)))

GAME = game.Game()
