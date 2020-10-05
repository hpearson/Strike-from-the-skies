'''
Setup a class to hold the plane information
'''

import crew

class Plane():
	''' Setup Game Vars '''
	def __init__(self):
		''' Prep Init Values '''
		self.max_speed = 300
		self.cur_speed = 100
		self.seats = {
			'Bombardier' : crew.Crew('Bombardier'),
			'Navigator' : crew.Crew('Navigator'),
			'Pilot' : crew.Crew('Pilot'),
			'CoPilot' : crew.Crew('CoPilot'),
			'Engineer' : crew.Crew('Engineer'),
			'Radio' : crew.Crew('Radio'),
			'Ball' : crew.Crew('Ball'),
			'Port' : crew.Crew('Port'),
			'Starboard' : crew.Crew('Starboard'),
			'Tail' : crew.Crew('Tail')
		}
