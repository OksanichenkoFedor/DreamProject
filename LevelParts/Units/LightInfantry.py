from Draws.UnitDraws import swordsman_draw
from LevelParts.Units.UnitAI.UnitAI import *


class LightInfantry(Unit):

    """

    Class of first unit light infantry

    : method __init__(): Initialise Light infantry. Do the super()__init__()
                                   life = life of swordsman
                                   unit_type = "swordsman"
                                   Receives side, coord
    : method update(screen, level): Redraw city. Defining the action of the swordsman
    : method reaction(level): Defining the action of the swordsman

    """

    def __init__(self, side, coord):
        super().__init__(side, LightInfantryLife, coord, LightInfantryType)

    def update(self, screen, level):
        """

        :param screen: Surface, where the picture is rendered
        :param level: Level of the game

        """
        swordsman_draw(self, self.side, self.position(level), screen)
        self.reaction(level)

    def reaction(self, level):
        """

        :param level: Level of the game

        """
        info = Info(self,level)
        solution = unitAI(info)
        if solution == "move forward":
            if self.side[1] == "left":
                self.coord[1] += LightInfantrySpeed
            else:
                self.coord[1] -= LightInfantrySpeed
