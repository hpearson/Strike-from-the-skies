'''
Setup a class to hold the crewmember information
'''


class Crew():
    ''' Setup Game Vars '''
    def __init__(self, seat):
        ''' Prep Init Values '''
        self.first_name = 'Hunter'
        self.last_name = 'Pearson'
        self.age = None
        self.training = seat
        self.targetable = []
        self.targeting = None

        # Where can this seat target
        self._assign_targetable()

    def _assign_targetable(self):
        ''' Defensive fire per seat '''
        if self.training == 'Bombardier':
            self.targetable.append({'Position': '12:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '12:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '12:00', 'Elevation': 'Low'})
        if self.training == 'Navigator':
            self.targetable.append({'Position': '1:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '1:30', 'Elevation': 'Level'})
            self.targetable.append({'Position': '1:30', 'Elevation': 'Low'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'Level'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'Low'})
        if self.training == 'Engineer':
            self.targetable.append({'Position': '12:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '12:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '1:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '6:00', 'Elevation': 'High'})
        if self.training == 'Radio':
            self.targetable.append({'Position': '6:00', 'Elevation': 'High'})
        if self.training == 'Ball':
            self.targetable.append({'Position': '1:30', 'Elevation': 'Low'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'Low'})
            self.targetable.append({'Position': '6:00', 'Elevation': 'Low'})
        if self.training == 'Port':
            self.targetable.append({'Position': '10:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'Low'})
        if self.training == 'Starboard':
            self.targetable.append({'Position': '1:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'Low'})
        if self.training == 'Tail':
            self.targetable.append({'Position': '6:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '6:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '6:00', 'Elevation': 'Low'})
