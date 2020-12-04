import pygame
import os
from LevelParts.Level import *
from LevelParts.Menu.MainMenu import *
from LevelParts.Menu.PauseMenu import *
"""

Do the whole program

"""

#Импорт картинок



# файл запуска программы
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
level_screen = pygame.display.set_mode((int(LevelXSize*DrawingCoefficient), int(LevelYSize*DrawingCoefficient)))
main_screen = pygame.display.set_mode((int(ScreenXSize*DrawingCoefficient), int(ScreenYSize*DrawingCoefficient)))
main_menu_screen = pygame.display.set_mode((int(MainMenuXSize*DrawingCoefficient), int(MainMenuYSize*DrawingCoefficient)))
pause_menu_screen = pygame.display.set_mode((int(PauseMenuXSize*DrawingCoefficient), int(PauseMenuYSize*DrawingCoefficient)))
main_screen.blit(main_menu_screen, (0, 0))
main_screen.blit(level_screen, (0, 0))
main_screen.blit(pause_menu_screen, (0, 0))
Test_Level = Level(map_drawer, level_screen)
Main_Menu = MainMenu(main_menu_screen)
Pause_Menu = PauseMenu(pause_menu_screen)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
flag = False
is_level = True
is_pause = False
is_main_menu = False


def activate_pause_menu():
    pause_menu_screen.set_alpha(255)
    level_screen.set_alpha(100)
    main_menu_screen.set_alpha(0)
    is_pause = True
    is_main_menu = False
    is_level = False


while not finished:
    clock.tick(FPS)
    Result = 0
    if is_level:
        Result = Test_Level.update()
    elif is_pause:
        Result = Pause_Menu.update()
    elif is_main_menu:
        Result = Main_Menu.update()

    if Result==1:
        finished = True
        print("Победил первый город")
    elif Result==2:
        finished = True
        print("Победил второй город")
    pygame.display.update()
    for event in pygame.event.get():
        answer = ""
        if is_level:
            answer = Test_Level.game_event(event)
        elif is_pause:
            answer = Pause_Menu.game_event(event)
        elif is_main_menu:
            answer = Main_Menu.game_event(event)
        if answer == "exit":
            finished = True
        elif answer == "resume":
            pause_menu_screen.set_alpha(0)
            level_screen.set_alpha(255)
            main_menu_screen.set_alpha(0)
            is_pause = False
            is_main_menu = False
            is_level = True
        elif answer == "pause":
            pause_menu_screen.set_alpha(255)
            level_screen.set_alpha(0)
            main_menu_screen.set_alpha(0)
            is_pause = True
            is_main_menu = False
            is_level = False
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

