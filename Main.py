from Game import *
"""

Do the whole program

"""
# Импорт нейросети


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


# файл запуска программы


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


EasyNN = ["Widgets/MashineLearning/differentAI/UnionNN1750.txt", "Widgets/MashineLearning/differentAI/OrderNN1750.txt"]
test_game = Game(EasyNN, EasyNN, EasyNN)

while not test_game.finished:
    test_game.update()
    for event in pygame.event.get():
        test_game.game_event(event)
pygame.quit()

