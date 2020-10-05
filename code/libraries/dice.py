'''
Use this libarie to roll dice
'''
import random


def roll(min_num, max_num):
    ''' Roll a xdx '''
    return random.randint(min_num, max_num)


def roll_list(input_list):
    ''' Pull 1 from list '''
    return random.choice(input_list)
