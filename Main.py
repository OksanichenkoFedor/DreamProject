import pygame
import os
from LevelParts.Level import *
from LevelParts.Menu.MainMenu import *
from LevelParts.Menu.PauseMenu import *
from Widgets.MashineLearning.NeuralNetwork import *
from Draws.MenuDraws import *
from Game import *
"""

Do the whole program

"""

#Импорт картинок





def true_image_import(screen):
    union_unit_types = [LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, AlchemistType]
    order_unit_types = [LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, HealerType]
    animation_types = [MotionlessAnimationType, MovementAnimationType, DealinDamageAnimationType,
                       TakingDamageAnimationType, DeathAnimationType]
    number = 0

    pygame.display.update()
    draw_download_menu(screen, number, total_image_number)
    Another_Images = {}
    Another_Images["castle union"] = pygame.image.load('images/zdanie_soyuz.png').convert_alpha()
    number += 1
    pygame.display.update()
    draw_download_menu(screen, number, total_image_number)
    Another_Images["square"] = pygame.image.load('images/ploschad.png').convert_alpha()
    number += 1
    pygame.display.update()
    draw_download_menu(screen, number, total_image_number)
    Another_Images["castle order"] = pygame.image.load('images/zdanie_orden.png').convert_alpha()
    number += 1
    pygame.display.update()
    draw_download_menu(screen, number, total_image_number)
    Another_Images["bruschatka"] = pygame.image.load('images/bruschatka.png').convert_alpha()
    number += 1
    pygame.display.update()
    draw_download_menu(screen, number, total_image_number)

    Union_Units_Images = {}
    for unit_type in union_unit_types:
        Union_Units_Images[unit_type] = {}
        for animation in animation_types:
            massive = []
            for i in range(animation_duration[animation]):
                file_name = "images/" + "Union" + unit_type + animation + str(i) + ".png"
                current_image = pygame.image.load(file_name).convert_alpha()
                massive.append(current_image)
                number += 1
                pygame.display.update()
                draw_download_menu(screen, number, total_image_number)
            Union_Units_Images[unit_type][animation] = [animation_duration[animation], massive]

    Order_Units_Images = {}
    for unit_type in order_unit_types:
        Order_Units_Images[unit_type] = {}
        for animation in animation_types:
            massive = []
            for i in range(animation_duration[animation]):
                file_name = "images/" + "Order" + unit_type + animation + str(i) + ".png"
                current_image = pygame.image.load(file_name).convert_alpha()
                massive.append(current_image)
                number += 1
                pygame.display.update()
                draw_download_menu(screen, number, total_image_number)
            Order_Units_Images[unit_type][animation] = [animation_duration[animation], massive]
    return Another_Images, Union_Units_Images, Order_Units_Images


# Импорт нейросети


def input_Neural_Network(file_name):
    file_obj = open(file_name, 'r')
    matrix = []
    shift = []
    for i in range(len(NNLayers)-1):
        matrix.append(np.zeros((NNLayers[i + 1], NNLayers[i]), dtype=float))
        for j in range(NNLayers[i+1]):
            for k in range(NNLayers[i]):
                matrix[i][j][k] = float(file_obj.readline())
    for i in range(len(NNLayers)-1):
        shift.append(np.zeros((NNLayers[i + 1],), dtype=float))
        for j in range(NNLayers[i+1]):
            shift[i][j] = float(file_obj.readline())
    file_obj.close()
    return matrix, shift


# файл запуска программы


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


EasyNN = ["Widgets/MashineLearning/differentAI/UnionNN20.txt", "Widgets/MashineLearning/differentAI/OrderNN20.txt"]
test_game = Game(EasyNN, EasyNN, EasyNN)

while not test_game.finished:
    test_game.update()
    for event in pygame.event.get():
        test_game.game_event(event)
pygame.quit()

