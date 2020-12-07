from Draws.UnitDraws import unit_draw
from LevelParts.Units.UnitAI.UnitAI import *
from LevelParts.Units.Unit import *


class LongRangeInfantry(Unit):

    """

    Class of first unit cavalry

    : method __init__(): Initialise LongRangeInfantry. Do the super()__init__()
                                   life = life of LongRange unit
                                   unit_type = "long_range_unit"
                                   Receives side, coord
    : method update(screen, level): Redraw city. Defining the action of the long range unit
    #: method reaction(level): Defining the action of the long range unit
    : method interaction_with_unit(self, unit: Unit, number, action): Method, that process situation, when self interact
                                                                      with another unit. Long Range Infantry can just attack
    : method interaction_with_district(self, unit: district, number, action): Method, that process situation, when self
                                                                              interact  with another unit. Long Range Infantry can just attack.
    : method process_interaction(action):
    """

    def __init__(self, side, coord, image):
        super().__init__(side, LongRangeInfantryLife, coord, LongRangeInfantryType, image, LongRangeInfantryArmor,
                         LongRangeInfantryRange, LongRangeInfantrySpeed, LongRangeInfantryCooldown, LongRangeInfantryDamage,
                         LongRangeInfantryDamageSpread, LongRangeInfantrySideX, LongRangeInfantrySideY)

    def update(self, level):
        """

        :param level: Level of the game

        """
        if self.interact_timer > 0:
            self.interact_timer -= 1
        info = Info(self, level)
        solution = unitAI(info)
        return self.reaction(solution, level)

    def draw(self, screen, level):
        unit_draw(self, self.side, self.position(level), screen, self.image, self.XSize, self.YSize)
