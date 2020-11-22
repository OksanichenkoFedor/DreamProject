import pygame
from LevelParts.Level import *
"""

Do the whole program

"""


# файл запуска программы
pygame.init()
level_screen = pygame.display.set_mode((LevelXSize, LevelYSize))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
flag = False
Test_Level = Level(map_drawer)

while not finished:
    Test_Level.update(level_screen)
    pygame.display.update()
    for event in pygame.event.get():
        Test_Level.game_event(event)
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

#Test11
#Test1
#Еуые228
