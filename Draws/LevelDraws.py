from LevelParts.Level import *
from Const.Level import *
from LevelParts.Map import *
from pygame.draw import *


def map_draw(level_map: Map, screen):
    """

    Draw map
    :param level_map: Object of class Map
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, WHT, (level_map.x, level_map.y, level_map.width, level_map.height))
    for i in level_map.Left_Roads:
        for j in i:
            circle(screen, BLC, j, 50)
    for i in level_map.Right_Roads:
        for j in i:
            circle(screen, BLC, j, 50)
    for i in level_map.Left_Roads:
        for j in i:
            circle(screen, WHT, j, 40)
    for i in level_map.Right_Roads:
        for j in i:
            circle(screen, WHT, j, 40)
    polygon(screen, BLC, level_map.Pole_Points)


def level_draw(level, screen):
    """

    Draw level: all without all objects (in this function you don't need to draw map, city and another objects)
    :param level: Object of class Level, that we will draw
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, BLC, (0, 0, LevelXSize, LevelXSize))


if __name__ == "__main__":
    print("This module is not for direct call!")
