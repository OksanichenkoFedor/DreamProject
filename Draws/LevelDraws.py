from LevelParts.Level import *
from Const.Level import *
from LevelParts.Map import *
from pygame.draw import *

# TODO Написать здесь функции, которые будут рисовать уровень игры


def map_draw(level_map: Map, screen):
    # TODO Написать функцию отрисовки карты
    """

    Draw map
    :param level_map: Object of class Map
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, WHT, (level_map.x, level_map.y, level_map.width, level_map.height))
    for i in level_map.Left_Roads:
        for j in i:
            circle(screen, BLC, j, 5)
    for i in level_map.Right_Roads:
        for j in i:
            circle(screen, BLC, j, 5)
    polygon(screen, BLC, level_map.Pole_Points)


def level_draw(level, screen):
    # TODO Написать функцию отрисовки уровня
    """

    Draw map
    :param level: Object of class Level
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, BLC, (0, 0, LevelXSize, LevelXSize))


def swordsman_draw(unit, level, screen):
    if(unit.side[0]=="order"):
        circle(screen, RED, (int(unit.coord[1] + level.map.x), int(unit.coord[2] + level.map.y)), 15)
    else:
        circle(screen, YLW, (int(unit.coord[1] + level.map.x), int(unit.coord[2] + level.map.y)), 15)



if __name__ == "__main__":
    print("This module is not for direct call!")
