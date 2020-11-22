

class Info:
    """

    Class, which contains information, which unitAI needs.

    : field unit: Gives the unit whose action needs to be defined
    : field friends: Massive of friendly units
    : field enemies: Massive of enemy units

    : method __init__(unit, level): Initialise Info. Put information to the Info. Receives side, life, x, y.

    """

    def __init__(self, unit, level):
        self.unit = unit
        self.friends = []
        self.enemies = []
        if level.first_city.side[0] == self.unit.side[0]:
            self.friends = level.first_city.Units
            self.enemies = level.second_city.Units
        else:
            self.friends = level.second_city.Units
            self.enemies = level.first_city.Units
