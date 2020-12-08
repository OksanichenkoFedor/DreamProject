from Const.Level import *
from pygame import *


def massive_multiply(j, a):
    j1 = []
    for i in range(len(j)):
        j1.append(int(j[i]*a))
    return j1


def blood_puddle_draw(x, y, w, h, blood_image, screen):
    """

    Draw blood puddle image

    :param x: First coordinate of centre of blood puddle
    :param y: Second coordinate of centre of blood puddle
    :param w: Width of blood puddle
    :param h: Height of blood puddle
    :param blood_image: Image of blood puddle
    :param screen: Surface, where the picture is rendered

    """
    blood_image = transform.scale(blood_image,
                                 (massive_multiply((w, h),
                                                   DrawingCoefficient)))
    screen.blit(blood_image, massive_multiply((x-w/2, y-h/2), DrawingCoefficient))


def dead_unit_draw(x, y, w, h, unit_image, screen):
    """

        Draw blood puddle image

        :param x: First coordinate of centre of dead unit
        :param y: Second coordinate of centre of dead unit
        :param w: Width of dead unit
        :param h: Height of dead unit
        :param unit_image: Image of dead unit
        :param screen: Surface, where the picture is rendered

        """
    unit_image = transform.scale(unit_image,
                                  (massive_multiply((w, h),
                                                    DrawingCoefficient)))
    screen.blit(unit_image, massive_multiply((x - w / 2, y - h / 2), DrawingCoefficient))
