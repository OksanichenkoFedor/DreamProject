from Const.Units import *
from LevelParts.City.CityCentre import *
from LevelParts.Units.LightInfantry import LightInfantry


class City(Interactable):
    """

    Class of city
    : field self.x: First coord of left-up point of city
    : field self.y: Second coord of left-up point of city
    : field self.city_centre: District "City Centre" of the city
    : field self.money: Number of money of this city
    : field self.Units: Massive of units of the city
    : field self.Districts: Massive of districts of the city

    : method self.__init__(side, x, y): Initialise City. Receives side, x, y
    : method self.update(screen, level): Update all parts of city (units, districts) and redraw city
    : method self.add_unit(type): Add unit of given type (type)

    """

    def __init__(self, side, x, y):
        super().__init__(side, CityLife)
        city_centre = CityCentre(side, x + CityCentreX, y + CityCentreY)
        self.x = x
        self.y = y
        self.money = 100
        self.Units = []
        self.Districts = []
        self.Districts.append(city_centre)
        print(len(self.Districts))

    def update(self, screen, level):
        """

        Update city. If life of city district under zero, than this district refill this life to zero,
                     pulling them from city.
        :param screen: Surface, where the picture is rendered
        :param level: Level of the game

        """
        Cash = []
        for unit in self.Units:
            Cash.append(unit.update(screen, level))

        if self.side[0] == "order":
            order_city_draw(self, self.side[1], screen)
        else:
            union_city_draw(self, self.side[1], screen)

        for i in range(len(self.Districts)):
            self.Districts[i].update(screen)
            print(self.Districts[i].life)
            if self.Districts[i].life < 0:
                self.life += self.Districts[i].life
                self.Districts[i].life = 0

        return Cash

    def add_unit(self, type, road=0):
        """

        :param type: Type of the unit
        :param road: Number of start road from up to down
        """
        if type == LightInfantryType:
            x0 = 0
            if self.side[1] == "right":
                x0 = MapXSize
            if self.money >= LightInfantryCost:
                self.Units.append(LightInfantry(self.side, ["battle_pole", x0, int(MapYSize / 2)]))
                self.money -= LightInfantryCost


if __name__ == "__main__":
    print("This module is not for direct call!")
