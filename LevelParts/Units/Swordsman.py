from Draws.UnitDraws import swordsman_draw
from LevelParts.Units.UnitAI.UnitAI import *


class Swordsman(Unit):

    """

    Class of first unit swordsman

    : method __init__(): Initialise City Centre. Do the super()__init__()
                                   life = life of swordsman
                                   unit_type = "swordsman"
                                   Receives side, coord
    : method update(screen, level): Redraw city. Defining the action of the swordsman
    : method reaction(level): Defining the action of the swordsman

    """

    def __init__(self, side, coord):
        super().__init__(side, SwordsmanLife, coord, SwordsmanType)

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
                self.coord[1] += SwordsmanSpeed
            else:
                self.coord[1] -= SwordsmanSpeed
