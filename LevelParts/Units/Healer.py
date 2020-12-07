from Draws.UnitDraws import unit_draw
from LevelParts.Units.UnitAI.UnitAI import *
from LevelParts.Units.Unit import *


class Healer(Unit):

    """

    Class of first unit Healer

    : method __init__(): Initialise Healer. Do the super()__init__()
                                   life = life of Healer unit
                                   unit_type = "healer"
                                   Receives side, coord
    : method update(screen, level): Redraw city. Defining the action of the Healer unit
    #: method reaction(level): Defining the action of the Healer unit
    : method interaction_with_unit(self, unit: Unit, number, action): Method, that process situation, when self interact
                                                                      with another unit. Healer can just heal
    : method interaction_with_district(self, unit: district, number, action): Method, that process situation, when self
                                                                              interact  with another unit. Cavalry can not attack.
    : method process_interaction(action):
    """

    def __init__(self, side, coord, image):
        super().__init__(side, HealerLife, coord, HealerType, image, HealerArmor,
                         HealerRange, HealerSpeed, HealerCooldown, HealerDamage,
                         HealerDamageSpread, HealerSideX, HealerSideY)

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
