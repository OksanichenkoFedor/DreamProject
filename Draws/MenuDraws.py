from pygame.draw import *
from Const.Level import *
from Const.Menus import *
from pygame.font import *

def massive_multiply(j, a):
    j1 = []
    for i in range(len(j)):
        j1.append(int(j[i] * a))
    return j1


def draw_download_menu(screen, number, total_number):
    screen.fill(WHT)
    rect(screen, GRN, massive_multiply((0.35*LevelXSize, 0.66*LevelYSize, 0.3 * LevelXSize*\
                                        ((1.0*number)/(1.0*total_number)), 0.05*LevelYSize), DrawingCoefficient))
    rect(screen, BLC, massive_multiply((0.35 * LevelXSize, 0.66 * LevelYSize, 0.3 * LevelXSize, 0.05 * LevelYSize),
                                       DrawingCoefficient), 1)

def draw_settings(screen):
    rect(screen, WHT, massive_multiply((0, 0, SettingsXSize, SettingsYSize), DrawingCoefficient))
    font_size = int(int(0.2 * SettingsXSize * DrawingCoefficient) // len(SettingsTextDifficulty))
    myFont = SysFont("Calibri", font_size)
    myText = myFont.render(SettingsTextDifficulty, 1, BLC)
    screen.blit(myText, massive_multiply((
        (SettingsXSize / 2 - myText.get_width() / 2,
        SettingsYSize*0.2 - myText.get_height() / 2), DrawingCoefficient)))

    font_size = int(int(0.2 * SettingsXSize * DrawingCoefficient) // len(SettingsTextPlayers))
    myFont = SysFont("Calibri", font_size)
    myText = myFont.render(SettingsTextPlayers, 1, BLC)
    screen.blit(myText, massive_multiply((
        (SettingsXSize / 2 - myText.get_width() / 2,
         SettingsYSize*0.6 - myText.get_height() / 2), DrawingCoefficient)))

if __name__ == "__main__":
    print("This module is not for direct call!")
