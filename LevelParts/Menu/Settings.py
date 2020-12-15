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
                             int((SettingsYSize*0.8 - SettingsReturnYSize / 2) * DrawingCoefficient),
                             int(SettingsReturnXSize * DrawingCoefficient),
                             int(SettingsReturnYSize * DrawingCoefficient), 10, "Return", WHT)
        self.Easy = Button(BLC, int((SettingsXSize*0.34 - SettingsEasyXSize / 2) * DrawingCoefficient),
                             int((SettingsYSize*0.2 - SettingsEasyYSize / 2) * DrawingCoefficient),
                             int(SettingsEasyXSize * DrawingCoefficient),
                             int(SettingsEasyYSize * DrawingCoefficient), 10, "Easy", WHT, RED)
        self.Normal = Button(BLC, int((SettingsXSize*0.5 - SettingsNormalXSize / 2) * DrawingCoefficient),
                             int((SettingsYSize*0.2 - SettingsNormalYSize / 2) * DrawingCoefficient),
                             int(SettingsNormalXSize * DrawingCoefficient),
                             int(SettingsNormalYSize * DrawingCoefficient), 10, "Normal", WHT, RED)
        self.Hard = Button(BLC, int((SettingsXSize*0.66 - SettingsHardXSize / 2) * DrawingCoefficient),
                             int((SettingsYSize*0.2 - SettingsHardYSize / 2) * DrawingCoefficient),
                             int(SettingsHardXSize * DrawingCoefficient),
                             int(SettingsHardYSize * DrawingCoefficient), 10, "Hard", WHT, RED)
        self.FirstPlayerTypeAI = Button(BLC, int((SettingsXSize*0.43 - SettingsFirstPlayerTypeXSize / 2) *
                                               DrawingCoefficient),
                                      int((SettingsYSize*0.50 - SettingsFirstPlayerTypeYSize / 2) *
                                          DrawingCoefficient), int(SettingsFirstPlayerTypeXSize * DrawingCoefficient),
                                      int(SettingsFirstPlayerTypeYSize * DrawingCoefficient), 10, "Player", WHT)
        self.SecondPlayerTypeAI = Button(BLC, int((SettingsXSize*0.57 - SettingsSecondPlayerTypeXSize / 2) *
                                               DrawingCoefficient),
                                      int((SettingsYSize*0.50 - SettingsSecondPlayerTypeYSize / 2) *
                                          DrawingCoefficient), int(SettingsSecondPlayerTypeXSize * DrawingCoefficient),
                                      int(SettingsSecondPlayerTypeYSize * DrawingCoefficient), 10, "Player", WHT)
        self.FirstPlayerTypeSide = Button(BLC, int((SettingsXSize * 0.43 - SettingsFirstPlayerTypeXSize / 2) *
                                                 DrawingCoefficient),
                                        int((SettingsYSize * 0.6 - SettingsFirstPlayerTypeYSize / 2) *
                                            DrawingCoefficient), int(SettingsFirstPlayerTypeXSize * DrawingCoefficient),
                                        int(SettingsFirstPlayerTypeYSize * DrawingCoefficient), 10, "Union", GRN)
        self.SecondPlayerTypeSide = Button(BLC, int((SettingsXSize * 0.57 - SettingsSecondPlayerTypeXSize / 2) *
                                                  DrawingCoefficient),
                                         int((SettingsYSize * 0.6 - SettingsSecondPlayerTypeYSize / 2) *
                                             DrawingCoefficient),
                                         int(SettingsSecondPlayerTypeXSize * DrawingCoefficient),
                                         int(SettingsSecondPlayerTypeYSize * DrawingCoefficient), 10, "Order", RED)
        self.screen = screen
        self.Easy.chosen = True
        self.returned = "main"

    def update(self):

        draw_settings(self.screen)
        self.Return.draw_button(self.screen)
        self.Easy.draw_button(self.screen)
        self.Normal.draw_button(self.screen)
        self.Hard.draw_button(self.screen)
        self.FirstPlayerTypeAI.draw_button(self.screen)
        self.SecondPlayerTypeAI.draw_button(self.screen)
        self.FirstPlayerTypeSide.draw_button(self.screen)
        self.SecondPlayerTypeSide.draw_button(self.screen)

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
            elif self.FirstPlayerTypeAI.is_pressed(pos):
                if self.FirstPlayerTypeAI.text == "Player":
                    self.FirstPlayerTypeAI.text = "Bot"
                    answer = "first bot"
                else:
                    self.FirstPlayerTypeAI.text = "Player"
                    answer = "first player"
            elif self.SecondPlayerTypeAI.is_pressed(pos):
                if self.SecondPlayerTypeAI.text == "Player":
                    self.SecondPlayerTypeAI.text = "Bot"
                    answer = "second bot"
                else:
                    self.SecondPlayerTypeAI.text = "Player"
                    answer = "second player"
            elif self.FirstPlayerTypeSide.is_pressed(pos):
                if self.FirstPlayerTypeSide.text == "Order":
                    self.FirstPlayerTypeSide.text = "Union"
                    self.FirstPlayerTypeSide.text_color = GRN
                    answer = "first union"
                else:
                    self.FirstPlayerTypeSide.text = "Order"
                    self.FirstPlayerTypeSide.text_color = RED
                    answer = "first order"
            elif self.SecondPlayerTypeSide.is_pressed(pos):
                if self.SecondPlayerTypeSide.text == "Order":
                    self.SecondPlayerTypeSide.text = "Union"
                    self.SecondPlayerTypeSide.text_color = GRN
                    answer = "second union"
                else:
                    self.SecondPlayerTypeSide.text = "Order"
                    self.SecondPlayerTypeSide.text_color = RED
                    answer = "second order"
        return answer


if __name__ == "__main__":
    print("This module is not for direct call!")
