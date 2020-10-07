'''
Setup a class to hold the mission information
'''
from libs.log import Log
from libs.tools import clamp, can_target, roll, roll_list, roll_dict, alive_enemies, ready_to_shoot

from objects.plane import Plane
from objects.enemy import Enemy


class Mission():
    ''' Setup Mission Vars '''
    def __init__(self):
        ''' Prep Init Values '''
        self.plane = Plane()
        self.enemies = []

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

    def mission_1(self):
        ''' Calc the target '''
        target_list = []
        # Location Name, Distance, Type
        target_list.append({'Name': 'Berlin', 'Distance': 1000, 'Type': 'City'})
        # Load in more targets
        target = roll_list(target_list)
        self.target_name = target['Name']
        self.target_distance = target['Distance']
        self.target_type = target['Type']
        Log(f'The target for today is: {self.target_name}')
        Log(f'{self.target_name} is {self.target_distance} miles away')
        Log(f'The bombing target is for: {self.target_type}')

    def mission_2(self):
        ''' Calc plane starting formation & postion '''
        position_list = ['Lead', 'Middle', 'Tail']
        self.formation_position = roll_list(position_list)
        Log(f'The bomber is: {self.formation_position} position')

        squadron_list = ['High', 'Middle', 'Low']
        self.squadron_position = roll_list(squadron_list)
        Log(f'The bomber is: {self.squadron_position} of the squadron')

    def mission_3(self):
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
            Log(f'The plane is {remaining} miles away from {self.target_name}')

        if self.distance_progress > self.target_distance:
            Log(f'The plane is over the target: {self.target_name}')
            if self.heading_home:
                self.mission_ended = True
                Log('Plane landed on 8th Airforce Airfield')

            if not self.heading_home:
                Log('The plane will trun around after the bombing run')
                # Turn the plane around
                self.heading_home = True
                self.above_target = True
                # Return home target
                self.target_name = '8th Airfoce'
                self.target_type = 'Airfield'
                # Calculate distance roll over
                self.distance_progress = self.distance_progress - self.target_distance
                remaining = self.target_distance - self.distance_progress
                Log(f'The plane is {remaining} miles away from {self.target_name}')

    def mission_4(self):
        ''' Calc the weather '''
        weather_num = None
        weather_list = ['Bad', 'Poor', 'Good', 'Great']
        if self.weather:
            # Calc weather changes
            result = roll(1, 2)
            weather_num = weather_list.index(self.weather)
            if result == 1:
                # Weather worstens
                weather_num -= 1
                self.weather = weather_list[clamp(weather_num, 0, 3)]
                Log(f'The weather changed into: {self.weather}')
            if result == 2:
                # Weather improves
                weather_num += 1
                self.weather = weather_list[clamp(weather_num, 0, 3)]
                Log(f'The weather changed into: {self.weather}')

        if not self.weather:
            # Calc initial weather
            self.weather = roll_list(weather_list)
            Log(f'Takeoff weather condition is: {self.weather}')

    def mission_5(self):
        ''' Calculate stress to the plane '''
        for section in self.plane.sections:
            if self.plane.sections[section] < 5:
                self.plane.sections[section] -= 1
                Log(f'{section} took stess damage')

    def mission_6(self):
        ''' Used to spawn enemies '''
        # Spawn new enemy
        result = roll(1, 3)
        for _ in range(result):
            aggressor = Enemy()
            self.enemies.append(aggressor)

        # Display all enemies in the area
        for aggressor in alive_enemies(self.enemies):
            Log(f'{aggressor.type} comes into view {aggressor.position} o\'clock {aggressor.elevation}')

    def mission_7(self):
        ''' Used to shoot at the enemies '''
        # Assign Targets
        for _ in alive_enemies(self.enemies):
            for turret in ready_to_shoot(self.plane.positions):
                if can_target(self.plane.positions.get(turret), _.position, _.elevation):
                    self.plane.positions[turret].crew_member.targeting = _
                    Log(f'{turret} is targeting: {_.type} {_.position} o\'clock {_.elevation}')

        # Shoot at Targets
        for turret in ready_to_shoot(self.plane.positions):
            if self.plane.positions[turret].crew_member.targeting:
                Log(f'{turret} is shooting: {self.plane.positions[turret].crew_member.targeting.type}')
                result = roll(1, 2)
                if result == 2:
                    self.plane.positions[turret].crew_member.targeting.alive = False
                    Log(f'{turret} shot down: {self.plane.positions[turret].crew_member.targeting.type}')
                if result == 1:
                    Log(f'{turret}: Missed')

    def mission_8(self):
        ''' Enemies shoot at plane '''
        agressors = alive_enemies(self.enemies)
        for agressor in agressors:
            result = roll(1, 2)
            if result == 2:
                Log(f'{agressor.type} attacks and hits!')
            if result == 1:
                Log(f'{agressor.type} attacks and misses!')

    def mission_9(self):
        ''' Calculate flak shots '''
        result = roll(1, 2)
        if result == 2:
            Log('Flak hits!')
        if result == 1:
            Log('Flak misses!')

    def mission_10(self):
        ''' Calculate damage to the plane '''
        hits = 5
        for _ in range(hits):
            section = roll_dict(self.plane.sections)
            Log(f'{section} was damaged')
            self.plane.sections[section] -= 1

    def mission_11(self):
        ''' After round cleanup '''
        # Remove crew targets
        for position in self.plane.positions:
            if self.plane.positions[position].crew_member:
                self.plane.positions[position].crew_member.targeting = False
