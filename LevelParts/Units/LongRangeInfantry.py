from Draws.UnitDraws import unit_draw
from LevelParts.Units.UnitAI.UnitAI import *
from LevelParts.Units.Unit import *


class Cavalry(Unit):

    """

    Class of first unit cavalry

    : method __init__(): Initialise Cavalry. Do the super()__init__()
                                   life = life of cavalry unit
                                   unit_type = "cavalry"
                                   Receives side, coord
    : method update(screen, level): Redraw city. Defining the action of the cavalry unit
    #: method reaction(level): Defining the action of the cavalry unit
    : method interaction_with_unit(self, unit: Unit, number, action): Method, that process situation, when self interact
                                                                      with another unit. Cavalry can just attack
    : method interaction_with_district(self, unit: district, number, action): Method, that process situation, when self
                                                                              interact  with another unit. Cavalry can just attack.
    : method process_interaction(action):
    """

    def __init__(self, side, coord, image):
        super().__init__(side, CavalryLife, coord, CavalryType, image, CavalryArmor,
                         CavalryRange, CavalrySpeed, CavalryCooldown, CavalryDamage,
                         CavalryDamageSpread, CavalrySideX, CavalrySideY)

    def update(self, screen, level):
        """

        :param screen: Surface, where the picture is rendered
        :param level: Level of the game

        """
        if self.interact_timer > 0:
            self.interact_timer -= 1
        unit_draw(self, self.side, self.position(level), screen, self.image, self.XSize, self.YSize)
        info = Info(self, level)
        solution = unitAI(info)
        return self.reaction(solution, level)
