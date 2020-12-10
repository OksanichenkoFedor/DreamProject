from Const.MashineLearning import *
import numpy as np


class NeuralNetwork():
    """

    Class of neural network

    : field matrix: Massive of matrices of NN
    : field shift: Massive of shifts
    : field unit_types: Dictionary of unit numbers and types

    : method reaction: Using CityInfo generate action

    """
    def __init__(self, NN, side):
        self.matrix = NN[0]
        self.shift = NN[1]
        self.unit_types = 0
        if side == "union":
            self.unit_types = UnitTypeUnion
        else:
            self.unit_types = UnitTypeOrder

    def reaction(self, city_info):
        for i in range(len(NNLayers)-1):
            city_info = np.dot(self.matrix[i], city_info) + self.shift[i]
            city_info = self.activation_function(NNFunctions[i], city_info)


        Anwser = city_info
        add_unit = 0
        z = Anwser[0][0]
        for i in range(5):
            if z < Anwser[i+1][0]:
                add_unit = i + 1
                z = Anwser[i+1][0]
        if add_unit != 0:
            return ["add unit", self.unit_types[add_unit-1]]
        throw_unit = 6
        z = Anwser[6][0]
        for i in range(3):
            if z < Anwser[i+7][0]:
                throw_unit = i + 7
                z = Anwser[i+7][0]
        if throw_unit != 6:
            road = throw_unit - 7
            return ["throw unit", road]
        z = Anwser[10][0]
        new_master = 1
        if z > 0.5:
            new_master = 2
        elif z < -0.5:
            new_master = 0
        return ["master change", new_master]

    def activation_function(self, function, vector):
        if function == ReluF:
            return np.array([u if u[0] > 0 else [0] for u in vector])
        elif function == Tanh:
            return np.tanh(vector)
        else:
            return False

