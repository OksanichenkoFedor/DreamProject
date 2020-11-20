from LevelParts.Map import *
from Draws.LevelDraws import *
from LevelParts.City.City import *


class Level:
    # TODO Создать класс уровня который будет мониторить ситуацию происходящюю во время игры, инициализируетс я в
    #  главном меню
    """

    Class of game level
    :field map: Map
    :field left_city: City of first player
    :field right_city:

    """

    def __init__(self, map_file):
        """

        Initialise of level
        :param map_file: File with information about map

        """
        self.map = Map(map_file, LevelXSize / 2 - MapXSize / 2, LevelYSize / 2 - MapYSize / 2, MapXSize, MapYSize)
        self.left_city = City("left")
        self.right_city = City("right")

    def update(self, screen):
        """

        Update level
        :param screen:
        :return:
        """
        level_draw(self, screen)
        map_draw(self.map, screen)
        self.left_city.update(screen)
        self.right_city.update(screen)


if __name__ == "__main__":
    print("This module is not for direct call!")
