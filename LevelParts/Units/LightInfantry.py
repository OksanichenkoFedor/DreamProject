from Draws.UnitDraws import lightinfantry_draw
from LevelParts.Units.UnitAI.UnitAI import *


class LightInfantry(Unit):

    """

    Class of first unit light infantry

    : method __init__(): Initialise Light infantry. Do the super()__init__()
                                   life = life of swordsman
                                   unit_type = "swordsman"
                                   Receives side, coord
    : method update(screen, level): Redraw city. Defining the action of the swordsman
    #: method reaction(level): Defining the action of the swordsman
    : method interaction_with_unit(self, unit: Unit, number, action): Method, that process situation, when self interact
                                                                      with another unit. Light Infantry can just attack
    : method interaction_with_district(self, unit: district, number, action): Method, that process situation, when self
                                                                              interact  with another unit. Light
                                                                              Infantry can just attack.
    : method process_interaction(action):
    """

    def __init__(self, side, coord, image):
        super().__init__(side, LightInfantryLife, coord, LightInfantryType, image)

    def update(self, screen, level):
        """

        :param screen: Surface, where the picture is rendered
        :param level: Level of the game

        """
        lightinfantry_draw(self, self.side, self.position(level), screen, self.image)
        info = Info(self, level)
        solution = unitAI(info)
        return self.reaction(solution, level)
