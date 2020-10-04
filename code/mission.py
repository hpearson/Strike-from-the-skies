'''
Setup a class to hold the mission information
'''
from libraries.log import log
from libraries.dice import roll
from libraries.clamp import clamp

class Mission():
	''' Setup Mission Vars '''
	def __init__(self):
		''' Prep Init Values '''
		self.weather = None


		log('== Starting Mission Prep ==')
		# Calc the current weather
		self._gen_weather()
		# Calc target
		# Calc target distance
		# Calc target type
		log('== Ending Mission Prep ==')

	def _gen_weather(self):
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
			result = roll(0, 3)
			self.weather = weather_list[result]
			log(f'Takeoff weather condition is: {self.weather}')
