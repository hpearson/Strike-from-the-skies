'''
Setup a class to hold the plane information
'''
from libraries.log import log

class Plane():
	''' Setup Game Vars '''
	def __init__(self):
		''' Prep Init Values '''
		self.max_speed = 300
		self.cur_speed = 100
		log('== Starting Plane Prep ==')

		log('== Ending Plane Prep ==')
