from Draws.CityDraws import *

class City:
    # TODO Создать годода, который будет обрабатывать информацию с ним связанную
    """

    Class of city
    : field side: A string that tells which side the given city is located on. If side=="left", than this is city, located in the left side of the level
                                                                               If side=="right", than this is city, located in the right side of the level

    """
    def __init__(self, side):
        """

        :param side:
        """

        self.side = side

    def update(self, screen):
        """

        :param screen:
        :return:
        """

        if self.side=="left" :
            left_city_draw(self, screen)
        else :
            right_city_draw(self, screen)
        pass


if __name__ == "__main__":
    print("This module is not for direct call!")
