from LevelParts.Menu.Button import *
from Const.Menus import *
from Const.Level import *

class MainMenu:
    # TODO Создать работающее главное меню
    def __init__(self, screen):
        self.Start = Button(BLC, MainMenuXSize/2, MainMenuYSize/2, 100, 75, 10, "Start", WHT)
        self.screen = screen

    def update(self):
        self.Start.update_button(self.screen)

    def game_event(self, event):
        answer = ""
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = ((event.pos[0] * 1.0) / (DrawingCoefficient * 1.0), (event.pos[1] * 1.0) / (DrawingCoefficient * 1.0))
            if self.Start.is_pressed(pos):
                answer = "resume"

        return answer


if __name__ == "__main__":
    print("This module is not for direct call!")
