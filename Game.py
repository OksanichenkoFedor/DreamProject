import pygame
from LevelParts.Level import *


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
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
