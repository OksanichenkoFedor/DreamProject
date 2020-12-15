import pygame
import os
from LevelParts.Level import *
from LevelParts.Menu.MainMenu import *
from LevelParts.Menu.PauseMenu import *
from LevelParts.Menu.Settings import *
from Widgets.MashineLearning.NeuralNetwork import *
from Draws.MenuDraws import *
from random import random

class Game:
    """

    Class of game

    :field main_screen: Screen of whole game
    :field level: Level of this game
    :field level_screen: Surface of level
    :field is_level: Boolean, which is True if level is activated
    :field pause_menu: Pause menu of this game
    :field pause_menu_screen: Surface of pause menu
    :field is_pause: Boolean, which is True if pause menu is activated
    :field main_menu: Main menu of this game
    :field main_menu_screen: Surface of main menu
    :field is_main_menu: Boolean, which is True if main menu is activated
    :field settings: Main menu of this game
    :field settings_screen: Surface of settings
    :field is_settings: Boolean, which is True if settings is activated
    :field finished: Boolean, which is true if game is finished
    :field clock: Clock of game
    :field EasyNetworks: Massive of easy bots
    :field NormalNetworks: Massive of normal bots
    :field HardNetworks: Massive of hard bots
    :field is_bots: Massive of boolean, which are true if current player is bot
    :field Images: Massive of images dictionaries
    :field difficulties: String, which show difficult of current player
    :field sides: List of strings, which tell type of left and right city

    """

    def __init__(self, EasyNN, NormalNN, HardNN):

        self.level_screen = pygame.display.set_mode(
            (int(LevelXSize * DrawingCoefficient), int(LevelYSize * DrawingCoefficient)))
        self.main_screen = pygame.display.set_mode(
            (int(ScreenXSize * DrawingCoefficient), int(ScreenYSize * DrawingCoefficient)))
        self.main_menu_screen = pygame.display.set_mode((int(MainMenuXSize * DrawingCoefficient),
                                                    int(MainMenuYSize * DrawingCoefficient)))
        self.pause_menu_screen = pygame.display.set_mode((int(PauseMenuXSize * DrawingCoefficient),
                                                     int(PauseMenuYSize * DrawingCoefficient)))
        self.settings_screen = pygame.display.set_mode((int(SettingsXSize * DrawingCoefficient),
                                                     int(SettingsYSize * DrawingCoefficient)))

        self.main_screen.blit(self.main_menu_screen, (0, 0))
        self.main_screen.blit(self.level_screen, (0, 0))
        self.main_screen.blit(self.pause_menu_screen, (0, 0))
        self.main_screen.blit(self.settings_screen, (0, 0))

        self.trees = []
        self.bushes = []
        for i in range(number_of_trees):
            self.trees.append((random(), random()))
        for i in range(number_of_bushes):
            self.bushes.append((random(), random()))

        self.EasyNetworks = [NeuralNetwork(self.input_Neural_Network(EasyNN[0]), "union"),
                         NeuralNetwork(self.input_Neural_Network(EasyNN[1]), "order")]
        self.NormalNetworks = [NeuralNetwork(self.input_Neural_Network(NormalNN[0]), "union"),
                             NeuralNetwork(self.input_Neural_Network(NormalNN[1]), "order")]
        self.HardNetworks = [NeuralNetwork(self.input_Neural_Network(HardNN[0]), "union"),
                             NeuralNetwork(self.input_Neural_Network(HardNN[1]), "order")]
        self.sides = ["union", "order"]

        self.clock = pygame.time.Clock()
        self.is_bots = [False, False]
        self.difficulties = "easy"
        self.Images = self.true_image_import(self.level_screen)
        self.level = Level(map_drawer, self.trees, self.bushes, self.level_screen, self.sides, self.Images,
                           self.is_bots, self.EasyNetworks,)
        self.finished = False
        self.is_level = False
        self.is_pause = False
        self.is_main_menu = True
        self.is_settings = False
        self.main_menu = MainMenu(self.main_menu_screen)
        self.pause_menu = PauseMenu(self.pause_menu_screen)
        self.settings = Settings(self.settings_screen)

    def true_image_import(self, screen):
        union_unit_types = [LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, AlchemistType]
        order_unit_types = [LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, HealerType]
        animation_types = [MotionlessAnimationType, MovementAnimationType, DealingDamageAnimationType,
                           TakingDamageAnimationType, DeathAnimationType]
        number = 0

        pygame.display.update()
        draw_download_menu(screen, number, total_image_number)
        Another_Images = {}
        Another_Images["castle union"] = pygame.image.load('images/union_castle.png').convert_alpha()
        number += 1
        pygame.display.update()
        draw_download_menu(screen, number, total_image_number)
        Another_Images["square"] = pygame.image.load('images/ploschad.png').convert_alpha()
        number += 1
        pygame.display.update()
        draw_download_menu(screen, number, total_image_number)
        Another_Images["castle order"] = pygame.image.load('images/order_castle.png').convert_alpha()
        number += 1
        pygame.display.update()
        draw_download_menu(screen, number, total_image_number)
        Another_Images["bruschatka"] = pygame.image.load('images/bruschatka.jpg').convert_alpha()
        number += 1
        pygame.display.update()
        draw_download_menu(screen, number, total_image_number)
        Another_Images["bush"] = pygame.image.load('images/bush.png').convert_alpha()
        number += 1
        pygame.display.update()
        draw_download_menu(screen, number, total_image_number)
        Another_Images["master"] = pygame.image.load('images/master.png').convert_alpha()
        number += 1
        pygame.display.update()
        draw_download_menu(screen, number, total_image_number)
        Another_Images["research centre"] = pygame.image.load('images/research_centre.png').convert_alpha()
        number += 1
        pygame.display.update()
        draw_download_menu(screen, number, total_image_number)
        Another_Images["mine"] = pygame.image.load('images/mine.png').convert_alpha()
        number += 1
        pygame.display.update()
        draw_download_menu(screen, number, total_image_number)
        Another_Images["tree"] = pygame.image.load('images/tree.png').convert_alpha()
        number += 1
        pygame.display.update()
        draw_download_menu(screen, number, total_image_number)



        Left_Union_Units_Images = {}
        for unit_type in union_unit_types:
            Left_Union_Units_Images[unit_type] = {}
            for animation in animation_types:
                massive = []
                for i in range(animation_duration[animation]):
                    file_name = "images/Unionleft/" + "Union" + unit_type + animation + str(i) + ".png"
                    current_image = pygame.image.load(file_name).convert_alpha()
                    massive.append(current_image)
                    number += 1
                    pygame.display.update()
                    draw_download_menu(screen, number, total_image_number, file_name)
                Left_Union_Units_Images[unit_type][animation] = [animation_duration[animation], massive]
        pygame.display.update()
        Right_Union_Units_Images = {}
        for unit_type in union_unit_types:
            Right_Union_Units_Images[unit_type] = {}
            for animation in animation_types:
                massive = []
                for i in range(animation_duration[animation]):
                    file_name = "images/Unionright/" + "Union" + unit_type + animation + str(i) + ".png"
                    current_image = pygame.image.load(file_name).convert_alpha()
                    massive.append(current_image)
                    number += 1
                    pygame.display.update()
                    draw_download_menu(screen, number, total_image_number, file_name)
                Right_Union_Units_Images[unit_type][animation] = [animation_duration[animation], massive]

        Union_Units_Images = {"left": Left_Union_Units_Images, "right": Right_Union_Units_Images}
        pygame.display.update()
        Left_Order_Units_Images = {}
        for unit_type in order_unit_types:
            Left_Order_Units_Images[unit_type] = {}
            for animation in animation_types:
                massive = []
                for i in range(animation_duration[animation]):
                    file_name = "images/Orderleft/" + "Order" + unit_type + animation + str(i) + ".png"
                    current_image = pygame.image.load(file_name).convert_alpha()
                    massive.append(current_image)
                    number += 1
                    pygame.display.update()
                    draw_download_menu(screen, number, total_image_number, file_name)
                Left_Order_Units_Images[unit_type][animation] = [animation_duration[animation], massive]
        pygame.display.update()
        Right_Order_Units_Images = {}
        for unit_type in order_unit_types:
            Right_Order_Units_Images[unit_type] = {}
            for animation in animation_types:
                massive = []
                for i in range(animation_duration[animation]):
                    file_name = "images/Orderright/" + "Order" + unit_type + animation + str(i) + ".png"
                    current_image = pygame.image.load(file_name).convert_alpha()
                    massive.append(current_image)
                    number += 1
                    pygame.display.update()
                    draw_download_menu(screen, number, total_image_number, file_name)
                Right_Order_Units_Images[unit_type][animation] = [animation_duration[animation], massive]
        pygame.display.update()
        Order_Units_Images = {"left": Left_Order_Units_Images, "right": Right_Order_Units_Images}

        Units_Images = {"order": Order_Units_Images, "union": Union_Units_Images}

        return Another_Images, Units_Images

    def activate_pause_menu(self):
        self.pause_menu_screen.set_alpha(255)
        self.level_screen.set_alpha(100)
        self.main_menu_screen.set_alpha(0)
        self.settings_screen.set_alpha(0)
        self.is_pause = True
        self.is_main_menu = False
        self.is_level = False
        self.is_settings = False

    def activate_level(self):
        self.pause_menu_screen.set_alpha(0)
        self.level_screen.set_alpha(255)
        self.main_menu_screen.set_alpha(0)
        self.settings_screen.set_alpha(0)
        self.is_pause = False
        self.is_main_menu = False
        self.is_level = True
        self.is_settings = False

    def activate_main_menu(self):
        self.pause_menu_screen.set_alpha(0)
        self.level_screen.set_alpha(100)
        self.main_menu_screen.set_alpha(255)
        self.settings_screen.set_alpha(0)
        self.is_pause = False
        self.is_main_menu = True
        self.is_level = False
        self.is_settings = False

    def activate_settings(self):
        self.pause_menu_screen.set_alpha(0)
        self.level_screen.set_alpha(100)
        self.main_menu_screen.set_alpha(0)
        self.settings_screen.set_alpha(255)
        self.is_pause = False
        self.is_main_menu = False
        self.is_level = False
        self.is_settings = True

    def update(self):
        self.clock.tick(FPS)
        Result = 0
        if self.is_level:
            self.level.draw()
            Result = self.level.update()
        elif self.is_pause:
            Result = self.pause_menu.update()
        elif self.is_main_menu:
            Result = self.main_menu.update()
        elif self.is_settings:
            Result = self.settings.update()

        if Result == 1:
            self.finished = True
            print("Победил первый город")
        elif Result == 2:
            self.finished = True
            print("Победил второй город")
        pygame.display.update()

    def game_event(self, curr_event):
        answer = ""
        if self.is_level:
            answer = self.level.game_event(curr_event)
        elif self.is_pause:
            answer = self.pause_menu.game_event(curr_event)
        elif self.is_main_menu:
            answer = self.main_menu.game_event(curr_event)
        elif self.is_settings:
            answer = self.settings.game_event(curr_event)
        if answer == "exit":
            self.finished = True
        elif answer == "resume":
            self.activate_level()
        elif answer == "pause":
            self.activate_pause_menu()
        elif answer == "main menu":
            print(self.sides)
            self.restart()
            self.activate_main_menu()
        elif answer == "start":
            self.restart()
        elif answer == "main settings":
            self.settings.returned = "main"
            self.activate_settings()
        elif answer == "pause settings":
            self.settings.returned = "pause"
            self.activate_settings()
        elif answer == "easy bots":
            self.difficulties = [0,0]
        elif answer == "normal bots":
            self.difficulties = [1,1]
        elif answer == "hard bots":
            self.difficulties = [2,2]
        elif answer == "first bot":
            self.is_bots[0] = True
        elif answer == "first player":
            self.is_bots[0] = False
        elif answer == "second bot":
            self.is_bots[1] = True
        elif answer == "second player":
            self.is_bots[1] = False
        elif answer == "return pause":
            self.restart()
            self.level.draw()
            self.activate_pause_menu()
        elif answer == "first union":
            self.sides[0] = "union"
        elif answer == "first order":
            self.sides[0] = "order"
        elif answer == "second union":
            self.sides[1] = "union"
        elif answer == "second order":
            self.sides[1] = "order"
        else:
            pass
        if curr_event.type == pygame.QUIT:
            self.finished = True

    def restart(self):
        self.level = Level(map_drawer, self.trees, self.bushes, self.level_screen, self.sides, self.Images,
                           self.is_bots, self.current_network())
        self.activate_level()

    def current_network(self):
        if self.difficulties == "easy":
            return self.EasyNetworks
        elif self.difficulties == "normal":
            return self.NormalNetworks
        else:
            return self.HardNetworks

    def input_Neural_Network(self, file_name):
        file_obj = open(file_name, 'r')
        matrix = []
        shift = []
        for i in range(len(NNLayers) - 1):
            matrix.append(np.zeros((NNLayers[i + 1], NNLayers[i]), dtype=float))
            for j in range(NNLayers[i + 1]):
                for k in range(NNLayers[i]):
                    matrix[i][j][k] = float(file_obj.readline())
        for i in range(len(NNLayers) - 1):
            shift.append(np.zeros((NNLayers[i + 1],), dtype=float))
            for j in range(NNLayers[i + 1]):
                shift[i][j] = float(file_obj.readline())
        file_obj.close()
        return matrix, shift