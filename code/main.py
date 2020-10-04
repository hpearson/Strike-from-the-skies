'''
Bootstrap the game
'''
import os

import game

# Set the OS CWD to script location
os.chdir(os.path.dirname(os.path.realpath(__file__)))

GAME = game.Game()

# Step 0 Prep
# Step 1 Calc Weather
# Step 2 Move plane (landing, ground, water, air, bailout)
# Step 3 Spawn enemies
# Step 4 Shoot at enemies
# Step 5 Enemy dmg calc
# Step 6 Enemy shoot
# Step 7 Flak shoot
# Step 8 Calc plane dmg
# Step 9 reactions
# Repeat
