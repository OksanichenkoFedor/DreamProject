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
        self.map = Map(map_file, LevelXSize / 2 - MapXSize / 2, LevelYSize - MapYSize, MapXSize, MapYSize)
        self.first_city = City(("order", "left"), LevelXSize / 2 - MapXSize / 2 - CityXSize,
                               LevelYSize - CityYSize)
        self.second_city = City(("union", "right"), LevelXSize / 2 + MapXSize / 2, LevelYSize - CityYSize)
        self.but1 = Button(BLC, 0, 0, 100, 75, 10, "Exit", WHT)

    def update(self, screen):
        """

        :param screen: Surface, where the picture is rendered

        """
        level_draw(self, screen)
        map_draw(self.map, screen)
        self.first_city.update(screen, self)
        self.second_city.update(screen, self)
        self.but1.update_button(screen)

    def game_event(self, event):
        """

        :param event: Pygame event

        """
        finished = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.but1.is_pressed(event.pos):
                    finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.first_city.add_unit(LightInfantryType)
            elif event.key == pygame.K_RIGHT:
                self.second_city.add_unit(LightInfantryType)
        return finished


if __name__ == "__main__":
    print("This module is not for direct call!")
