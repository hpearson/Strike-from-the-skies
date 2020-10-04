'''
Bootstrap the game
'''
import os
from libraries.log import log
from libraries.dice import roll

from objects import game

# Set the OS CWD to script location
os.chdir(os.path.dirname(os.path.realpath(__file__)))

log('== Starting Game ==')
roll(1, 6)

GAME = game.Game()
