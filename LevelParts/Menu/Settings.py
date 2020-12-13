from LevelParts.Menu.Button import *
from Const.Menus import *
from Const.Level import *
from Draws.MenuDraws import *

class Settings:
    """

    Class of Settings

    :field screen: Surface where self is rendered
    :field Return: Button Return
    :field Easy: Button Easy
    :field Normal: Button Normal
    :field Hard: Button Hard
    :field FirstPlayerType: First player type button
    :field SecondPlayerType: Second player type button
    :field returned: Place, where we will go after returning

    """

    def __init__(self, screen):
        self.Return = Button(BLC, int((SettingsXSize / 2 - SettingsReturnXSize / 2) * DrawingCoefficient),
                             int((SettingsYSize*0.7 - SettingsReturnYSize / 2) * DrawingCoefficient),
                             int(SettingsReturnXSize * DrawingCoefficient),
                             int(SettingsReturnYSize * DrawingCoefficient), 10, "Return", WHT)
        self.Easy = Button(BLC, int((SettingsXSize*0.3 - SettingsEasyXSize / 2) * DrawingCoefficient),
                             int((SettingsYSize*0.3 - SettingsEasyYSize / 2) * DrawingCoefficient),
                             int(SettingsEasyXSize * DrawingCoefficient),
                             int(SettingsEasyYSize * DrawingCoefficient), 10, "Easy", WHT, RED)
        self.Normal = Button(BLC, int((SettingsXSize*0.5 - SettingsNormalXSize / 2) * DrawingCoefficient),
                             int((SettingsYSize*0.3 - SettingsNormalYSize / 2) * DrawingCoefficient),
                             int(SettingsNormalXSize * DrawingCoefficient),
                             int(SettingsNormalYSize * DrawingCoefficient), 10, "Normal", WHT, RED)
        self.Hard = Button(BLC, int((SettingsXSize*0.7 - SettingsHardXSize / 2) * DrawingCoefficient),
                             int((SettingsYSize*0.3 - SettingsHardYSize / 2) * DrawingCoefficient),
                             int(SettingsHardXSize * DrawingCoefficient),
                             int(SettingsHardYSize * DrawingCoefficient), 10, "Hard", WHT, RED)
        self.FirstPlayerType = Button(BLC, int((SettingsXSize*0.33 - SettingsFirstPlayerTypeXSize / 2) *
                                               DrawingCoefficient),
                                      int((SettingsYSize*0.5 - SettingsFirstPlayerTypeYSize / 2) *
                                          DrawingCoefficient), int(SettingsFirstPlayerTypeXSize * DrawingCoefficient),
                                      int(SettingsFirstPlayerTypeYSize * DrawingCoefficient), 10, "Player", WHT)
        self.SecondPlayerType = Button(BLC, int((SettingsXSize*0.66 - SettingsSecondPlayerTypeXSize / 2) *
                                               DrawingCoefficient),
                                      int((SettingsYSize*0.5 - SettingsSecondPlayerTypeYSize / 2) *
                                          DrawingCoefficient), int(SettingsSecondPlayerTypeXSize * DrawingCoefficient),
                                      int(SettingsSecondPlayerTypeYSize * DrawingCoefficient), 10, "Player", WHT)
        self.screen = screen
        self.Easy.chosen = True
        self.returned = "main"

    def update(self):

        draw_settings(self.screen)
        self.Return.draw_button(self.screen)
        self.Easy.draw_button(self.screen)
        self.Normal.draw_button(self.screen)
        self.Hard.draw_button(self.screen)
        self.FirstPlayerType.draw_button(self.screen)
        self.SecondPlayerType.draw_button(self.screen)

    def game_event(self, event):
        answer = ""
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = ((event.pos[0] * 1.0) / (DrawingCoefficient * 1.0), (event.pos[1] * 1.0) / (DrawingCoefficient * 1.0))
            if self.Return.is_pressed(pos):
                if self.returned == "main":
                    answer = "main menu"
                elif self.returned == "pause":
                    answer = "return pause"
            elif self.Easy.is_pressed(pos):
                answer = "easy bots"
                self.Easy.chosen = True
                self.Normal.chosen = False
                self.Hard.chosen = False
            elif self.Normal.is_pressed(pos):
                answer = "normal bots"
                self.Easy.chosen = False
                self.Normal.chosen = True
                self.Hard.chosen = False
            elif self.Hard.is_pressed(pos):
                answer = "hard bots"
                self.Easy.chosen = False
                self.Normal.chosen = False
                self.Hard.chosen = True
            elif self.FirstPlayerType.is_pressed(pos):
                if self.FirstPlayerType.text == "Player":
                    self.FirstPlayerType.text = "Bot"
                    answer = "first bot"
                else:
                    self.FirstPlayerType.text = "Player"
                    answer = "first player"
            elif self.SecondPlayerType.is_pressed(pos):
                if self.SecondPlayerType.text == "Player":
                    self.SecondPlayerType.text = "Bot"
                    answer = "second bot"
                else:
                    self.SecondPlayerType.text = "Player"
                    answer = "second player"
        print(answer)
        return answer


if __name__ == "__main__":
    print("This module is not for direct call!")
