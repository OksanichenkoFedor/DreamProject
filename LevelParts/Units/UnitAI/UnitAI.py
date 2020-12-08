from LevelParts.Units.UnitAI.Info import Info
from Const.Level import *
from Const.Units import *
from Const.City import *
from random import randint


def nearestUnit(info):

    if info.unit.coord[0] == "battle_pole":
        friendly_distance = (LevelXSize**2 + LevelYSize**2)**0.5
        enemy_distance = (LevelXSize**2 + LevelYSize**2)*0.5
        friendly_index = 0.1
        enemy_index = 0.1

        for i in range(len(info.friends)):
            if info.friends[i].coord[0] == "battle_pole":
                r = ((info.unit.coord[1] - info.friends[i].coord[1]) ** 2 + (
                            info.unit.coord[2] - info.friends[i].coord[2]) ** 2) ** 0.5
                if r < friendly_distance:
                    friendly_distance = r
                    friendly_index = i

        for i in range(len(info.enemies)):
            if info.enemies[i].coord[0] == "battle_pole":
                r = ((info.unit.coord[1]-info.enemies[i].coord[1])**2 + (info.unit.coord[2]-info.enemies[i].coord[2])**2)**0.5
                if r < enemy_distance:
                    enemy_distance = r
                    enemy_index = i

        return friendly_distance, friendly_index, enemy_distance, enemy_index

    elif info.unit.coord[0] == "left":
        friendly_distance = LevelXSize ** 2 + LevelYSize ** 2
        enemy_distance = LevelXSize ** 2 + LevelYSize ** 2
        friendly_index = 0.1
        enemy_index = 0.1
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
        return friendly_distance, friendly_index, enemy_distance, enemy_index

    elif info.unit.coord[0] == "right":
        friendly_distance = LevelXSize ** 2 + LevelYSize ** 2
        enemy_distance = LevelXSize ** 2 + LevelYSize ** 2
        friendly_index = 0.1
        enemy_index = 0.1
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

        return friendly_distance, friendly_index, enemy_distance, enemy_index

def unitAI(info: Info):
    """

    Make decision for unit
    :param info: Object Info, which contains necessary information
    :return: Solution: Solution, which tell unit what to do. Massive:
                                                             1.) String, that say, what, we will do
                                                             2.) Parameters, dependent on what we would do


    """

    if info.unit.type == LightInfantryType or info.unit.type == HeavyInfantryType or info.unit.type == CavalryType or info.unit.type == LongDistanceSoldierType:
        friendly_distance, friendly_index, enemy_distance, enemy_index= nearestUnit(info)
        solution = []
        first = " "

        if info.unit.side[1] == "left":
            if (enemy_index != 0.1) or (info.unit.coord[0] == "right" and info.unit.coord[2]==0):
                first = "interact"
            else:
                first = "move forward"
        elif info.unit.side[1] == "right":
            if (enemy_index != 0.1) or (info.unit.coord[0] == "left" and info.unit.coord[2] == 0):
                first = "interact"
            else:
                first = "move forward"
        solution.append(first)
        if first == "interact":
            if enemy_index == 0.1:
                # solution[1] = interactable
                # solution[2] = action
                solution.append(info.enemy_districts[info.unit.coord[1]])
                solution.append(("attacked", info.unit.damage+randint(-info.unit.damage_spread, info.unit.damage_spread) ))
            else:
                if info.unit.coord[0] == "battle_pole":
                    if enemy_distance < info.unit.range:
                        solution.append(info.enemies[enemy_index])
                        solution.append(("attacked", info.unit.damage))
                    else:
                        solution[0] = "moving to unit"
                        rast = ((info.enemies[enemy_index].coord[2] - info.unit.coord[2])**2+(info.enemies[enemy_index].coord[1] - info.unit.coord[1])**2)**0.5
                        sin = (info.enemies[enemy_index].coord[2] - info.unit.coord[2])/rast #nearest_unit[1][0]
                        cos = (info.enemies[enemy_index].coord[1] - info.unit.coord[1])/rast #nearest_unit[1][0]
                        solution.append(cos)
                        solution.append(sin)

                else:
                    if info.unit.coord[0] == "left":
                        if enemy_distance < info.unit.range/info.total_length_L[info.unit.coord[1]]:
                            solution.append(info.enemies[enemy_index])
                            solution.append(["attacked", info.unit.damage+randint(-info.unit.damage_spread,info.unit.damage_spread)])
                        else:
                            solution[0] = "moving to unit"
                            if info.unit.coord[2] < info.enemies[enemy_index].coord[2]:
                                solution.append(1)
                            else:
                                solution.append(-1)

                    elif info.unit.coord[0] == "right":
                        if enemy_distance < info.unit.range / info.total_length_R[info.unit.coord[1]]:
                            solution.append(info.enemies[enemy_index])
                            solution.append(["attacked", info.unit.damage+randint(-info.unit.damage_spread,info.unit.damage_spread)])
                        else:
                            solution[0] = "moving to unit"
                            if info.unit.coord[2] < info.enemies[enemy_index].coord[2]:
                                solution.append(1)
                            else:
                                solution.append(-1)




    elif info.unit.type == HealerType:
        friendly_distance, friendly_index, enemy_distance, enemy_index= nearestUnit(info)
        solution = []
        first = " "

        if info.unit.side[1] == "left":
            if (friendly_index != 0.1):
                first = "interact"
            else:
                first = "move forward"
        elif info.unit.side[1] == "right":
            if (friendly_index != 0.1):
                first = "interact"
            else:
                first = "move forward"
        solution.append(first)
        if first == "interact":
            #if friendly_index != 0.1:
            if info.unit.coord[0] == "battle_pole":
                if friendly_distance < info.unit.range:
                    solution.append(info.friends[friendly_index])
                    solution.append(("healed", info.unit.damage))
                else:
                    solution[0] = "moving to unit"
                    rast = ((info.friends[friendly_index].coord[2] - info.unit.coord[2])**2+(info.friends[friendly_index].coord[1] - info.unit.coord[1])**2)**0.5
                    sin = (info.friends[friendly_index].coord[2] - info.unit.coord[2])/rast #nearest_unit[1][0]
                    cos = (info.friends[friendly_index].coord[1] - info.unit.coord[1])/rast #nearest_unit[1][0]
                    solution.append(cos)
                    solution.append(sin)

            else:
                if info.unit.coord[0] == "left":
                    if friendly_distance < info.unit.range/info.total_length_L[info.unit.coord[1]]:
                        solution.append(info.friends[friendly_index])
                        solution.append(["healed", info.unit.damage+randint(-info.unit.damage_spread,info.unit.damage_spread)])
                    else:
                        solution[0] = "moving to unit"
                        if info.unit.coord[2] < info.friends[friendly_index].coord[2]:
                            solution.append(1)
                        else:
                            solution.append(-1)

                elif info.unit.coord[0] == "right":
                    if friendly_distance < info.unit.range / info.total_length_R[info.unit.coord[1]]:
                        solution.append(info.friends[friendly_index])
                        solution.append(["healed", info.unit.damage+randint(-info.unit.damage_spread,info.unit.damage_spread)])
                    else:
                        solution[0] = "moving to unit"
                        if info.unit.coord[2] < info.friends[friendly_index].coord[2]:
                            solution.append(1)
                        else:
                            solution.append(-1)

    elif info.unit.type == AlchemistType:
        friendly_distance, friendly_index, enemy_distance, enemy_index = nearestUnit(info)
        solution = []
        first = " "

        if info.unit.side[1] == "left":
            if (friendly_index != 0.1):
                first = "interact"
            else:
                first = "move forward"
        elif info.unit.side[1] == "right":
            if (friendly_index != 0.1):
                first = "interact"
            else:
                first = "move forward"
        solution.append(first)
        if first == "interact":
            # if friendly_index != 0.1:
            if info.unit.coord[0] == "battle_pole":
                if friendly_distance < info.unit.range:
                    solution.append(info.friends[friendly_index])
                    solution.append(("increased", info.unit.damage))
                else:
                    solution[0] = "moving to unit"
                    rast = ((info.friends[friendly_index].coord[2] - info.unit.coord[2]) ** 2 + (
                                info.friends[friendly_index].coord[1] - info.unit.coord[1]) ** 2) ** 0.5
                    sin = (info.friends[friendly_index].coord[2] - info.unit.coord[2]) / rast  # nearest_unit[1][0]
                    cos = (info.friends[friendly_index].coord[1] - info.unit.coord[1]) / rast  # nearest_unit[1][0]
                    solution.append(cos)
                    solution.append(sin)

            else:
                if info.unit.coord[0] == "left":
                    if friendly_distance < info.unit.range / info.total_length_L[info.unit.coord[1]]:
                        solution.append(info.friends[friendly_index])
                        solution.append(
                            ["increased", info.unit.damage + randint(-info.unit.damage_spread, info.unit.damage_spread)])
                    else:
                        solution[0] = "moving to unit"
                        if info.unit.coord[2] < info.friends[friendly_index].coord[2]:
                            solution.append(1)
                        else:
                            solution.append(-1)

                elif info.unit.coord[0] == "right":
                    if friendly_distance < info.unit.range / info.total_length_R[info.unit.coord[1]]:
                        solution.append(info.friends[friendly_index])
                        solution.append(
                            ["increased", info.unit.damage + randint(-info.unit.damage_spread, info.unit.damage_spread)])
                    else:
                        solution[0] = "moving to unit"
                        if info.unit.coord[2] < info.friends[friendly_index].coord[2]:
                            solution.append(1)
                        else:
                            solution.append(-1)



    return solution


