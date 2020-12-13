from LevelParts.Menu.Button import *
from Const.Menus import *
from Const.Level import *

class MainMenu:
    """

    Class of Main Menu

    :field screen: Surface where self is rendered
    :field Start: Button Start
    :field SettingsButton: Button Settings

    """

    def __init__(self, screen):
        self.Start = Button(BLC, int((MainMenuXSize / 2 - MainStartXSize / 2) * DrawingCoefficient),
                             int((MainMenuYSize*0.33 - MainStartYSize / 2) * DrawingCoefficient),
                             int(MainStartXSize * DrawingCoefficient),
                             int(MainStartYSize * DrawingCoefficient), 10, "Start", WHT)
        self.SettingsButton = Button(BLC, int((MainMenuXSize / 2 - MainSettingsXSize / 2) * DrawingCoefficient),
                             int((MainMenuYSize*0.66 - MainSettingsYSize / 2) * DrawingCoefficient),
                             int(MainSettingsXSize * DrawingCoefficient),
                             int(MainSettingsYSize * DrawingCoefficient), 10, "Settings", WHT)
        self.screen = screen

    def update(self):
        pygame.draw.rect(self.screen, WHT, self.screen.get_rect())
        self.Start.draw_button(self.screen)
        self.SettingsButton.draw_button(self.screen)

    def game_event(self, event):
        answer = ""
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = ((event.pos[0] * 1.0) / (DrawingCoefficient * 1.0), (event.pos[1] * 1.0) / (DrawingCoefficient * 1.0))
            if self.Start.is_pressed(pos):
                answer = "start"
            elif self.SettingsButton.is_pressed(pos):
                answer = "main settings"

        return answer


if __name__ == "__main__":
    print("This module is not for direct call!")
