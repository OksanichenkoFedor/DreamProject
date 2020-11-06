import pygame

# файл запуска программы
pygame.init()
screen = pygame.display.set_mode((int(800), int(800)))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
flag = False

while not finished:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
