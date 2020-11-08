from Const.Level import *
from pygame.draw import *
# TODO Написать здесь функции, которые будут рисовать уровень игры


def map_draw(level_map, screen):
    # TODO Написать функцию отрисовки карты
    """

    Draw map
    :param level_map: Object of class Map
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, WHT, (LevelXSize/2 -MapXSize/2, LevelYSize/2 -MapYSize/2, MapXSize, MapYSize))


def level_draw(level, screen):
    # TODO Написать функцию отрисовки уровня
    """

    Draw map
    :param level: Object of class Level
    :param screen: Surface, where the picture is rendered

    """
    rect(screen,BLC, (0,0,LevelXSize,LevelXSize))


if __name__ == "__main__":
    print("This module is not for direct call!")
