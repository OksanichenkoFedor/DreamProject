from LevelParts.Menu.Button import *
from Const.Menus import *
from Const.Level import *

class PauseMenu:
    """

    """

    def __init__(self, screen):
        self.Resume = Button(BLC, int((PauseMenuXSize/2-PauseResumeXSize/2)*DrawingCoefficient),
                             int((PauseMenuYSize*0.3-PauseResumeYSize/2)*DrawingCoefficient),
                             int(PauseResumeXSize*DrawingCoefficient),
                             int(PauseResumeYSize*DrawingCoefficient), 0, "Resume", WHT)
        self.Restart = Button(BLC, int((PauseMenuXSize / 2 - PauseRestartXSize / 2) * DrawingCoefficient),
                             int((PauseMenuYSize*0.5 - PauseRestartYSize / 2) * DrawingCoefficient),
                             int(PauseRestartXSize * DrawingCoefficient),
                             int(PauseRestartYSize * DrawingCoefficient), 0, "Restart", WHT)
        self.SettingsButton = Button(BLC, int((PauseMenuXSize / 2 - PauseSettingsXSize / 2) * DrawingCoefficient),
                              int((PauseMenuYSize * 0.7 - PauseSettingsYSize / 2) * DrawingCoefficient),
                              int(PauseSettingsXSize * DrawingCoefficient),
                              int(PauseSettingsYSize * DrawingCoefficient), 0, "Settings", WHT)
        self.screen = screen

    def update(self):
        pygame.draw.rect(self.screen, BLC, self.screen.get_rect(), 100)
        self.Resume.draw_button(self.screen)
        self.Restart.draw_button(self.screen)
        self.SettingsButton.draw_button(self.screen)


    def game_event(self, event):
        answer = ""
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = ((event.pos[0] * 1.0) / (DrawingCoefficient * 1.0), (event.pos[1] * 1.0) / (DrawingCoefficient * 1.0))
            if self.Resume.is_pressed(pos):
                answer = "resume"
            elif self.Restart.is_pressed(pos):
                answer = "start"
            elif self.SettingsButton.is_pressed(pos):
                answer = "pause settings"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                answer = "resume"
        return answer

if __name__ == "__main__":
    print("This module is not for direct call!")
