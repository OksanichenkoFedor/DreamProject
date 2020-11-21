from Draws.LevelDraws import swordsman_draw
from LevelParts.Units.UnitAI.UnitAI import *


class Swordsman(Unit):
    def __init__(self, side, coord):
        super().__init__(side, SwordsmanLife, coord, SwordsmanType)

    def update(self, screen, level):
        """

        :param screen:
        :param level:
        :return:
        """
        swordsman_draw(self, level, screen)
        self.reaction(level)

    def reaction(self, level):
        """

        :return:
        """
        info = Info(self,level)
        solution = unitAI(info)
        if solution == "move forward":
            if self.side[1] == "left":
                self.coord[1] += SwordsmanSpeed
            else:
                self.coord[1] -= SwordsmanSpeed
