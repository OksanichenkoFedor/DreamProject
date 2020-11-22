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
    :return: Solution: what this unit will do

    """
    if info.unit.type == LightInfantryType:
        solution = " "
        if info.unit.side[1] == "left":
            if info.unit.coord[1] >= MapXSize:
                pass
            else:
                solution = "move forward"
        else:
            if info.unit.coord[1] <= 0:
                pass
            else:
                solution = "move forward"
    return solution


def attack_unit(unit: Unit):
    #TODO написать атаку, (придумать как отсюда влиять на объекты)
    """

    Function, that realise attack on unit
    :param unit: Unit that will be attacked
    :return:
    """
    pass


def attack_district(dist: District):
    """
    Function, that realise attack on district
    :param dist: District that will be attacked
    :return:
    """
    pass
