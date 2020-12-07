from pygame.font import SysFont

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


def tech_bar(coord, tech, full_tech, screen):
    """
    Draw Health Bar
    :param coord: Massive of x, y, w, h
    :param tech: Life of object
    :param full_tech: Full tech of city, to go on next step
    :param screen: Surface, where the picture is rendered
    :return:
    """
    rect(screen, LBL, (coord[0], coord[1], int((coord[2]*(max(tech, 0)))/(full_tech*1.0)), coord[3]))
    rect(screen, BLC, coord, 1)


def master_draw(x,y, screen):
    """

    :param x: First coordinate of master
    :param y: Second coordinate of master
    :param screen: Surface, where the picture is rendered
    :return:
    """
    circle(screen, YLW, massive_multiply((x,y),DrawingCoefficient),int(10*DrawingCoefficient))


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
        tech_bar(
            massive_multiply((city.x + CityXSize / 6, city.y + CityYSize / 30, 2 * CityXSize / 3, CityYSize / 20),
                             DrawingCoefficient),
            city.tech_points, (city.tech_level + 1) * EachTechPoints, screen)
        font_size = int((CityXSize * DrawingCoefficient) / 6.0)
        myFont = SysFont("Money: "+str(int(city.money)), font_size)
        myText = myFont.render("Money: "+str(int(city.money)), 1, YLW)
        screen.blit(myText, massive_multiply((
            (city.x + CityXSize / 2) - myText.get_width() / 2,
            (city.y + CityYSize*(13.0/15.0)) - myText.get_height() / 2), DrawingCoefficient))
        font_size = int((CityXSize * DrawingCoefficient) / 6.0)
        myFont = SysFont("Tech Level: " + str(int(city.tech_level)), font_size)
        myText = myFont.render("Tech Level: " + str(int(city.tech_level)), 1, LBL)
        screen.blit(myText, massive_multiply((
            (city.x + CityXSize / 2) - myText.get_width() / 2,
            (city.y + CityYSize * (14.0 / 15.0)) - myText.get_height() / 2), DrawingCoefficient))
    else:
        image_bruschatka = transform.scale(image_bruschatka,
                                           (massive_multiply((CityXSize, CityYSize), DrawingCoefficient)))

        screen.blit(image_bruschatka, massive_multiply((city.x, city.y), DrawingCoefficient))
        health_bar(
            massive_multiply((city.x + CityXSize / 6, city.y + CityYSize / 10, 2 * CityXSize / 3, CityYSize / 20),
                             DrawingCoefficient),
            city.life, CityLife, screen)
        tech_bar(
            massive_multiply((city.x + CityXSize / 6, city.y + CityYSize / 30, 2 * CityXSize / 3, CityYSize / 20),
                             DrawingCoefficient),
            city.tech_points, (city.tech_level + 1) * EachTechPoints, screen)
        font_size = int((CityXSize * DrawingCoefficient) / 6.0)
        myFont = SysFont("Money: " + str(int(city.money)), font_size)
        myText = myFont.render("Money: " + str(int(city.money)), 1, YLW)
        screen.blit(myText, massive_multiply((
            (city.x + CityXSize / 2) - myText.get_width() / 2,
            (city.y + CityYSize * (13.0 / 15.0)) - myText.get_height() / 2), DrawingCoefficient))
        font_size = int((CityXSize * DrawingCoefficient) / 6.0)
        myFont = SysFont("Tech Level: " + str(int(city.tech_level)), font_size)
        myText = myFont.render("Tech Level: " + str(int(city.tech_level)), 1, LBL)
        screen.blit(myText, massive_multiply((
            (city.x + CityXSize / 2) - myText.get_width() / 2,
            (city.y + CityYSize * (14.0 / 15.0)) - myText.get_height() / 2), DrawingCoefficient))


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
        if city_centre.master>0:
            master_draw(city_centre.x + 7.0*CityCentreXSize / 6, city_centre.y + CityCentreYSize / 2, screen)

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
        if city_centre.master>0:
            master_draw(city_centre.x - (1.0*CityCentreXSize) / 6, city_centre.y + CityCentreYSize / 2, screen)


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
        rect(screen, RED, massive_multiply((mine.x, mine.y, MineXSize, MineYSize),DrawingCoefficient))
        health_bar(
            massive_multiply((mine.x + MineXSize / 6, mine.y + MineYSize / 10,
                              2 * MineXSize / 3, MineYSize / 20),
                             DrawingCoefficient),
            mine.life, MineLife, screen)
        if mine.master>0:
            master_draw(mine.x + 7.0*CityCentreXSize / 6, mine.y + CityCentreYSize / 2, screen)
    else:
        rect(screen, YLW, massive_multiply((mine.x, mine.y, MineXSize, MineYSize),DrawingCoefficient))
        health_bar(
            massive_multiply((mine.x + MineXSize / 6, mine.y + MineYSize / 10,
                              2 * MineXSize / 3, MineYSize / 20),
                             DrawingCoefficient),
            mine.life, MineLife, screen)
        if mine.master>0:
            master_draw(mine.x - (1.0*MineXSize) / 6, mine.y + MineYSize / 2, screen)


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
        rect(screen, RED, massive_multiply((research_centre.x, research_centre.y, ResearchCentreXSize,
                                            ResearchCentreYSize), DrawingCoefficient))
        health_bar(
            massive_multiply((research_centre.x + ResearchCentreXSize / 6, research_centre.y + ResearchCentreYSize / 10,
                              2 * ResearchCentreXSize / 3, ResearchCentreYSize / 20),
                             DrawingCoefficient),
            research_centre.life, ResearchCentreLife, screen)
        if research_centre.master>0:
            master_draw(research_centre.x + 7.0*ResearchCentreXSize / 6, research_centre.y + ResearchCentreYSize / 2, screen)
    else:
        rect(screen, YLW, massive_multiply((research_centre.x, research_centre.y, ResearchCentreXSize,
                                            ResearchCentreYSize), DrawingCoefficient))
        health_bar(
            massive_multiply((research_centre.x + ResearchCentreXSize / 6, research_centre.y + ResearchCentreYSize / 10,
                              2 * ResearchCentreXSize / 3, ResearchCentreYSize / 20),
                             DrawingCoefficient),
            research_centre.life, ResearchCentreLife, screen)
        if research_centre.master>0:
            master_draw(research_centre.x - (1.0*ResearchCentreXSize) / 6, research_centre.y + ResearchCentreYSize / 2, screen)



if __name__ == "__main__":
    print("This module is not for direct call!")
