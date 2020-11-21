from LevelParts.Map import *
from Draws.LevelDraws import *
from LevelParts.City.City import *
import pygame


class Level:
    # TODO Создать класс уровня который будет мониторить ситуацию происходящюю во время игры, инициализируетс я в
    #  главном меню
    """

    Class of game level
    :field map: Map
    :field left_city: City of first player
    :field right_city: Сity of second player

    """

    def __init__(self, map_file):
        """

        Initialise of level
        :param map_file: File with information about map

        """
        self.map = Map(map_file, LevelXSize / 2 - MapXSize / 2, LevelYSize / 2 - MapYSize / 2, MapXSize, MapYSize)
        self.left_order_city = City("left", "order", LevelXSize / 2 - MapXSize / 2 - CityXSize, LevelYSize / 2 - CityYSize / 2)
        self.right_union_city = City("right", "union", LevelXSize / 2 + MapXSize / 2, LevelYSize / 2 - CityYSize / 2)

    def update(self, screen):
        """

        Update level
        :param screen:
        :return:
        """
        level_draw(self, screen)
        map_draw(self.map, screen)
        self.left_order_city.update(screen)
        self.right_union_city.update(screen)


    def game_event (self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass


if __name__ == "__main__":
    print("This module is not for direct call!")
