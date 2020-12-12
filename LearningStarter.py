from random import random
from Widgets.MashineLearning.LearningLevel import *
import time




def fake_image_import():
    union_unit_types = [LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, AlchemistType]
    order_unit_types = [LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, HealerType]

    Another_Images = {}
    Another_Images["castle union"] = 0
    Another_Images["square"] = 0
    Another_Images["castle order"] = 0
    Another_Images["bruschatka"] = 0

    Union_Units_Images = {}
    for unit_type in union_unit_types:
        Union_Units_Images[unit_type] = {}

    Order_Units_Images = {}
    for unit_type in order_unit_types:
        Order_Units_Images[unit_type] = {}

    return Another_Images, Union_Units_Images, Order_Units_Images


def input_Neural_Network(file_name):
    file_obj = open(file_name, 'r')
    matrix = []
    shift = []
    for i in range(len(NNLayers)-1):
        matrix.append(np.zeros((NNLayers[i + 1], NNLayers[i]), dtype=float))
        for j in range(NNLayers[i+1]):
            for k in range(NNLayers[i]):
                matrix[i][j][k] = float(file_obj.readline())
    for i in range(len(NNLayers)-1):
        shift.append(np.zeros((NNLayers[i + 1],), dtype=float))
        for j in range(NNLayers[i+1]):
            shift[i][j] = float(file_obj.readline())
    file_obj.close()
    return matrix, shift


def output_Neural_Network(NN, file_name):
    matrix = NN[0]
    shift = NN[1]
    file_obj = open(file_name, "w")
    for i in range(len(NNLayers)-1):
        for j in range(NNLayers[i+1]):
            for k in range(NNLayers[i]):
                file_obj.write(str(matrix[i][j][k]) + '\n')
    for i in range(len(NNLayers)-1):
        for j in range(NNLayers[i+1]):
            file_obj.write(str(shift[i][j]) + '\n')
    file_obj.close()


def learning_iteration(learning_rate, union_parents, order_parents):


    Fake_Images = fake_image_import()
    # скрещивание / генерация нового поколения / рандомизация
    order_childs = []
    union_childs = []
    for k in range(ChildsNumber-ParentsNumber):
        matrix = []
        shift = []
        for i in range(len(NNLayers)-1):
            matrix.append(np.zeros((NNLayers[i + 1], NNLayers[i]), dtype=float))
        for i in range(len(NNLayers) - 1):
            shift.append(np.zeros((NNLayers[i + 1],), dtype=float))

        shares = generate_shares(ParentsNumber)

        for i in range(len(NNLayers) - 1):
            for j in range(ParentsNumber):
                matrix[i] = matrix[i] + shares[j] * order_parents[j][0][i]
                shift[i] = shift[i] + shares[j] * order_parents[j][1][i]
            matrix[i] = matrix[i] + learning_rate*(2.0*np.random.sample((NNLayers[i + 1], NNLayers[i])) -
                                           np.ones((NNLayers[i + 1], NNLayers[i]), dtype=float))
            shift[i] = shift[i] + learning_rate * (2.0 * np.random.sample((NNLayers[i + 1],))
                                                   - np.ones((NNLayers[i + 1],)))

        order_childs.append([matrix, shift])

    for i in range(ParentsNumber):
        order_childs.append(order_parents[i])

    for i in range(ParentsNumber):
        union_childs.append(union_parents[i])

    for k in range(ChildsNumber-ParentsNumber):
        matrix = []
        shift = []
        for i in range(len(NNLayers)-1):
            matrix.append(np.zeros((NNLayers[i + 1], NNLayers[i]), dtype=float))
        for i in range(len(NNLayers) - 1):
            shift.append(np.zeros((NNLayers[i + 1],), dtype=float))

        shares = generate_shares(ParentsNumber)

        for i in range(len(NNLayers) - 1):
            for j in range(ParentsNumber):
                matrix[i] = matrix[i] + shares[j] * union_parents[j][0][i]
                shift[i] = shift[i] + shares[j] * union_parents[j][1][i]
            matrix[i] = matrix[i] + learning_rate * (2.0 * np.random.sample((NNLayers[i + 1], NNLayers[i])) -
                                                     np.ones((NNLayers[i + 1], NNLayers[i]), dtype=float))
            shift[i] = shift[i] + learning_rate * (2.0 * np.random.sample((NNLayers[i + 1],))
                                                   - np.ones((NNLayers[i + 1],)))

        union_childs.append([matrix, shift])


    # оценка поколения

    order_results = []
    union_results = []
    for i in range(ChildsNumber):
        union_NN = NeuralNetwork(union_childs[i], "union")
        order_NN = NeuralNetwork(order_childs[i], "order")
        learning_level = LearningLevel("Widgets/MapEditor/map2.txt", Fake_Images, order_NN, union_NN)
        union_score, order_score = learning_level.game()
        order_results.append(order_score)
        union_results.append(union_score)

    # сортировка поколения / пузырьком

    for i in range(ChildsNumber-1):
        for j in range(ChildsNumber-1, i-1, -1):
            if order_results[j] > order_results[j-1]:
                order_results[j], order_results[j-1] = order_results[j-1], order_results[j]
                order_childs[j], order_childs[j-1] = order_childs[j-1], order_childs[j]

    for i in range(ChildsNumber-1):
        for j in range(ChildsNumber-1, i-1, -1):
            if union_results[j] > union_results[j-1]:
                union_results[j], union_results[j-1] = union_results[j-1], union_results[j]
                union_childs[j], union_childs[j-1] = union_childs[j-1], union_childs[j]

    # генерация будущих родителей

    new_order_parents = []
    new_union_parents = []
    for i in range(ParentsNumber):
        new_union_parents.append(union_childs[i])
        new_order_parents.append(order_childs[i])

    return new_union_parents, new_order_parents, union_results[0], order_results[0]


def generate_shares(number):
    shares = []
    collected = 0.0
    for i in range(number-1):
        new_share = random()*(1.0-collected)
        collected += new_share
        shares.append(new_share)
    shares.append(1.0-collected)
    return shares


def generate_random_parents():
    order_parents = []
    union_parents = []
    for i in range(ParentsNumber):
        matrix = []
        shift = []
        for i in range(len(NNLayers) - 1):
            matrix.append(StartRate*(2.0 * np.random.sample((NNLayers[i + 1], NNLayers[i]))
                                                   - np.ones((NNLayers[i + 1], NNLayers[i]))))
        for i in range(len(NNLayers) - 1):
            shift.append(StartRate*(2.0 * np.random.sample((NNLayers[i + 1],))
                                                   - np.ones((NNLayers[i + 1],))))
        order_parents.append([matrix, shift])
    for i in range(ParentsNumber):
        matrix = []
        shift = []
        for i in range(len(NNLayers) - 1):
            matrix.append(StartRate * (2.0 * np.random.sample((NNLayers[i + 1], NNLayers[i]))
                                       - np.ones((NNLayers[i + 1], NNLayers[i]))))
        for i in range(len(NNLayers) - 1):
            shift.append(StartRate * (2.0 * np.random.sample((NNLayers[i + 1],))
                                      - np.ones((NNLayers[i + 1],))))
        union_parents.append([matrix, shift])
    return order_parents, union_parents

union_parents, order_parents = generate_random_parents()

number = 0
file_name = "Widgets/MashineLearning/differentAI/" + "UnionNN" + str(number) + ".txt"
output_Neural_Network(union_parents[0], file_name)
file_name = "Widgets/MashineLearning/differentAI/" + "OrderNN" + str(number) + ".txt"
output_Neural_Network(order_parents[0], file_name)
while True:
    number += 1
    start_time = time.process_time()
    union_parents, order_parents, union_result, order_result = learning_iteration(LearningRate, union_parents, order_parents)
    end_time = time.process_time()
    print("-----------")
    print(" ")
    print("Generation: " + str(number))
    it_time = (end_time - start_time)
    print("Time: " + str(it_time))
    print(" ")
    print("-----------")
    file_obj = open("Widgets/MashineLearning/differentAI/results1.txt", 'a')
    file_obj.write(str(union_result) + "\n")
    file_obj.write(str(order_result) + "\n")
    file_obj.close()
    if number % 10 == 0:
        file_name = "Widgets/MashineLearning/differentAI/" + "UnionNN" + str(number) + ".txt"
        output_Neural_Network(union_parents[0], file_name)
        file_name = "Widgets/MashineLearning/differentAI/" + "OrderNN" + str(number) + ".txt"
        output_Neural_Network(order_parents[0], file_name)
        print("Saved")
