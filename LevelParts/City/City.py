from Const.Units import *
from LevelParts.City.CityCentre import *
from LevelParts.Units.Swordsman import Swordsman


class City:
    """

    Class of city
    : field self.side[1]: A string that tells which side the given city is located on.
                            If side=="left", than this is city, located in the left side of the level
                            If side=="right", than this is city, located in the right side of the level
    : field self.side[0]: String, which say, what type of city we have: "Order" , "Union"
    : field self.life: Life of the city
    : field self.x: First coord of left-up point of city
    : field self.y: Second coord of left-up point of city
    : field self.city_centre: District "City Centre" of the city
    : field self.money: Number of money of this city

    : method self.__init__(side, x, y): Initialise City. Receives side, x, y
    : method self.update(screen, level) Update all parts of city (units, districts) and redraw city
    : method self.add_unit(type) Add unit of given type (type)

    """

    def __init__(self, side, x, y):
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
        :param level: Level of the game

        """
        for unit in self.Units:
            unit.update(screen, level)

        if self.side[0] == "order":
            order_city_draw(self, self.side[1], screen)
        else:
            union_city_draw(self, self.side[1], screen)
        pass
        self.city_centre.update(screen)

    def add_unit(self, type):
        if type == SwordsmanType:
            x0 = 0
            if self.side[1] == "right":
                x0 = MapXSize
            if self.money >= SwordsmanCost:
                self.Units.append(Swordsman(self.side, [0, x0, int(MapYSize / 2)]))
                self.money -= SwordsmanCost


if __name__ == "__main__":
    print("This module is not for direct call!")
