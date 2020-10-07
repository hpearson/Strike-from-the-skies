'''
Setup a class to hold the crewmember information
'''


class Crew():
    ''' Setup Game Vars '''
    def __init__(self, training):
        ''' Prep Init Values '''
        self.first_name = 'Hunter'
        self.last_name = 'Pearson'
        self.age = None
        self.training = training
        self.targetable = []
        self.targeting = None
        self.alive = True
