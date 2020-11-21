from Const.Level import *
from Const.City import *
from pygame.draw import *


# TODO Написать здесь функции, которые будут рисовать город

def order_city_draw(city, screen):
    """

    Function, which draw the left city
    :param city: Object city, which we want to draw
    :param screen:
    :return:
    """
    if city.coord_side == "left" :
        rect(screen, RED,
             (city.x, city.y, CityXSize, CityYSize))
    else :
        rect(screen, RED, (city.x, city.y, CityXSize, CityYSize))


def union_city_draw(city, screen):
    """

    Function, which draw the right city
    :param city:
    :param screen:
    :return:
    """
    pass
    if city.coord_side == "left":
        rect(screen, YLW,
             (city.x, city.y, CityXSize, CityYSize))
    else:
        rect(screen, YLW, (city.x, city.y, CityXSize, CityYSize))


def order_city_centre_draw(city_centre, screen):
    """
    Draw Order City Centre

    :param city_centre:
    :param screen:
    :return:
    """
    rect(screen, YLW,
         (city_centre.x, city_centre.y, CityCentreXSize, CityCentreYSize))

def union_city_centre_draw(city_centre, screen):
    rect(screen, RED,
         (city_centre.x, city_centre.y, CityCentreXSize, CityCentreYSize))

if __name__ == "__main__":
    print("This module is not for direct call!")
