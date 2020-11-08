from Const.Level import *
from Const.City import *
from pygame.draw import *


# TODO Написать здесь функции, которые будут рисовать город

def left_city_draw(city, screen):
    """

    Function, which draw the left city
    :param city:
    :param screen:
    :return:
    """
    rect(screen, YLW, (LevelXSize / 2 - MapXSize / 2 - CityXSize, LevelYSize / 2 - CityYSize / 2, CityXSize, CityYSize))


def right_city_draw(city, screen):
    """

    Function, which draw the right city
    :param city:
    :param screen:
    :return:
    """
    pass
    rect(screen, YLW, (LevelXSize / 2 + MapXSize / 2, LevelYSize / 2 - CityYSize / 2, CityXSize, CityYSize))


if __name__ == "__main__":
    print("This module is not for direct call!")
