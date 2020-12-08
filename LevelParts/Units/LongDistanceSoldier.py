from Draws.UnitDraws import unit_draw
from LevelParts.Units.UnitAI.UnitAI import *
from LevelParts.Units.Unit import *


class LongDistanceSoldier(Unit):

    """

    Class of first unit LongDistanceSoldier

    : method __init__(): Initialise LongDistanceSoldier. Do the super()__init__()
                                   life = life of LongRange unit
                                   unit_type = "long_distance_unit"
                                   Receives side, coord
    : method update(screen, level): Redraw city. Defining the action of the Long Distance Soldier
    #: method reaction(level): Defining the action of the Long Distance Soldier
    : method interaction_with_unit(self, unit: Unit, number, action): Method, that process situation, when self interact
                                                                      with another unit. Long Distance Soldier can just attack
    : method interaction_with_district(self, unit: district, number, action): Method, that process situation, when self
                                                                              interact  with another unit. Long Distance Soldier can just attack.
    : method process_interaction(action):
    """

    def __init__(self, side, coord, image):
        super().__init__(side, LongDistanceSoldierLife, coord, LongDistanceSoldierType, image, LongDistanceSoldierArmor,
                         LongDistanceSoldierRange, LongDistanceSoldierSpeed, LongDistanceSoldierCooldown, LongDistanceSoldierDamage,
                         LongDistanceSoldierDamageSpread, LongDistanceSoldierSideX, LongDistanceSoldierSideY)

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
