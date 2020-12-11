from LevelParts.Map import *
from Const.Units import *
from Const.Level import *
from LevelParts.City.City import City
from Widgets.MashineLearning.NeuralNetwork import *
from Const.MashineLearning import *
import numpy as np


class LearningLevel():
    """

    Class of changed level, which will realise right between to neural networks

    : field first_nn: First neural network
    : field second_nn: Second neural network
    : field first_city: First city
    : field second_city: Second city
    : map: Map of the level

    : method smth:

    """
    def __init__(self, map_file, Fake_Images, NN_Order, NN_Union):
        self.first_city = City(["union", "left"], LevelXSize / 2 - MapXSize / 2 - CityXSize,
                               LevelYSize - CityYSize, Fake_Images[0], Fake_Images[1])

        self.second_city = City(["order", "right"], LevelXSize / 2 + MapXSize / 2, LevelYSize - CityYSize,
                            Fake_Images[0],
                            Fake_Images[2])

        self.NN_Union = NN_Union
        self.NN_Order = NN_Order

        self.union_score = 0
        self.order_score = 0

        self.map = Map(map_file, LevelXSize / 2 - MapXSize / 2, LevelYSize - MapYSize, MapXSize, MapYSize)

    def game(self):
        """

        Process whole game and return scores of both NN
        :return:
        """
        timer = 0
        running = True
        while running:
            timer += 1
            self.union_score -= TimeCost
            self.order_score -= TimeCost
            self.update()
            if self.first_city.life<0:
                running = False
                self.order_score += WinCost
            if self.second_city.life<0:
                running = False
                self.union_score += WinCost
            if timer > MaxGameTime:
                running = False

        return self.union_score, self.order_score

    def update(self):
        """

        Process level situation and change NN scores
        :return:
        """
        prev_union_life = [self.first_city.life, self.first_city.Districts[0].life, self.first_city.Districts[1].life,
                           self.first_city.Districts[2].life]
        prev_order_life = [self.second_city.life, self.second_city.Districts[0].life,
                           self.second_city.Districts[1].life, self.second_city.Districts[2].life]
        info = self.info_parameters()
        union_action = self.NN_Union.reaction(info[0])
        if union_action[0] == "add unit":
            is_addable = False
            if union_action[1] == LightInfantryType:
                is_addable = True
            elif union_action[1] == HeavyInfantryType:
                if self.first_city.tech_level >= 1:
                    is_addable = True
            elif union_action[1] == CavalryType:
                if self.first_city.tech_level >= 2:
                    is_addable = True
            elif union_action[1] == LongDistanceSoldierType:
                if self.first_city.tech_level >= 3:
                    is_addable = True
            elif union_action[1] == AlchemistType:
                if self.first_city.tech_level >= 4:
                    is_addable = True

            if is_addable:
                self.union_score += TrainUnitCost[union_action[1]]
                self.first_city.reaction(union_action)
        else:
            self.first_city.reaction(union_action)

        if union_action[0] == "throw unit":
                self.union_score += ThrowUnitCost

        order_action = self.NN_Order.reaction(info[0])
        if order_action[0] == "add unit":
            is_addable = False
            if order_action[1] == LightInfantryType:
                is_addable = True
            elif order_action[1] == HeavyInfantryType:
                if self.second_city.tech_level >= 1:
                    is_addable = True
            elif order_action[1] == CavalryType:
                if self.second_city.tech_level >= 2:
                    is_addable = True
            elif order_action[1] == LongDistanceSoldierType:
                if self.second_city.tech_level >= 3:
                    is_addable = True
            elif order_action[1] == HealerType:
                if self.second_city.tech_level >= 4:
                    is_addable = True

            if is_addable:
                self.order_score += TrainUnitCost[order_action[1]]
                self.second_city.reaction(order_action)
        else:
            self.second_city.reaction(order_action)

        if order_action[0] == "throw unit":
            self.order_score += ThrowUnitCost

        self.first_city.update(self)
        self.second_city.update(self)

        curr_union_life = [self.first_city.life, self.first_city.Districts[0].life, self.first_city.Districts[1].life,
                           self.first_city.Districts[2].life]
        curr_order_life = [self.second_city.life, self.second_city.Districts[0].life,
                           self.second_city.Districts[1].life, self.second_city.Districts[2].life]

        for i in range(4):
            if prev_order_life[i] - curr_order_life[i] > 0:
                self.union_score += DamageCost[i] * (prev_order_life[i] - curr_order_life[i])
        for i in range(4):
            if prev_union_life[i] - curr_union_life[i] > 0:
                self.order_score += DamageCost[i] * (prev_union_life[i] - curr_union_life[i])

    def info_parameters(self):
        union_info = []
        for i in range(70):
            union_info.append(0)
        for unit in self.first_city.Units:
            if unit.coord[0] == "left":
                union_info[5 * unit.coord[1] + UnitNumber[unit.type]] += 1
            elif unit.coord[0] == "right":
                union_info[5 * (unit.coord[1] + 4) + UnitNumber[unit.type]] += 1
            elif unit.coord[0] == "battle_pole":
                union_info[15 + UnitNumber[unit.type]] += 1
        for unit in self.second_city.Units:
            if unit.coord[0] == "left":
                union_info[5 * (unit.coord[1] + 7) + UnitNumber[unit.type]] += 1
            elif unit.coord[0] == "right":
                union_info[5 * (unit.coord[1] + 11) + UnitNumber[unit.type]] += 1
            elif unit.coord[0] == "battle_pole":
                union_info[50 + UnitNumber[unit.type]] += 1

        union_info.append(self.first_city.life / 1000.0)
        for i in range(3):
            union_info.append(self.first_city.Districts[i].life / 1000.0)

        union_info.append(self.second_city.life / 1000.0)
        for i in range(3):
            union_info.append(self.second_city.Districts[i].life / 1000.0)

        union_info.append(len(self.first_city.Buffered_Units))

        union_info.append(self.first_city.money / 1000.0)
        union_info.append(self.first_city.tech_level / 10)

        union_info = np.array(union_info, dtype=float)

        order_info = []
        for i in range(70):
            order_info.append(0)
        for unit in self.second_city.Units:
            if unit.coord[0] == "right":
                order_info[5 * unit.coord[1] + UnitNumber[unit.type]] += 1
            elif unit.coord[0] == "left":
                order_info[5 * (unit.coord[1] + 4) + UnitNumber[unit.type]] += 1
            elif unit.coord[0] == "battle_pole":
                order_info[15 + UnitNumber[unit.type]] += 1
        for unit in self.second_city.Units:
            if unit.coord[0] == "right":
                order_info[5 * (unit.coord[1] + 7) + UnitNumber[unit.type]] += 1
            elif unit.coord[0] == "left":
                order_info[5 * (unit.coord[1] + 11) + UnitNumber[unit.type]] += 1
            elif unit.coord[0] == "battle_pole":
                order_info[50 + UnitNumber[unit.type]] += 1

        order_info.append(self.second_city.life / 1000.0)
        for i in range(3):
            order_info.append(self.second_city.Districts[i].life / 1000.0)

        order_info.append(self.first_city.life / 1000.0)
        for i in range(3):
            order_info.append(self.first_city.Districts[i].life / 1000.0)

        order_info.append(len(self.second_city.Buffered_Units) / 1000.0)

        order_info.append(self.second_city.money / 1000.0)
        order_info.append(self.second_city.tech_level / 1000.0)

        order_info = np.array(order_info, dtype=float)

        return union_info, order_info