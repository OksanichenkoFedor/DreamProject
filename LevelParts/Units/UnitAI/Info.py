

class Info:
    """

    Class, which contains information, which unitAI needs.

    : field self.unit: Gives the unit whose action needs to be defined
    : field self.friends: Massive of friendly units
    : field self.enemies: Massive of enemy units
    : field self.friendly_districts: Massive of friendly districts
    : field self.enemy_districts: Massive of enemy districts

    : method __init__(unit, level): Initialise Info. Put information to the Info. Receives side, life, x, y.

    """

    def __init__(self, unit, level):
        self.unit = unit
        self.friends = []
        self.enemies = []
        self.friendly_districts = []
        self.enemy_districts = []
        if level.first_city.side[0] == self.unit.side[0]:
            self.friends = level.first_city.Units
            self.enemies = level.second_city.Units
            self.friendly_districts = level.first_city.Districts
            self.enemy_districts = level.second_city.Districts
        else:
            self.friends = level.second_city.Units
            self.enemies = level.first_city.Units
            self.friendly_districts = level.second_city.Districts
            self.enemy_districts = level.first_city.Districts
