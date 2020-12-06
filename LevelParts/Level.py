from Draws.LevelDraws import *
from LevelParts.City.City import *
from LevelParts.Map import *
from LevelParts.Menu.Button import *
import pygame


class Level:
    # TODO Создать класс уровня который будет мониторить ситуацию происходящюю во время игры, инициализируетс я в
    #  главном меню
    """

    Class of game level

    : field map: Map of the game
    : field first_city: City of first player
    : field second_city: Сity of second player

    : method __init__(map_file): Initialise level. Receives map_file (for the initialisation of map)
    : method update(screen): Update level and its parts. Redraw level and map
    : method game_event(event): Handle the pygame event

    """

    def __init__(self, map_file, screen):
        """

        Initialise of level
        :param map_file: File with information about map
        :param screen: Surface, where the picture is rendered

        """
        self.image_import()
        self.map = Map(map_file, LevelXSize / 2 - MapXSize / 2, LevelYSize - MapYSize, MapXSize, MapYSize)
        self.first_city = City(["union", "left"], LevelXSize / 2 - MapXSize / 2 - CityXSize,
                               LevelYSize - CityYSize,self.image_bruschatka, self.image_castle_union, self.image_square,self.image_unit_pexota_union)
        self.second_city = City(["order", "right"], LevelXSize / 2 + MapXSize / 2, LevelYSize - CityYSize, self.image_bruschatka, self.image_castle_order, self.image_square,self.image_unit_pexota_order)
        self.but1 = Button(BLC, 0, 0, 100, 75, 10, "Exit", WHT)
        self.screen = screen

    def image_import(self):
        self.image_bruschatka = image.load('images/bruschatka.png').convert_alpha()
        self.image_castle_order = image.load('images/zdanie_orden.png').convert_alpha()
        self.image_castle_union = image.load('images/zdanie_soyuz.png').convert_alpha()
        self.image_square = image.load('images/ploschad.png').convert_alpha()
        self.image_unit_pexota_order = image.load('images/pekhota_orden.png').convert_alpha()
        self.image_unit_pexota_union = image.load('images/pekhota_soyuz.png').convert_alpha()

    def update(self):
        """

        :param screen: Surface, where the picture is rendered

        """

        self.first_city.update(self.screen, self)
        self.second_city.update(self.screen, self)
        self.but1.update_button()
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
        self.first_city.draw(self.screen)
        self.second_city.draw(self.screen)

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
            if event.key == pygame.K_1:
                self.first_city.add_unit(LightInfantryType, 0)
            elif event.key == pygame.K_2:
                self.first_city.add_unit(LightInfantryType, 1)
            elif event.key == pygame.K_3:
                self.first_city.add_unit(LightInfantryType, 2)
            elif event.key == pygame.K_LEFT:
                self.second_city.add_unit(LightInfantryType, 0)
            elif event.key == pygame.K_DOWN:
                self.second_city.add_unit(LightInfantryType, 1)
            elif event.key == pygame.K_RIGHT:
                self.second_city.add_unit(LightInfantryType, 2)
            elif event.key == pygame.K_ESCAPE:
                answer = "pause"
        return answer


if __name__ == "__main__":
    print("This module is not for direct call!")
