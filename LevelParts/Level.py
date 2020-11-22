from Draws.LevelDraws import *
from LevelParts.City.City import *
from LevelParts.Map import *
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

    def __init__(self, map_file):
        """

        Initialise of level
        :param map_file: File with information about map

        """
        self.map = Map(map_file, LevelXSize / 2 - MapXSize / 2, LevelYSize / 2 - MapYSize / 2, MapXSize, MapYSize)
        self.first_city = City(("order", "left"), LevelXSize / 2 - MapXSize / 2 - CityXSize,
                                    LevelYSize / 2 - CityYSize / 2)
        self.second_city = City(("union", "right"), LevelXSize / 2 + MapXSize / 2, LevelYSize / 2 - CityYSize / 2)

    def update(self, screen):
        """

        :param screen: Surface, where the picture is rendered

        """
        level_draw(self, screen)
        map_draw(self.map, screen)
        self.first_city.update(screen, self)
        self.second_city.update(screen, self)

    def game_event(self, event):
        """

        :param event: Pygame event

        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.first_city.add_unit(SwordsmanType)
            elif event.key == pygame.K_RIGHT:
                self.second_city.add_unit(SwordsmanType)


if __name__ == "__main__":
    print("This module is not for direct call!")
