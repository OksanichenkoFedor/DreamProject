from LevelParts.Level import *
from Const.Level import *
from LevelParts.Map import *
from pygame.draw import *
from pygame.font import *
#from pygame import *


def map_draw(level_map: Map, screen):
    """

    Draw map
    :param level_map: Object of class Map
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, WHT, (level_map.x, level_map.y, level_map.width, level_map.height))
    for i in level_map.Left_Roads:
        for j in i:
            circle(screen, BLC, j, 20)
    for i in level_map.Right_Roads:
        for j in i:
            circle(screen, BLC, j, 20)
    polygon(screen, BLC, level_map.Pole_Points)


def level_draw(level, screen):
    """

    Draw level: all without all objects (in this function you don't need to draw map, city and another objects)
    :param level: Object of class Level, that we will draw
    :param screen: Surface, where the picture is rendered

    """
    rect(screen, BLU, (0, 0, LevelXSize, LevelXSize))


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
    rect(screen, button.color, (button.x, button.y, button.length, button.height), 0)
    rect(screen, (190, 190, 190), (button.x, button.y, button.length, button.height), 1)

    # Текст
    font_size = int(button.length // len(button.text))
    myFont = SysFont("Calibri", font_size)
    myText = myFont.render(button.text, 1, button.text_color)
    screen.blit(myText, (
    (button.x + button.length / 2) - myText.get_width() / 2, (button.y + button.height / 2) - myText.get_height() / 2))


if __name__ == "__main__":
    print("This module is not for direct call!")
