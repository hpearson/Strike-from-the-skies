'''
Setup a class to hold the plane position information
'''


class Position():
    ''' Setup turret Vars '''
    def __init__(self, location_name, crew_member=None):
        ''' Prep Init Values '''
        self.targetable = []
        self.ammo = 0
        self.twin_gun = False
        self.crew_member = crew_member

        # if location_name == 'Ventral Turret':
        #    self.targetable.append({'Position': '12:00', 'Elevation': 'High'})
        #    self.targetable.append({'Position': '12:00', 'Elevation': 'Level'})
        #    self.targetable.append({'Position': '12:00', 'Elevation': 'Low'})
        #    self.targetable.append({'Position': '1:30', 'Elevation': 'High'})
        #    self.targetable.append({'Position': '1:30', 'Elevation': 'Level'})
        #    self.targetable.append({'Position': '1:30', 'Elevation': 'Low'})
        #    self.targetable.append({'Position': '3:00', 'Elevation': 'High'})
        #    self.targetable.append({'Position': '3:00', 'Elevation': 'Level'})
        #    self.targetable.append({'Position': '3:00', 'Elevation': 'Low'})
        #    self.targetable.append({'Position': '9:00', 'Elevation': 'High'})
        #    self.targetable.append({'Position': '9:00', 'Elevation': 'Level'})
        #    self.targetable.append({'Position': '9:00', 'Elevation': 'Low'})
        #    self.targetable.append({'Position': '10:30', 'Elevation': 'High'})
        #    self.targetable.append({'Position': '10:30', 'Elevation': 'Level'})
        #    self.targetable.append({'Position': '10:30', 'Elevation': 'Low'})
        #    self.twin = True
        if location_name == 'Port Cheek':
            # self.targetable.append({'Position': '12:00', 'Elevation': 'High'})
            # self.targetable.append({'Position': '12:00', 'Elevation': 'Level'})
            # self.targetable.append({'Position': '12:00', 'Elevation': 'Low'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'Level'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'Low'})
        if location_name == 'Starboard Cheek':
            # self.targetable.append({'Position': '12:00', 'Elevation': 'High'})
            # self.targetable.append({'Position': '12:00', 'Elevation': 'Level'})
            # self.targetable.append({'Position': '12:00', 'Elevation': 'Low'})
            self.targetable.append({'Position': '1:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '1:30', 'Elevation': 'Level'})
            self.targetable.append({'Position': '1:30', 'Elevation': 'Low'})
        if location_name == 'Dorsal Turret':
            self.targetable.append({'Position': '12:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '12:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '1:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '1:30', 'Elevation': 'Level'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '6:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '6:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'Level'})
            self.twin = True
        if location_name == 'Dorsal':
            self.targetable.append({'Position': '6:00', 'Elevation': 'High'})
        if location_name == 'Ventral Ball Turret':
            self.targetable.append({'Position': '12:00', 'Elevation': 'Low'})
            self.targetable.append({'Position': '12:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '1:30', 'Elevation': 'Low'})
            self.targetable.append({'Position': '1:30', 'Elevation': 'Level'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'Low'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '6:00', 'Elevation': 'Low'})
            self.targetable.append({'Position': '6:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'Low'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'Low'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'Level'})
            self.twin = True
        if location_name == 'Port Waist':
            self.targetable.append({'Position': '9:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '9:00', 'Elevation': 'Low'})
            self.targetable.append({'Position': '10:30', 'Elevation': 'High'})
        if location_name == 'Starboard Waist':
            self.targetable.append({'Position': '1:30', 'Elevation': 'High'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '3:00', 'Elevation': 'Low'})
        if location_name == 'Tail Turret':
            self.targetable.append({'Position': '6:00', 'Elevation': 'High'})
            self.targetable.append({'Position': '6:00', 'Elevation': 'Level'})
            self.targetable.append({'Position': '6:00', 'Elevation': 'Low'})
            self.twin = True
