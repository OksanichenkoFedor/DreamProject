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
        if info.unit.side[1] == "left":
            if info.unit.coord[1] >= MapXSize:
                solution.append("attack")
                # solution[1] = district
                # solution[2] = action
                solution.append(info.enemy_districts[CityCentreNumber])
                solution.append(("attacked", LightInfantryDamage))
            else:
                solution.append("move forward")
        else:
            if info.unit.coord[1] <= 0:
                solution.append("attack")
                # solution[1] = district
                # solution[2] = action
                solution.append(info.enemy_districts[CityCentreNumber])
                solution.append(("attacked", LightInfantryDamage))
            else:
                solution.append("move forward")
    return solution


