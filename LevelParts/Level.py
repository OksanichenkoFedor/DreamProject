from LevelParts.Map import *


class Level:
    # TODO Создать класс уровня который будет мониторить ситуацию происходящюю во время игры, инициализируетс я в
    #  главном меню
    """

    Class of game level
    :field map: Map
    :field down_city: City of first player
    :field up_city:

    """

    def __init__(self, map_file):
        """

        Initialise of level
        :param map_file: File with information about map

        """
        self.map = Map(map_file, x=1, y=1, w=1, h=1)


if __name__ == "__main__":
    print("This module is not for direct call!")
