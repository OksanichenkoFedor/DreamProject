from Const.Units import LightInfantryType
from LevelParts.City.District import *
from LevelParts.Units.Unit import Unit
from LevelParts.Units.UnitAI.Info import Info
from Const.Level import *
from Const.Units import *
from Const.City import *
import math


def nearestUnit(info):

    if info.unit.coord[0] == "battle_pole":
        friendly_distance = LevelXSize**2 + LevelYSize**2
        enemy_distance = LevelXSize**2 + LevelYSize**2
        friendly_index = False
        enemy_index = False

        for friendly_unit in info.friends:
            if friendly_unit.coord[0] == "battle_pole":
                r = ((info.unit.coord[1]-friendly_unit.coord[1])**2 + (info.unit.coord[2]-friendly_unit.coord[2])**2)**0.5
                if r<friendly_distance:
                    friendly_distance = r
                    friendly_index = info.friends.index(friendly_unit)

        for enemy_unit in info.enemies:
            if enemy_unit.coord[0] == "battle_pole":
                r = ((info.unit.coord[1]-enemy_unit.coord[1])**2 + (info.unit.coord[2]-enemy_unit.coord[2])**2)**0.5
                if r<enemy_distance:
                    enemy_distance = r
                    enemy_index = info.enemies.index(enemy_unit)

        return ((friendly_distance, friendly_index), (enemy_distance, enemy_index))

    elif info.unit.coord[0] == "left":
        friendly_distance = LevelXSize ** 2 + LevelYSize ** 2
        enemy_distance = LevelXSize ** 2 + LevelYSize ** 2
        friendly_index = False
        enemy_index = False
        road_num = info.unit.coord[1]

        for friendly_unit in info.friends:
            if friendly_unit.coord[0] == "left":
                if friendly_unit.coord[1] == road_num:
                    r = abs(info.unit.coord[2] - friendly_unit.coord[2])
                    if r < friendly_distance:
                        friendly_distance = r
                        friendly_index = info.friends.index(friendly_unit)

        for enemy_unit in info.enemies:
            if enemy_unit.coord[0] == "left":
                if enemy_unit.coord[1] == road_num:
                    r = abs(info.unit.coord[2] - enemy_unit.coord[2])
                    if r < enemy_distance:
                        enemy_distance = r
                        enemy_index = info.enemies.index(enemy_unit)
        return ((friendly_distance, friendly_index), (enemy_distance, enemy_index))

    elif info.unit.coord[0] == "right":
        friendly_distance = LevelXSize ** 2 + LevelYSize ** 2
        enemy_distance = LevelXSize ** 2 + LevelYSize ** 2
        friendly_index = False
        enemy_index = False
        road_num = info.unit.coord[1]

        for friendly_unit in info.friends:
            if friendly_unit.coord[0] == "right":
                if friendly_unit.coord[1] == road_num:
                    r = abs(info.unit.coord[2] - friendly_unit.coord[2])
                    if r < friendly_distance:
                        friendly_distance = r
                        friendly_index = info.friends.index(friendly_unit)

        for enemy_unit in info.enemies:
            if enemy_unit.coord[0] == "right":
                if enemy_unit.coord[1] == road_num:
                    r = abs(info.unit.coord[2] - enemy_unit.coord[2])
                    if r < enemy_distance:
                        enemy_distance = r
                        enemy_index = info.enemies.index(enemy_unit)

        return ((friendly_distance, friendly_index), (enemy_distance, enemy_index))

def unitAI(info: Info):
    """

    Make decision for unit
    :param info: Object Info, which contains necessary information
    :return: Solution: Solution, which tell unit what to do. Massive:
                                                             1.) String, that say, what, we will do
                                                             2.) Parameters, dependent on what we would do


    """

    if info.unit.type == LightInfantryType:
        nearest_unit = nearestUnit(info)
        solution = []
        first = " "

        if info.unit.side[1] == "left":
            if (nearest_unit[1][0] != False) or (info.unit.coord[0] == "right" and info.unit.coord[2]==0):
                first = "interact"
            else:
                first = "move forward"
        elif info.unit.side[1] == "right":
            if (nearest_unit[1][0] != False) or (info.unit.coord[0] == "left" and info.unit.coord[2] == 0):
                first = "interact"
            else:
                first = "move forward"
    solution.append(first)
    if first == "interact":
        if nearest_unit[1][0] == False:
            # solution[1] = interactable
            # solution[2] = action
            solution.append(info.enemy_districts[CityCentreNumber])
            solution.append(("attacked", LightInfantryDamage))
        else:
            if info.unit.coord[0] == "battle_pole":
                if nearest_unit[1][0] < info.unit.range:
                    pass
                else:
                    solution[0] = "moving to unit"
                    sin = (info.enemies[nearest_unit[1][1]].coord[2] - info.unit.coord[2])/nearest_unit[1][0]
                    cos = (info.enemies[nearest_unit[1][1]].coord[1] - info.unit.coord[1])/nearest_unit[1][0]
                    solution.append(sin)
                    solution.append(cos)

            else:
                if info.unit.coord[0] == "left":
                    if nearest_unit[1][0] < info.unit.range/info.total_length_L[info.unit.coord[1]]:
                        solution.append(info.enemies[nearest_unit[1][1]])
                        solution.append(("attacked", LightInfantryDamage))
                    else:
                        solution[0] = "moving to unit"
                        if info.unit.coord[2] < info.enemies[nearest_unit[1][1]].coord[2]:
                            solution.append(-1)
                        else:
                            solution.append(1)

                elif info.unit.coord[0] == "right":
                    if nearest_unit[1][0] < info.unit.range / info.total_length_R[info.unit.coord[1]]:
                        solution.append(info.enemies[nearest_unit[1][1]])
                        solution.append(("attacked", LightInfantryDamage))
                    else:
                        solution[0] = "moving to unit"
                        if info.unit.coord[2] < info.enemies[nearest_unit[1][1]].coord[2]:
                            solution.append(-1)
                        else:
                            solution.append(1)



    return solution








