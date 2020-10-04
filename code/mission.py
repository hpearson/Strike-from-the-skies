'''
Setup a class to hold the mission information
'''
from libraries.log import log
from libraries.dice import roll, roll_list
from libraries.clamp import clamp

import plane

class Mission():
	''' Setup Mission Vars '''
	def __init__(self):
		''' Prep Init Values '''
		self.plane = plane.Plane()

		self.weather = None
		self.target_name = None
		self.target_distance = None
		self.target_type = None
		self.distance_progress = 0
		self.heading_home = False
		self.formation_position = None
		self.squadron_position = None
		self.above_target = False
		self.mission_ended = False

		log('== Starting Mission Prep ==')
		log('== Ending Mission Prep ==')

	def m1(self):
		''' Calc the target '''
		target_list = []
		# Location Name, Distance, Type
		target_list.append({'Name': 'Berlin', 'Distance': 1000, 'Type': 'City'})
		# Load in more targets
		target = roll_list(target_list)
		self.target_name = target['Name']
		self.target_distance = target['Distance']
		self.target_type = target['Type']
		log(f'The target for today is: {self.target_name}')
		log(f'{self.target_name} is {self.target_distance} miles away')
		log(f'The bombing target is for: {self.target_type}')

	def m2(self):
		''' Calc the weather '''
		weather_num = None
		weather_list = ['Bad', 'Poor', 'Good', 'Great']
		if self.weather:
			# Calc weather changes
			result = roll(1, 3)
			weather_num = weather_list.index(self.weather)
			if result == 1:
				# Weather worstens
				weather_num -= 1
				self.weather = weather_list[clamp(weather_num, 0, 3)]
				log(f'The weather worsened into: {self.weather}')
			if result == 2:
				# Weather does not change
				log(f'No changes to the weather, still: {self.weather}')
			if result == 3:
				# Weather improves
				weather_num += 1
				self.weather = weather_list[clamp(weather_num, 0, 3)]
				log(f'The weather improved into: {self.weather}')

		if not self.weather:
			# Calc initial weather
			self.weather = roll_list(weather_list)
			log(f'Takeoff weather condition is: {self.weather}')

	def m3(self):
		''' Calc plane starting formation & postion '''
		position_list = ['Lead', 'Middle', 'Tail']
		self.formation_position = roll_list(position_list)
		log(f'The bomber is: {self.formation_position} position')

		squadron_list = ['High', 'Middle', 'Low']
		self.squadron_position = roll_list(squadron_list)
		log(f'The bomber is: {self.squadron_position} of the squadron')

	def m4(self):
		''' Calc movement for plane '''
		# TODO let player choose
		# TODO Ground
		# TODO Water
		# TODO Bailout
		# TODO Abort Mission
		# Move plane through air

		# Move plane closer to target
		self.distance_progress += self.plane.cur_speed
		self.above_target = False

		if self.distance_progress < self.target_distance:
			remaining = self.target_distance - self.distance_progress
			log(f'The plane is {remaining} miles away from {self.target_name}')

		if self.distance_progress > self.target_distance:
			log(f'The plane is over the target: {self.target_name}')
			if self.heading_home:
				self.mission_ended = True
				print('Plane landed on 8th Airforce Airfield')

			if not self.heading_home:
				log('The plane will trun around after the bombing run')
				# Turn the plane around
				self.heading_home = True
				self.above_target = True
				# Return home target
				self.target_name = '8th Airfoce'
				self.target_type = 'Airfield'
				# Calculate distance roll over
				self.distance_progress =  self.distance_progress - self.target_distance
				remaining = self.target_distance - self.distance_progress
				log(f'The plane is {remaining} miles away from {self.target_name}')
