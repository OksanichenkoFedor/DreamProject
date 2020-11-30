import pygame
import os
from LevelParts.Level import *
"""

Do the whole program

"""


# файл запуска программы
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
#level_screen = pygame.display.set_mode((LevelXSize, LevelYSize), pygame.FULLSCREEN)
level_screen = pygame.display.set_mode((int(LevelXSize*DrawingCoefficient), int(LevelYSize*DrawingCoefficient)))
#если лагает переключи на это
pygame.display.update()
clock = pygame.time.Clock()
finished = False
flag = False
Test_Level = Level(map_drawer, level_screen)

while not finished:
    Test_Level.update(level_screen)
    pygame.display.update()
    for event in pygame.event.get():
        finished = Test_Level.game_event(event)
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

