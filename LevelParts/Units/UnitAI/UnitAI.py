from LevelParts.City.District import *
from LevelParts.Units.Unit import Unit
from LevelParts.Units.UnitAI.Info import Info
from Const.Level import *


def unitAI(info: Info):
    """

    Make decision for unit
    :param info: Information
    :return: Solution: what this unit will do
    """
    if info.unit.type == SwordsmanType:
        solution = ""
        if info.unit.side[1]=="left":
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

    :param unit:
    :return:
    """
    pass


def attack_district(dist: District):
    dist.under_attack(SwordsmanDamage)
