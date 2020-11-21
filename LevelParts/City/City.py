from Draws.CityDraws import *
from LevelParts.City.CityCentre import *
from LevelParts.Units.Swordsman import Swordsman


class City:
    # TODO Создать годода, который будет обрабатывать информацию с ним связанную
    """

    Class of city
    : field self.side[1]: A string that tells which side the given city is located on. If side=="left", than this is city, located in the left side of the level
                                                                               If side=="right", than this is city, located in the right side of the level
    : field self.side[0]: String, which say, what type of city we have: "Order" , "Union"
    : field self.life: Life of the city
    : field self.x: First coord of left-up point of city
    : field self.y: Second coord of left-up point of city
    : field self.city_centre: District "City Centre" of the city
    : field self.money: Number of money of this city

    """

    def __init__(self, side, x, y):
        """

        :param side: String, which say, what type of city we have: "Order" , "Union"
        :param coord_side: A string that tells which side the given city is located on. If side=="left", than this is city, located in the left side of the level
                                                                               If side=="right", than this is city, located in the right side of the level
        """

        self.side = side
        self.life = CityLife
        self.city_centre = CityCentre(side, x + CityCentreX, y + CityCentreY)
        self.x = x
        self.y = y
        self.money = 100
        self.Units = []

    def update(self, screen, level):
        """

        :param screen: Surface, where the picture is rendered
        :param level: Object level of whole game
        :return:
        """
        for unit in self.Units:
            unit.update(screen, level)

        if self.side[0] == "order":
            order_city_draw(self, screen)
        else:
            union_city_draw(self, screen)
        pass
        self.city_centre.update(screen)

    def add_unit(self,type):
        if type == SwordsmanType:
            x0=0
            if self.side[1]=="right":
                x0 = MapXSize
            self.Units.append(Swordsman(self.side, [0, x0, int(MapYSize/2)]))






if __name__ == "__main__":
    print("This module is not for direct call!")
