from Const.Level import *
from Const.City import *
from pygame.draw import *


def order_city_draw(city, pole_side, screen):
    """

    Function, which draw the order city. Have to draw two variants: left side and right side
    :param city: Object city, which we want to draw
    :param pole_side: A string that tells which side the given city is located on.
                      If side=="left", than this is city, located in the left side of the level
                      If side=="right", than this is city, located in the right side of the level
    :param screen: Surface, where the picture is rendered

    """

    if pole_side == "left":
        rect(screen, RED,
             (city.x, city.y, CityXSize, CityYSize))
    else :
        rect(screen, RED, (city.x, city.y, CityXSize, CityYSize))


def union_city_draw(city, pole_side, screen):
    """

    Function, which draw the union city. Have to draw two variants: left side and right side
    :param city: Object city, which we want to draw
    :param pole_side: A string that tells which side the given city is located on.
                      If side=="left", than this is city, located in the left side of the level
                      If side=="right", than this is city, located in the right side of the level
    :param screen: Surface, where the picture is rendered

    """

    if pole_side == "left":
        rect(screen, YLW,
             (city.x, city.y, CityXSize, CityYSize))
    else:
        rect(screen, YLW, (city.x, city.y, CityXSize, CityYSize))


def order_city_centre_draw(city_centre, pole_side, screen):
    """

    Function, which draw the order city centre. Have to draw two variants: left side and right side
    :param city_centre: Object city centre, which we want to draw
    :param pole_side: A string that tells which side the given city is located on.
                      If side=="left", than this is city, located in the left side of the level
                      If side=="right", than this is city, located in the right side of the level
    :param screen: Surface, where the picture is rendered

    """

    if pole_side == "left":
        rect(screen, YLW,
             (city_centre.x, city_centre.y, CityCentreXSize, CityCentreYSize))
    else :
        rect(screen, YLW,
             (city_centre.x, city_centre.y, CityCentreXSize, CityCentreYSize))


def union_city_centre_draw(city_centre, pole_side, screen):
    """

    Function, which draw the order city centre. Have to draw two variants: left side and right side
    :param city_centre: Object city centre, which we want to draw
    :param pole_side: A string that tells which side the given city is located on.
                      If side=="left", than this is city, located in the left side of the level
                      If side=="right", than this is city, located in the right side of the level
    :param screen: Surface, where the picture is rendered

    """

    if pole_side == "left":
        rect(screen, RED,
             (city_centre.x, city_centre.y, CityCentreXSize, CityCentreYSize))
    else :
        rect(screen, RED,
             (city_centre.x, city_centre.y, CityCentreXSize, CityCentreYSize))


if __name__ == "__main__":
    print("This module is not for direct call!")
