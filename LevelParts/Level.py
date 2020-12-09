from Draws.LevelDraws import *
from LevelParts.City.City import City
from LevelParts.ButtonPole import *
import pygame
from Const.Units import *


class Level:
    """

    Class of game level

    : field map: Map of the game
    : field first_city: City of first player
    : field second_city: Сity of second player
    : field Images: Dictionary of unit images dictionaries

    : method __init__(map_file): Initialise level. Receives map_file (for the initialisation of map)
    : method update(screen): Update level and its parts. Redraw level and map
    : method game_event(event): Handle the pygame event

    """

    def __init__(self, map_file, screen, Images):
        """

        Initialise of level
        :param map_file: File with information about map
        :param screen: Surface, where the picture is rendered

        """
        self.Another_Images = Images[0]
        self.Union_Units_Images = Images[1]
        self.Order_Units_Images = Images[2]
        self.map = Map(map_file, LevelXSize / 2 - MapXSize / 2, LevelYSize - MapYSize, MapXSize, MapYSize)
        self.first_city = City(["union", "left"], LevelXSize / 2 - MapXSize / 2 - CityXSize,
                               LevelYSize - CityYSize, self.Another_Images, self.Union_Units_Images)
        self.first_pole = ButtonPole(LevelXSize / 2 - MapXSize / 2 - CityXSize - ButtonPoleXSize
                                     , LevelYSize - ButtonPoleYSize, [LightInfantryType, "Light Infantry"])
        self.second_city = City(["order", "right"], LevelXSize / 2 + MapXSize / 2, LevelYSize - CityYSize,
                                self.Another_Images,
                                self.Order_Units_Images)
        self.second_pole = ButtonPole(LevelXSize / 2 + MapXSize / 2 + CityXSize, LevelYSize - ButtonPoleYSize,
                                      [LightInfantryType, "Light Infantry"])
        self.but1 = Button(BLC, 0, 0, 100, 75, 10, "Exit", WHT)
        self.screen = screen





    def update(self):
        """


        """

        if self.first_city.update(self) == "tech up":
            if self.first_city.tech_level == 1:
                self.first_pole.add_button([HeavyInfantryType, "Heavy Infantry"])
            elif self.first_city.tech_level == 2:
                self.first_pole.add_button([CavalryType, "Cavalry"])
            elif self.first_city.tech_level == 3:
                self.first_pole.add_button([LongDistanceSoldierType, "Long Distance Soldier"])
            elif self.first_city.tech_level == 4:
                if self.first_city.side[0] == "order":
                    self.first_pole.add_button([HealerType, "Healer"])
                else:
                    self.first_pole.add_button([AlchemistType, "Alchemist"])
        if self.second_city.update(self) == "tech up":
            if self.second_city.tech_level == 1:
                self.second_pole.add_button([HeavyInfantryType, "Heavy Infantry"])
            elif self.second_city.tech_level == 2:
                self.second_pole.add_button([CavalryType, "Cavalry"])
            elif self.second_city.tech_level == 3:
                self.second_pole.add_button([LongDistanceSoldierType, "Long Distance Soldier"])
            elif self.second_city.tech_level == 4:
                if self.second_city.side[0] == "order":
                    self.second_pole.add_button([HealerType, "Healer"])
                else:
                    self.second_pole.add_button([AlchemistType, "Alchemist"])
        if self.first_city.life < 0:
            return 1
        elif self.second_city.life < 0:
            return 2
        else:
            return 0

    def draw(self):
        level_draw(self, self.screen)
        map_draw(self.map, self.screen)
        self.but1.draw_button(self.screen)
        self.first_city.draw(self.screen, self)
        self.second_city.draw(self.screen, self)
        self.first_pole.update(self.screen)
        self.second_pole.update(self.screen)

    def game_event(self, event):
        """

        :param event: Pygame event

        """

        answer = ""
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = ((event.pos[0] * 1.0) / (DrawingCoefficient * 1.0),(event.pos[1] * 1.0) / (DrawingCoefficient * 1.0))
            if event.button == 1:
                if self.but1.is_pressed(pos):
                    answer = "exit"
        if event.type == pygame.KEYDOWN:
            action = []
            if event.key == pygame.K_1:
                action.append("throw unit")
                action.append(0)
                self.first_city.reaction(action)
            elif event.key == pygame.K_2:
                action.append("throw unit")
                action.append(1)
                self.first_city.reaction(action)
            elif event.key == pygame.K_3:
                action.append("throw unit")
                action.append(2)
                self.first_city.reaction(action)
            elif event.key == pygame.K_LEFT:
                action.append("throw unit")
                action.append(0)
                self.second_city.reaction(action)
            elif event.key == pygame.K_DOWN:
                action.append("throw unit")
                action.append(1)
                self.second_city.reaction(action)
            elif event.key == pygame.K_RIGHT:
                action.append("throw unit")
                action.append(2)
                self.second_city.reaction(action)
            elif event.key == pygame.K_w:
                action.append("add unit")
                action.append(self.first_pole.Buttons[self.first_pole.chosen].type)
                self.first_city.reaction(action)
            elif event.key == pygame.K_UP:
                action.append("add unit")
                action.append(self.second_pole.Buttons[self.second_pole.chosen].type)
                self.second_city.reaction(action)
            elif event.key == pygame.K_s:
                action.append("master change")
                if self.first_city.master == 2:
                    action.append(0)
                else:
                    action.append(self.first_city.master+1)
                self.first_city.reaction(action)
            elif event.key == pygame.K_RSHIFT:
                action.append("master change")
                if self.second_city.master == 2:
                    action.append(0)
                else:
                    action.append(self.second_city.master + 1)
                self.second_city.reaction(action)
            elif event.key == pygame.K_ESCAPE:
                answer = "pause"
            elif event.key == pygame.K_q:
                self.first_pole.changeChosen(max(0, self.first_pole.chosen-1))
            elif event.key == pygame.K_e:
                self.first_pole.changeChosen(min(len(self.first_pole.Buttons)-1, self.first_pole.chosen+1))
            elif event.key == pygame.K_PAGEUP:
                self.second_pole.changeChosen(max(0, self.second_pole.chosen-1))
            elif event.key == pygame.K_PAGEDOWN:
                self.second_pole.changeChosen(min(len(self.second_pole.Buttons)-1, self.second_pole.chosen+1))
        return answer


if __name__ == "__main__":
    print("This module is not for direct call!")