from LevelParts.Level import *
from Const.Level import *
from LevelParts.Map import *
from pygame.draw import *
from pygame.font import *
#from pygame import *


def massive_multiply(j, a):
    j1 = []
    for i in range(len(j)):
        j1.append(int(j[i]*a))
    return j1


def Two_D_massive_multiply(j, a):
    j1 = []
    for i in range(len(j)):
        j1.append([])
        for k in range(len(j[i])):
            j1[i].append(int(j[i][k]*a))
    return j1

def map_draw(level_map: Map, screen):
    """

    Draw map
    :param level_map: Object of class Map
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, WHT, massive_multiply((level_map.x, level_map.y, level_map.width, level_map.height),DrawingCoefficient))
    for i in level_map.Left_Roads:
        for j in i:
            circle(screen, BLC, massive_multiply(j,DrawingCoefficient), int(20*DrawingCoefficient))
    for i in level_map.Right_Roads:
        for j in i:
            circle(screen, BLC, massive_multiply(j,DrawingCoefficient), int(20*DrawingCoefficient))
    polygon(screen, BLC, Two_D_massive_multiply(level_map.Pole_Points,DrawingCoefficient))


def level_draw(level, screen):
    """

    Draw level: all without all objects (in this function you don't need to draw map, city and another objects)
    :param level: Object of class Level, that we will draw
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, BLU, (0, 0, int(LevelXSize*DrawingCoefficient), int(LevelXSize*DrawingCoefficient)))


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
    rect(screen, button.color, massive_multiply((button.x, button.y, button.length, button.height),DrawingCoefficient), 0)
    rect(screen, (190, 190, 190), massive_multiply((button.x, button.y, button.length, button.height),DrawingCoefficient), 1)

    # Текст
    font_size = int(int(button.length*DrawingCoefficient) // len(button.text))
    myFont = SysFont("Calibri", font_size)
    myText = myFont.render(button.text, 1, button.text_color)
    screen.blit(myText, massive_multiply((
    (button.x + button.length / 2) - myText.get_width() / 2, (button.y + button.height / 2) - myText.get_height() / 2), DrawingCoefficient))


if __name__ == "__main__":
    print("This module is not for direct call!")
