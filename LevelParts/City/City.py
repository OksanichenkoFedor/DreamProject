from Const.Units import *
from LevelParts.City.Districts.CityCentre import *
from LevelParts.City.Districts.Mine import *
from LevelParts.City.Districts.ResearchCentre import *
from LevelParts.Units.LightInfantry import LightInfantry
from LevelParts.ButtonPole import *


class City(Interactable):
    """

    Class of city
    : field self.x: First coord of left-up point of city
    : field self.y: Second coord of left-up point of city
    : field self.city_centre: District "City Centre" of the city
    : field self.money: Number of money of this city
    : field self.Units: Massive of units of the city
    : field self.Buffered_Units: Massive of units in buffer
    : field self.Districts: Massive of districts of the city
    : field self.pole : Button Pole of this city
    : field self.tech_level : Level of technologies

    : method self.__init__(side, x, y): Initialise City. Receives side, x, y
    : method self.update(screen, level): Update all parts of city (units, districts) and redraw city
    : method self.add_unit(type): Add unit of given type (type)

    """

    def __init__(self, side, x, y, image_bruschatka, image_castle, image_square, unit_image):
        super().__init__(side, CityLife)
        self.image_bruschatka = image_bruschatka
        mine = Mine(side, x + MineX, y + MineY)
        city_centre = CityCentre(side, x + CityCentreX, y + CityCentreY, image_castle, image_square)
        research_centre = ResearchCentre(side, x + ResearchCentreX, y + ResearchCentreY)
        self.x = x
        self.y = y
        self.money = 100.0
        self.Units = []
        self.Buffered_Units = []
        self.Districts = []
        self.Districts.append(research_centre)
        self.Districts.append(city_centre)
        self.Districts.append(mine)
        self.unit_image = unit_image
        self.pole = ButtonPole(self.x, self.y)
        self.tech_level = 0
        self.tech_points = 0.0

    def update(self, level):
        """

        Update city. If life of city district under zero, than this district refill this life to zero,
                     pulling them from city.
        :param level: Level of the game

        """
        for i in range(len(self.Units)-1, -1, -1):
            self.Units[i].update(level)

        for i in range(len(self.Buffered_Units) - 1, -1, -1):
            self.Buffered_Units[i].update(level)

        for i in range(len(self.Units)-1, -1, -1):
            if self.Units[i].life <= 0:
                self.Units.pop(i)

        for district in self.Districts:
            if district.life < 0:
                self.life += district.life
                district.life = 0
        self.tech_points = self.Districts[ResearchCentreNumber].update(self.tech_points)
        self.money = self.Districts[MineNumber].update(self.money)
        if self.tech_points>(self.tech_level+1)*EachTechPoints:
            self.tech_level += 1
            self.tech_points -= self.tech_level*EachTechPoints
        self.pole.update()

    def draw(self, screen, level):
        city_draw(self, self.side[0], screen, self.image_bruschatka)
        for district in self.Districts:
            district.draw(screen)
        for i in range(len(self.Units)-1, -1, -1):
            self.Units[i].draw(screen, level)
        self.pole.draw(screen)

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
                self.Units.append(LightInfantry(self.side, (self.side[1], road, 0),self.unit_image))
                self.money -= LightInfantryCost


if __name__ == "__main__":
    print("This module is not for direct call!")
