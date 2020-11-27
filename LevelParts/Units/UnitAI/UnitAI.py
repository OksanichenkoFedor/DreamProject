from Const.Units import LightInfantryType
from LevelParts.City.District import *
from LevelParts.Units.Unit import Unit
from LevelParts.Units.UnitAI.Info import Info
from Const.Level import *
from Const.Units import *
from Const.City import *


def unitAI(info: Info):
    """

    Make decision for unit
    :param info: Object Info, which contains necessary information
    :return: Solution: Solution, which tell unit what to do. Massive:
                                                             1.) String, that say, what, we will do
                                                             2.) Parameters, dependent on what we would do


    """
    #print(info.enemy_districts[CityCentreNumber].life)
    if info.unit.type == LightInfantryType:
        solution = []
        first = " "
        if info.unit.side[1] == "left":
            if info.unit.coord[1] >= MapXSize:
                first = "interact"
            else:
                first = "move forward"
        else:
            if info.unit.coord[1] <= 0:
                first = "interact"

            else:
                first = "move forward"
    solution.append(first)
    if first == "interact":
        # solution[1] = interactable
        # solution[2] = action
        solution.append(info.enemy_districts[CityCentreNumber])
        solution.append(("attacked", LightInfantryDamage))
    return solution


