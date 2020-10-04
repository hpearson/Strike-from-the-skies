'''
Setup a class to hold the game information
'''
from libraries.log import log

import mission
import plane

class Game():
	''' Setup Game Vars '''
	def __init__(self):
		log('== Starting Game Prep ==')
		# Start at mission zero
		self.mission = 0
		# Gen a new plane
		self.plane = plane.Plane()
		# Gen a new Mission
		self.mission = mission.Mission()
		log('== Ending Game Prep ==')
