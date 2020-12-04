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


def city_draw(city, side, screen, image_bruschatka):
    """

    Function, which draw the order city. Have to draw two variants: left side and right side
    :param image_bruschatka: Image of cobblestone
    :param city: Object city, which we want to draw
    :param side: A string that tells which side the given city is located on.
                      If side=="order", than this is order city
                      If side=="union", than this is union city
    :param screen: Surface, where the picture is rendered

    """


    if side == "order":
        image_bruschatka = transform.scale(image_bruschatka,
                                           (massive_multiply((CityXSize, CityYSize), DrawingCoefficient)))
        screen.blit(image_bruschatka, massive_multiply((city.x, city.y), DrawingCoefficient))
        health_bar(
            massive_multiply((city.x + CityXSize / 6, city.y + CityYSize / 10, 2 * CityXSize / 3, CityYSize / 20),
                             DrawingCoefficient),
            city.life, CityLife, screen)
    else:
        image_bruschatka = transform.scale(image_bruschatka,
                                           (massive_multiply((CityXSize, CityYSize), DrawingCoefficient)))

        screen.blit(image_bruschatka, massive_multiply((city.x, city.y), DrawingCoefficient))
        health_bar(
            massive_multiply((city.x + CityXSize / 6, city.y + CityYSize / 10, 2 * CityXSize / 3, CityYSize / 20),
                             DrawingCoefficient),
            city.life, CityLife, screen)


def city_centre_draw(city_centre, side, screen, image_castle ,image_square):
    """

    Function, which draw the order city centre. Have to draw two variants: left side and right side
    :param image_square: Image of city square
    :param image_castle: Image of city castle
    :param side: A string that tells which side the given city centre is located on.
                      If side=="order", than this is order city centre
                      If side=="union", than this is union city centre
    :param city_centre: Object city centre, which we want to draw
    :param screen: Surface, where the picture is rendered

    """
    if side == "order":
        image_castle = transform.scale(image_castle,
                                             (massive_multiply((CityCentreXSize / 2, CityCentreYSize / 2),
                                                               DrawingCoefficient)))
        screen.blit(image_castle,
                    massive_multiply((city_centre.x + CityCentreXSize / 2, city_centre.y), DrawingCoefficient))

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
    else:
        image_castle = transform.scale(image_castle,
                                             (massive_multiply((CityCentreXSize / 2, CityCentreYSize / 2),
                                                               DrawingCoefficient)))
        screen.blit(image_castle, massive_multiply((city_centre.x, city_centre.y), DrawingCoefficient))
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


def mine_draw(mine, side, screen):
    """
    Function, which draw the mine
    :param mine: Object Mine, which we want to draw
    :param side: A string that tells which side the given mine is located on.
                      If side=="order", than this is order mine
                      If side=="union", than this is union mine
    :param screen: Surface, where the picture is rendered
    """

    if side == "order":
        rect(screen, RED, (mine.x, mine.y, MineXSize, MineYSize))
        health_bar(
            massive_multiply((mine.x + MineXSize / 6, mine.y + MineYSize / 10,
                              2 * MineXSize / 3, MineYSize / 20),
                             DrawingCoefficient),
            mine.life, MineLife, screen)
    else:
        rect(screen, YLW, (mine.x, mine.y, MineXSize, MineYSize))
        health_bar(
            massive_multiply((mine.x + MineXSize / 6, mine.y + MineYSize / 10,
                              2 * MineXSize / 3, MineYSize / 20),
                             DrawingCoefficient),
            mine.life, MineLife, screen)


def research_centre_draw(research_centre, side, screen):
    """
    Function, which draw the research centre
    :param research_centre: Object Research Centre, which we want to draw
    :param side: A string that tells which side the given research centre is located on.
                      If side=="order", than this is order research centre
                      If side=="union", than this is union research centre
    :param screen: Surface, where the picture is rendered
    """

    if side == "order":
        rect(screen, RED, (research_centre.x, research_centre.y, MineXSize, MineYSize))
        health_bar(
            massive_multiply((research_centre.x + ResearchCentreXSize / 6, research_centre.y + ResearchCentreYSize / 10,
                              2 * ResearchCentreXSize / 3, ResearchCentreYSize / 20),
                             DrawingCoefficient),
            research_centre.life, ResearchCentreLife, screen)
    else:
        rect(screen, YLW, (research_centre.x, research_centre.y, ResearchCentreXSize, ResearchCentreYSize))
        health_bar(
            massive_multiply((research_centre.x + ResearchCentreXSize / 6, research_centre.y + ResearchCentreYSize / 10,
                              2 * ResearchCentreXSize / 3, ResearchCentreYSize / 20),
                             DrawingCoefficient),
            research_centre.life, ResearchCentreLife, screen)



if __name__ == "__main__":
    print("This module is not for direct call!")
