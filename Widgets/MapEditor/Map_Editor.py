import pygame
from Const.Level import *
from pygame.draw import *

# файл запуска программы
pygame.init()
screen = pygame.display.set_mode((MapXSize, MapYSize))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
flag = False
LeftRoads = [[]]
RightRoads = [[]]
NumLRd = 0
NumRRd = 0
SideIndex = "left"
screen.fill(WHT)

while not finished:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if SideIndex == "left":
                    LeftRoads[NumLRd].append(event.pos)
                    circle(screen, (0, int(255 * (1.0 * NumberOfRoads - 1.0 * NumLRd) / (1.0 * NumberOfRoads)),
                                    int(255 * (1.0 * NumLRd + 1.0) / (1.0 * NumberOfRoads))),
                           [event.pos[0], event.pos[1]], 2)
                else:
                    RightRoads[NumRRd].append(event.pos)
                    circle(screen, (int(255 * (1.0 * NumberOfRoads - 1.0 * NumRRd) / (1.0 * NumberOfRoads)),
                                    int(255 * (1.0 * NumRRd + 1.0) / (1.0 * NumberOfRoads)), 0),
                           [event.pos[0], event.pos[1]], 2)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("2121")
                if NumLRd < NumberOfRoads - 1:
                    NumLRd = NumLRd + 1
                    LeftRoads.append([])
                elif NumRRd < NumberOfRoads - 1:
                    if SideIndex == "left":
                        SideIndex = "right"
                    else:
                        NumRRd = NumRRd + 1
                    RightRoads.append([])
                else:
                    finished = True
        elif event.type == pygame.QUIT:
            finished = True
# запись в файл
map_file_name = "map2.txt"
file_obj = open(map_file_name, 'w')
file_obj.write(str(NumLRd+1) + '\n')
file_obj.write(str(NumRRd+1) + '\n')
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
file_obj.close()

pygame.quit()
