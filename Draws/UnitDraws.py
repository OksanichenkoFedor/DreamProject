from Const.Level import *
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
    rect(screen, (int((255.0*(full_life-max(life, 0)))/(full_life*1.0)), int((255.0*(max(life,0)))/(full_life*1.0)),0), (coord[0], coord[1], int((coord[2]*(max(life,0)))/(full_life*1.0)),coord[3]))
    rect(screen, BLC, coord, 1)


def unit_draw(unit, unit_side, unit_position, screen, image_unit, XSize, YSize):
    """

    :param unit: Object Swordsman (we use class unit to avoid circle import)
    :param unit_side: Massive, that contains information, which is important for drawing
                      unit_side[0]: String, which say, what type of unit we have: "Order" , "Union"
                      unit_side[1]: A string that tells which side the given city is located on.
                          If side=="left", than this is city, located in the left side of the level
                          If side=="right", than this is city, located in the right side of the level
    :param unit_position: Massive, which contains:
                                             a.) First coordinate of swordsman in level screen
                                             b.) Second coordinate of swordsman in level screen
    :param screen: Surface, where the picture is rendered

    """
    position = []
    position.append(unit_position[0] - XSize/2)
    position.append(unit_position[1] - YSize/2)
    health_bar(massive_multiply((position[0], position[1], XSize, YSize/10), DrawingCoefficient), unit.life,
               unit.full_life, screen)
    image_unit = transform.scale(image_unit,
                                        (massive_multiply((XSize, YSize),
                                                          DrawingCoefficient)))
    screen.blit(image_unit, massive_multiply(position, DrawingCoefficient))
    if unit_side[0] == "order":
        if unit_side[1] == "left":
            pass
        else:
            pass
    else:
        if unit_side[1] == "left":
            pass
        else:
            pass


if __name__ == "__main__":
    print("This module is not for direct call!")
