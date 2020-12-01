from Const.Level import *
from Const.City import *
from pygame import *
from pygame.draw import *


def massive_multiply(j, a):
    j1 = []
    for i in range(len(j)):
        j1.append(int(j[i]*a))
    return j1


def health_bar(coord, life, full_life, screen):
    """
    Draw Health Bar
    :param x: First coordinate of left-up point of bar
    :param y: Second coordinate of left-up point of bar
    :param w: Width of bar
    :param h: Height of bar
    :param life: Life of object
    :param full_life: Full life of object
    :param screen: Surface, where the picture is rendered
    :return:
    """
    rect(screen,(int((255.0*(full_life-max(life,0)))/(full_life*1.0)), int((255.0*(max(life,0)))/(full_life*1.0)),0), (coord[0], coord[1], int((coord[2]*(max(life,0)))/(full_life*1.0)),coord[3]))
    rect(screen, BLC, coord, 1)


def order_city_draw(city, pole_side, screen ,image_bruschatka):
    """

    Function, which draw the order city. Have to draw two variants: left side and right side
    :param city: Object city, which we want to draw
    :param pole_side: A string that tells which side the given city is located on.
                      If side=="left", than this is city, located in the left side of the level
                      If side=="right", than this is city, located in the right side of the level
    :param screen: Surface, where the picture is rendered

    """


    #rect(screen, RED, massive_multiply((city.x, city.y, CityXSize, CityYSize), DrawingCoefficient))

    image_bruschatka = transform.scale(image_bruschatka,
                                       (massive_multiply((CityXSize, CityYSize), DrawingCoefficient)))
    screen.blit(image_bruschatka, massive_multiply((city.x, city.y), DrawingCoefficient))
    health_bar(
        massive_multiply((city.x + CityXSize / 6, city.y + CityYSize / 10, 2 * CityXSize / 3, CityYSize / 20),
                         DrawingCoefficient),
        city.life, CityLife, screen)


def union_city_draw(city, pole_side, screen,image_bruschatka):
    """

    Function, which draw the union city. Have to draw two variants: left side and right side
    :param city: Object city, which we want to draw
    :param pole_side: A string that tells which side the given city is located on.
                      If side=="left", than this is city, located in the left side of the level
                      If side=="right", than this is city, located in the right side of the level
    :param screen: Surface, where the picture is rendered

    """
    image_bruschatka = transform.scale(image_bruschatka,
                                       (massive_multiply((CityXSize, CityYSize), DrawingCoefficient)))

    screen.blit(image_bruschatka, massive_multiply((city.x, city.y), DrawingCoefficient))
    health_bar(
        massive_multiply((city.x + CityXSize / 6, city.y + CityYSize / 10, 2 * CityXSize / 3, CityYSize / 20),
                         DrawingCoefficient),
        city.life, CityLife, screen)


def order_city_centre_draw(city_centre, pole_side, screen, image_castle_orden ,image_square):
    """

    Function, which draw the order city centre. Have to draw two variants: left side and right side
    :param city_centre: Object city centre, which we want to draw
    :param pole_side: A string that tells which side the given city is located on.
                      If side=="left", than this is city, located in the left side of the level
                      If side=="right", than this is city, located in the right side of the level
    :param screen: Surface, where the picture is rendered

    """
    image_castle_orden = transform.scale(image_castle_orden,
                                       (massive_multiply((CityCentreXSize/2, CityCentreYSize/2), DrawingCoefficient)))
    screen.blit(image_castle_orden, massive_multiply((city_centre.x+CityCentreXSize/2, city_centre.y),DrawingCoefficient))

    image_square = transform.scale(image_square,
                                         (massive_multiply((CityCentreXSize / 2, CityCentreYSize / 2),
                                                           DrawingCoefficient)))
    screen.blit(image_square,
                massive_multiply((city_centre.x, city_centre.y + CityCentreYSize / 2),
                                 DrawingCoefficient))
    health_bar(
        massive_multiply((city_centre.x + CityCentreXSize / 6, city_centre.y + CityCentreYSize / 10, 2 * CityCentreXSize / 3, CityCentreYSize / 20),
                         DrawingCoefficient),
        city_centre.life, CityCentreLife, screen)



def union_city_centre_draw(city_centre, pole_side, screen,image_castle_union, image_square):
    """

    Function, which draw the order city centre. Have to draw two variants: left side and right side
    :param city_centre: Object city centre, which we want to draw
    :param pole_side: A string that tells which side the given city is located on.
                      If side=="left", than this is city, located in the left side of the level
                      If side=="right", than this is city, located in the right side of the level
    :param screen: Surface, where the picture is rendered

    """


    image_castle_union = transform.scale(image_castle_union,
                                         (massive_multiply((CityCentreXSize/2, CityCentreYSize/2), DrawingCoefficient)))
    screen.blit(image_castle_union, massive_multiply((city_centre.x, city_centre.y), DrawingCoefficient))
    image_square = transform.scale(image_square,
                                   (massive_multiply((CityCentreXSize / 2, CityCentreYSize / 2),
                                                     DrawingCoefficient)))
    screen.blit(image_square,
                massive_multiply((city_centre.x, city_centre.y + CityCentreYSize / 2),
                                 DrawingCoefficient))
    health_bar(
        massive_multiply((city_centre.x + CityCentreXSize / 6, city_centre.y + CityCentreYSize / 10,
                          2 * CityCentreXSize / 3, CityCentreYSize / 20),
                         DrawingCoefficient),
        city_centre.life, CityCentreLife, screen)



if __name__ == "__main__":
    print("This module is not for direct call!")
