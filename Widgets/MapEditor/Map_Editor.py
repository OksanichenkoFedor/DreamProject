import pygame
from Const.Level import *
from pygame.draw import *

"""

Это виджет создания карты

Сначала он создаёт левые дороги набором пар координат узлов (дороги делате сверху вниз)
Потом так же правые (так же, дороги делайте сверху вниз)
Переключение между дорогами происходит по нажатию клавиши "Пробел"
После этого создаётся полигон поля боя. Он состоит из:
 1. Набора последних узлов левых улиц
 2. Вводимого набора точек (это точки которые будут лежать "около 6 часов" нашего полигона, вводить против часовой )
 3. Инвертированного набора последних узлов правых улиц
 4. Вводимого набора точек (это точки которые будут лежать "около 12 часов" нашего полигона, вводить против часовой)
После этого все значения вводятся в .txt файл по одному числу на строку в следующем порядке:
 1. Количество левых дорог
 2. Количество правых дорог
 3. Набор левых дорог
   a.) Количество узлов у дороги
   b.) Набор узлов левой дороги (первая строчка x координата, вторая точка y координата)
 4. Набор правых дорог
   a.) Количество узлов у дороги
   b.) Набор узлов (первая строчка x координата, вторая точка y координата)
 5. Первый набор точек полигона
   a.) Количество точек у набора
   b.) Набор точек (первая строчка x координата, вторая точка y координата)
 6. Второй набор точек полигона
   a.) Количество точек у набора
   b.) Набор точек (первая строчка x координата, вторая точка y координата)

Пользуйтесь на здоровье!!!
"""


def minrad(a, b, r):
    """

    :param a: Tuple, which contains coordinates of first point
    :param b: Tuple, which contains coordinates of second point
    :param r: Radius, that we check
    :return: Boolean, which is:
                               1.) True, if distance between a and b is not less, than r.
                               2.) False, if distance between a and b is less, than r.

    """
    if (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 < r * r:
        return False
    else:
        return True


pygame.init()
screen = pygame.display.set_mode((MapXSize, MapYSize))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
flag = False
LeftRoads = [[]]
RightRoads = [[]]
DownPolygon = []
UpPolygon = []
NumLRd = 0
NumRRd = 0
SideIndex = "left"
minimum_dist = 8
screen.fill(WHT)
ButtonDown = False
while not finished:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                ButtonDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            ButtonDown = False
        elif ButtonDown:
            if SideIndex == "left":
                if len(LeftRoads[NumLRd]) == 0:
                    LeftRoads[NumLRd].append(event.pos)
                    circle(screen, (0, int(255 * (1.0 * NumberOfRoads - 1.0 * NumLRd) / (1.0 * NumberOfRoads)),
                                    int(255 * (1.0 * NumLRd + 1.0) / (1.0 * NumberOfRoads))),
                           [event.pos[0], event.pos[1]], 2)
                elif minrad(LeftRoads[NumLRd][len(LeftRoads[NumLRd]) - 1], event.pos, minimum_dist):
                    LeftRoads[NumLRd].append(event.pos)
                    circle(screen, (0, int(255 * (1.0 * NumberOfRoads - 1.0 * NumLRd) / (1.0 * NumberOfRoads)),
                                    int(255 * (1.0 * NumLRd + 1.0) / (1.0 * NumberOfRoads))),
                           [event.pos[0], event.pos[1]], 2)
            elif SideIndex == "right":
                if len(RightRoads[NumRRd]) == 0:
                    RightRoads[NumRRd].append(event.pos)
                    circle(screen, (int(255 * (1.0 * NumberOfRoads - 1.0 * NumRRd) / (1.0 * NumberOfRoads)),
                                    int(255 * (1.0 * NumRRd + 1.0) / (1.0 * NumberOfRoads)), 0),
                           [event.pos[0], event.pos[1]], 2)
                elif minrad(RightRoads[NumRRd][len(RightRoads[NumRRd]) - 1], event.pos, minimum_dist):
                    RightRoads[NumRRd].append(event.pos)
                    circle(screen, (int(255 * (1.0 * NumberOfRoads - 1.0 * NumRRd) / (1.0 * NumberOfRoads)),
                                    int(255 * (1.0 * NumRRd + 1.0) / (1.0 * NumberOfRoads)), 0),
                           [event.pos[0], event.pos[1]], 2)
            elif SideIndex == "down":
                if len(DownPolygon) == 0:
                    DownPolygon.append(event.pos)
                    circle(screen, BLC, [event.pos[0], event.pos[1]], 2)
                elif minrad(DownPolygon[len(DownPolygon) - 1], event.pos, minimum_dist):
                    DownPolygon.append(event.pos)
                    circle(screen, BLC, [event.pos[0], event.pos[1]], 2)
            else:
                if len(UpPolygon) == 0:
                    UpPolygon.append(event.pos)
                    circle(screen, BLC, [event.pos[0], event.pos[1]], 2)
                elif minrad(UpPolygon[len(UpPolygon) - 1], event.pos, minimum_dist):
                    UpPolygon.append(event.pos)
                    circle(screen, BLC, [event.pos[0], event.pos[1]], 2)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space")
                if NumLRd < NumberOfRoads:
                    NumLRd = NumLRd + 1
                    if NumLRd < NumberOfRoads:
                        LeftRoads.append([])
                    else:
                        SideIndex = "right"
                elif NumRRd < NumberOfRoads:
                    NumRRd = NumRRd + 1
                    if NumRRd < NumberOfRoads:
                        RightRoads.append([])
                    else:
                        SideIndex = "down"
                elif SideIndex == "down":
                    SideIndex = "up"
                else:
                    finished = True
        elif event.type == pygame.QUIT:
            finished = True
# запись в файл
map_file_name = "map2.txt"
file_obj = open(map_file_name, 'w')
file_obj.write(str(NumLRd) + '\n')
file_obj.write(str(NumRRd) + '\n')
for i in range(len(LeftRoads)):
    file_obj.write(str(len(LeftRoads[i])) + '\n')
    for j in range(len(LeftRoads[i])):
        file_obj.write(str(LeftRoads[i][j][0]) + '\n')
        file_obj.write(str(LeftRoads[i][j][1]) + '\n')
for i in range(len(RightRoads)):
    file_obj.write(str(len(RightRoads[i])) + '\n')
    for j in range(len(RightRoads[i])):
        file_obj.write(str(RightRoads[i][j][0]) + '\n')
        file_obj.write(str(RightRoads[i][j][1]) + '\n')
polygon_points_number = len(LeftRoads) + len(DownPolygon) + len(UpPolygon) + len(RightRoads)
file_obj.write(str(polygon_points_number) + '\n')
for i in range(len(LeftRoads)):
    file_obj.write(str(LeftRoads[i][len(LeftRoads[i]) - 1][0]) + '\n')
    file_obj.write(str(LeftRoads[i][len(LeftRoads[i]) - 1][1]) + '\n')
for i in range(len(DownPolygon)):
    file_obj.write(str(DownPolygon[i][0]) + '\n')
    file_obj.write(str(DownPolygon[i][1]) + '\n')
for i in range(len(RightRoads) - 1, -1, -1):
    file_obj.write(str(RightRoads[i][len(RightRoads[i]) - 1][0]) + '\n')
    file_obj.write(str(RightRoads[i][len(RightRoads[i]) - 1][1]) + '\n')
for i in range(len(UpPolygon)):
    file_obj.write(str(UpPolygon[i][0]) + '\n')
    file_obj.write(str(UpPolygon[i][1]) + '\n')

file_obj.close()

pygame.quit()
