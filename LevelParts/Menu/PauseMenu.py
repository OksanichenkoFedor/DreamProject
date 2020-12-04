from LevelParts.Menu.Button import *
from Const.Menus import *
from Const.Level import *

class PauseMenu:
    # TODO Создать работающее главное меню
    def __init__(self, screen):
        self.Resume = Button(BLC, int((PauseMenuXSize/2-PauseResumeXSize/2)*DrawingCoefficient),
                             int((PauseMenuYSize/2-PauseResumeYSize/2)*DrawingCoefficient),
                             int(PauseResumeXSize*DrawingCoefficient),
                             int(PauseResumeYSize*DrawingCoefficient), 10, "Resume", WHT)
        self.screen = screen

    def update(self):
        pygame.draw.rect(self.screen, BLC, self.screen.get_rect(),100)
        self.Resume.update_button(self.screen)


    def game_event(self, event):
        answer = ""
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = ((event.pos[0] * 1.0) / (DrawingCoefficient * 1.0), (event.pos[1] * 1.0) / (DrawingCoefficient * 1.0))
            if self.Resume.is_pressed(pos):
                answer = "resume"

        return answer

if __name__ == "__main__":
    print("This module is not for direct call!")
