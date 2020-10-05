'''
Use this libarie to use tools
'''
import random


def can_target(seat, position, elevation):
    ''' Can this seat shoot this enemy location '''
    for _ in seat.targetable:
        if _.get('Position') == position and _.get('Elevation') == elevation:
            return True
    return False


def clamp(value, min_num, max_num):
    ''' Clamp the dice roll to the min/max possible '''
    return max(min(max_num, value), min_num)


def roll(min_num, max_num):
    ''' Roll a xdx '''
    return random.randint(min_num, max_num)


def roll_list(input_list):
    ''' Pull 1 from list '''
    return random.choice(input_list)


def alive_enemies(enemies):
    ''' Filter dead enemies and return the living '''
    alive_agressors = []
    for _ in enemies:
        if _.alive:
            alive_agressors.append(_)
    return alive_agressors
