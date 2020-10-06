'''
Bootstrap the game
'''
import os
import game

# Set the OS CWD to script location
os.chdir(os.path.dirname(os.path.realpath(__file__)))

GAME = game.Game()
