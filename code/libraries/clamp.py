'''
Create clamp tool
'''

def clamp(value, min_num, max_num):
	''' Clamp the dice roll to the min/max possible '''
	return max(min(max_num, value), min_num)
