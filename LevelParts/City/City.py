from Const.Units import *
from LevelParts.City.Districts.CityCentre import *
from LevelParts.City.Districts.Mine import *
from LevelParts.City.Districts.ResearchCentre import *
from LevelParts.Units.Alchemist import Alchemist
from LevelParts.Units.Cavalry import Cavalry
from LevelParts.Units.Healer import Healer
from LevelParts.Units.HeavyInfantry import HeavyInfantry
from LevelParts.Units.LightInfantry import LightInfantry
from LevelParts.Units.LongDistanceSoldier import LongDistanceSoldier
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
    : field self.master : Number of district with master
    : field self.Units_Images: Dictionary of unit images dictionary
    : field self.Another_Images: Dictionary of another images

    : method self.__init__(side, x, y): Initialise City. Receives side, x, y
    : method self.update(screen, level): Update all parts of city (units, districts) and redraw city
    : method self.add_unit(type): Add unit of given type (type)

    """

    def __init__(self, side, x, y, Another_Images, Units_Images):
        super().__init__(side, CityLife)
        self.Another_Images = Another_Images
        mine = Mine(side, x + MineX, y + MineY, self.Another_Images["mine"], self.Another_Images["master"])
        city_centre = CityCentre(side, x + CityCentreX, y + CityCentreY, self.Another_Images["castle "+self.side[0]],
                                 Another_Images["square"], self.Another_Images["master"])
        research_centre = ResearchCentre(side, x + ResearchCentreX, y + ResearchCentreY,
                                         self.Another_Images["research centre"], self.Another_Images["master"])
        self.x = x
        self.y = y
        self.money = 0.0
        self.Units = []
        self.Queue_Units = []
        self.Buffered_Units = []
        self.Districts = []
        self.Unit_Images = Units_Images
        self.Districts.append(research_centre)
        self.Districts.append(city_centre)
        self.Districts.append(mine)
        self.master = CityCentreNumber

        self.tech_level = 0
        self.tech_points = 0.0

    def update(self, level):
        """

        Update city. If life of city district under zero, than this district refill this life to zero,
                     pulling them from city.
        :param level: Level of the game

        """
        if len(self.Queue_Units) > 0:
            if self.Queue_Units[0].train_time <= 0 and len(self.Buffered_Units) <= MaximumBufferVolume:
                self.Queue_Units[0].XSize /= 2
                self.Queue_Units[0].YSize /= 2
                self.Queue_Units[0].coord[0] = "buffered"
                self.Buffered_Units.append(self.Queue_Units[0])
                self.Queue_Units.pop(0)
                self.buffer_update()
            else:
                self.Queue_Units[0].train_time -= 1


        for i in range(len(self.Units)-1, -1, -1):
            self.Units[i].update(level)

        for i in range(len(self.Units)-1, -1, -1):
            if self.Units[i].life <= 0:
                self.Units.pop(i)

        for district in self.Districts:
            if district.life < 0:
                self.life += district.life
                district.life = 0
        self.tech_points = self.Districts[ResearchCentreNumber].update(self.tech_points)
        self.money = self.Districts[MineNumber].update(self.money)
        if self.tech_points > (self.tech_level+1)*EachTechPoints:
            self.tech_level += 1
            self.tech_points -= self.tech_level*EachTechPoints
            return "tech up"

    def draw(self, screen, level):
        city_draw(self, self.side[0], screen, self.Another_Images["bruschatka"])
        for district in self.Districts:
            district.draw(screen)
        for unit in self.Units:
            unit.draw(screen, level)
        if len(self.Buffered_Units) > 0:
            for i in range(len(self.Buffered_Units) - 1, -1, -1):
                self.Buffered_Units[i].draw(screen, level)

    def add_unit(self, type):
        """

        :param type: Type of the unit

        """
        is_new_unit = False
        unit = 0
        if type == LightInfantryType:
            unit = LightInfantry(self.side, ("queue", 0, 0), self.Unit_Images[type])
            is_new_unit = True
        elif type == HeavyInfantryType:
            unit = HeavyInfantry(self.side, ("queue", 0, 0), self.Unit_Images[type])
            is_new_unit = True
        elif type == CavalryType:
            unit = Cavalry(self.side, ("queue", 0, 0), self.Unit_Images[type])
            is_new_unit = True
        elif type == LongDistanceSoldierType:
            unit = LongDistanceSoldier(self.side, ("queue", 0, 0), self.Unit_Images[type])
            is_new_unit = True
        elif type == HealerType:
            unit = Healer(self.side, ("queue", 0, 0), self.Unit_Images[type])
            is_new_unit = True
        elif type == AlchemistType:
            unit = Alchemist(self.side, ("queue", 0, 0), self.Unit_Images[type])
            is_new_unit = True

        if is_new_unit:
            if self.master == CityCentreNumber:
                unit.train_time = unit.train_time / 2
                unit.train_timer = unit.train_timer / 2
            if self.money >= unit.cost:
                self.Queue_Units.append(unit)
                self.money -= unit.cost
                return True
        return False

    def reaction(self, action):
        if action[0] == "add unit":
            return self.add_unit(action[1])
        elif action[0] == "throw unit":
            if len(self.Buffered_Units) > 0:
                self.Buffered_Units[0].coord = [self.side[1], action[1], 0]
                self.Buffered_Units[0].XSize *= 2
                self.Buffered_Units[0].YSize *= 2
                self.Units.append(self.Buffered_Units[0])
                self.Buffered_Units.pop(0)
                self.buffer_update()
        elif action[0] == "master change":
            self.master = action[1]
            for district in self.Districts:
                if district.number == action[1]:
                    district.master = 1
                else:
                    district.master = 0
    def buffer_update(self):
        for i in range(len(self.Buffered_Units)):
            if self.side[1] == "right":
                self.Buffered_Units[i].change_buffer_place(self.x + BufferedAreaX1 +
                                                           (BufferedAreaX2 * 1.0 - BufferedAreaX1 * 1.0) * (
                                                                   (1.0 * i) /
                                                                   (1.0 * len(self.Buffered_Units))),
                                                           self.y + BufferedAreaY)
            else:
                self.Buffered_Units[i].change_buffer_place(self.x + BufferedAreaX1 +
                                                           (BufferedAreaX2 * 1.0 - BufferedAreaX1 * 1.0) * (
                                                                   (1.0 * (len(self.Buffered_Units) - 1 - i)) /
                                                                   (1.0 * len(self.Buffered_Units))),
                                                           self.y + BufferedAreaY)




if __name__ == "__main__":
    print("This module is not for direct call!")
