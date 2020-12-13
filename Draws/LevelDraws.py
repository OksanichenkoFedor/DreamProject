from LevelParts.Level import *
from Const.Level import *
from LevelParts.Map import *
from pygame.draw import *
from pygame.font import *
from math import atan, cos, tan, pi


def massive_multiply(j, a):
    j1 = []
    for i in range(len(j)):
        j1.append(int(j[i] * a))
    return j1


def Two_D_massive_multiply(j, a):
    j1 = []
    for i in range(len(j)):
        j1.append([])
        for k in range(len(j[i])):
            j1[i].append(int(j[i][k] * a))
    return j1


def map_draw(level_map: Map, screen):
    """

    Draw map
    :param level_map: Object of class Map
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, WHT,
         massive_multiply((level_map.x, level_map.y, level_map.width, level_map.height), DrawingCoefficient))
    for i in level_map.Left_Roads:
        for j in i:
            circle(screen, BLC, massive_multiply(j, DrawingCoefficient), int(20 * DrawingCoefficient))
    for i in level_map.Right_Roads:
        for j in i:
            circle(screen, BLC, massive_multiply(j, DrawingCoefficient), int(20 * DrawingCoefficient))
    polygon(screen, BLC, Two_D_massive_multiply(level_map.Pole_Points, DrawingCoefficient))


def level_draw(level, screen):
    """

    Draw level: all without all objects (in this function you don't need to draw map, city and another objects)
    :param level: Object of class Level, that we will draw
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, BLC, (0, 0, int(LevelXSize * DrawingCoefficient), int(LevelXSize * DrawingCoefficient)))


def button_draw(screen, button):
    """

    :param screen: Surface, where the picture is rendered
    :param button: Button, that we will draw
    :return:
    """

    # Вид кнопки. Переделать
    """for i in range(1, 10):
                            s = pygame.Surface((length + (i * 2), height + (i * 2)))
                            s.fill(color)
                            alpha = (255 / (i + 2))
                            if alpha <= 0:
                                alpha = 1
                            s.set_alpha(alpha)
                            pygame.draw.rect(s, color, (x - i, y - i, length + i, height + i), width)
                            surface.blit(s, (x - i, y - i))"""
    if button.chosen:
        color = button.chosen_color
    else:
        color = button.color
    rect(screen, color, massive_multiply((button.x, button.y, button.length, button.height), DrawingCoefficient), 0)
    rect(screen, (190, 190, 190),
         massive_multiply((button.x, button.y, button.length, button.height), DrawingCoefficient), 1)

    # Текст
    font_size = int(int(1.5 * button.length * DrawingCoefficient) // len(button.text))
    myFont = SysFont("Calibri", font_size)
    myText = myFont.render(button.text, 1, button.text_color)
    screen.blit(myText, massive_multiply((
        (button.x + button.length / 2) - myText.get_width() / 2,
        (button.y + button.height / 2) - myText.get_height() / 2), DrawingCoefficient))


def unit_button_draw(screen, button, alpha, number):
    """

        :param screen: Surface, where the picture is rendered
        :param button: Button, that we will draw
        :param alpha:
        :param number: Numer of units in queue
        :return:
        """

    # Вид кнопки. Переделать
    """for i in range(1, 10):
                            s = pygame.Surface((length + (i * 2), height + (i * 2)))
                            s.fill(color)
                            alpha = (255 / (i + 2))
                            if alpha <= 0:
                                alpha = 1
                            s.set_alpha(alpha)
                            pygame.draw.rect(s, color, (x - i, y - i, length + i, height + i), width)
                            surface.blit(s, (x - i, y - i))"""
    if button.chosen:
        number -= 1
        color = button.chosen_color
    else:
        color = button.color
    rect(screen, color, massive_multiply((button.x, button.y, button.length, button.height), DrawingCoefficient), 0)
    rect(screen, (190, 190, 190),
         massive_multiply((button.x, button.y, button.length, button.height), DrawingCoefficient), 1)

    if alpha>0:
        alpha = 2.0*pi - alpha
        alpha0 = atan((button.length * 1.0) / (button.height * 1.0))
        pol = []
        pol.append(massive_multiply((button.x + button.length / 2, button.y + button.height / 2), DrawingCoefficient))
        if alpha < alpha0:
            pol.append(
                massive_multiply((button.x + button.length * (1 - tan(alpha)) * 0.5, button.y), DrawingCoefficient))
            pol.append(massive_multiply((button.x, button.y), DrawingCoefficient))
            pol.append(massive_multiply((button.x, button.y + button.height), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length, button.y + button.height), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length, button.y), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length / 2, button.y), DrawingCoefficient))
        elif alpha < pi - alpha0:
            pol.append(
                massive_multiply((button.x, button.y + button.height / 2 + button.length * 0.5 * tan(alpha - pi / 2))
                                 , DrawingCoefficient))
            pol.append(massive_multiply((button.x, button.y + button.height), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length, button.y + button.height), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length, button.y), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length / 2, button.y), DrawingCoefficient))
        elif alpha < pi + alpha0:
            pol.append(massive_multiply((button.x + button.length / 2 + button.height * 0.5 * (alpha - 1.0 * pi),
                                         button.y + button.height), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length, button.y + button.height), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length, button.y), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length / 2, button.y), DrawingCoefficient))
        elif alpha < 2.0 * pi - alpha0:
            pol.append(massive_multiply((button.x + button.length, button.y + button.height / 2 -
                                         button.length * 0.5 * tan(alpha - 1.5 * pi)), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length, button.y), DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length / 2, button.y), DrawingCoefficient))
        else:
            pol.append(
                massive_multiply((button.x + button.length / 2 - button.height * 0.5 * tan(alpha - 2.0 * pi), button.y),
                                 DrawingCoefficient))
            pol.append(massive_multiply((button.x + button.length / 2, button.y), DrawingCoefficient))
        polygon(screen, GRY, pol)

    # Текст
    font_size = int(int(2.0 * button.length * DrawingCoefficient) // len(button.text))
    myFont = SysFont("Calibri", font_size)
    myText = myFont.render(button.text, 1, button.text_color)
    screen.blit(myText, massive_multiply((
        (button.x + button.length / 2) - myText.get_width() / 2,
        (button.y + button.height / 2) - myText.get_height() / 2), DrawingCoefficient))


    if number > 0:
        text = str(number)
        font_size = int(int(0.3 * button.length * DrawingCoefficient) // len(text))
        myFont = SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, button.text_color)
        screen.blit(myText, massive_multiply((
            (button.x + button.length) - myText.get_width() * 1.5,
            (button.y + button.height) - myText.get_height() * 1.0), DrawingCoefficient))


def button_pole_draw(screen, button_pole):
    """

    :param screen: Surface, where the picture is rendered
    :param button_pole: Button Pole, that we will draw
    :return:
    """
    rect(screen, BLU, massive_multiply((button_pole.x, button_pole.y, button_pole.width, button_pole.height),
                                       DrawingCoefficient))


if __name__ == "__main__":
    print("This module is not for direct call!")
