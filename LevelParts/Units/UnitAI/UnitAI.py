from Const.Units import LightInfantryType
from LevelParts.City.District import *
from LevelParts.Units.Unit import Unit
from LevelParts.Units.UnitAI.Info import Info
from Const.Level import *
from Const.Units import *


def unitAI(info: Info):
    """

    Make decision for unit
    :param info: Object Info, which contains necessary information
    :return: Solution: Solution, which tell unit what to do. Massive:
                                                             1.) String, that say, what, we will do
                                                             2.) Parameters, dependent on what we would do


    """
    if info.unit.type == LightInfantryType:
        solution = []
        solution.append(" ")
        if info.unit.side[1] == "left":
            if info.unit.coord[1] >= MapXSize:
                solution[0] = "attack district"
            else:
                solution[0] = "move forward"
        else:
            if info.unit.coord[1] <= 0:
                solution[0] = "attack district"
            else:
                solution[0] = "move forward"
    return solution


