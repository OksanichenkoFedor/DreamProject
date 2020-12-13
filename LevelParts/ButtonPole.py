from Draws.LevelDraws import *
from Const.Level import *
from Draws.LevelDraws import unit_button_draw, button_pole_draw
from LevelParts.Menu.Button import *
from math import pi


class ButtonPole():
    """

    Class of button pole, where units are located

    : field self.Buttons: List of buttons
    : field self.x: First coordinate of button pole
    : field self.y: Second coordinate of button pole
    : field self.chosen: Integer, which contains key of chosen button
    : field self.animation_timer: Time of animation left
    : field self.Training: List of lists, which contains information about training:
                                          1.) Number of unit, which we want to train
                                          2.) Time, left for train
                                          3.) Total time

    """

    def __init__(self, x, y, first):
        self.x = x
        self.y = y
        self.width = ButtonPoleXSize
        self.height = ButtonPoleYSize
        self.Buttons = []
        self.chosen = None
        self.Buttons.append(Button(BLC, self.x + self.width / 2 - ButtonPoleButtonXSize / 2,
                                   self.y + self.height / 2 - ButtonPoleButtonYSize / 2, ButtonPoleButtonXSize,
                                   ButtonPoleButtonYSize, 0, first[1], WHT, RED, first[0]))
        self.Training = []
        self.Cash_Button = []
        self.animation_timer = -1
        self.changeChosen(0)

    def update(self, screen):
        button_pole_draw(screen, self)
        if self.animation_timer > 0:
            self.animation_timer -= 1
            for i in range(len(self.Buttons)):
                y0 = (self.height * 1.0) * ((i + 1) / (len(self.Buttons) + 1.0))
                y1 = (self.height * 1.0) * ((i + 1) / (len(self.Buttons) + 2.0))
                self.Buttons[i].update_button(self.Buttons[i].x, self.y - ButtonPoleButtonYSize / 2 + y1 * 1.0 +
                                              (y0 * 1.0 - y1 * 1.0) * (
                                                          (1.0 * self.animation_timer) / (ButtonAnimationTime * 1.0)))
        elif self.animation_timer == 0:
            self.animation_timer = -1
            self.Buttons.append(self.Cash_Button)
            self.Cash_Button = 0
        if len(self.Training) == 0:
            for button in self.Buttons:
                unit_button_draw(screen, button, 0, button.number)
            if button.number > 0:
                print("Error")
        else:
            for i in range(len(self.Buttons)):
                if i != self.Training[0][0]:
                    unit_button_draw(screen, self.Buttons[i], 0, self.Buttons[i].number)
            j = self.Training[0][0]
            if self.Training[0][1] <= 0:
                self.Training.pop(0)
                self.Buttons[j].number -= 1
                unit_button_draw(screen, self.Buttons[j], 0, self.Buttons[j].number)
            else:
                self.Training[0][1] -= 1
                unit_button_draw(screen, self.Buttons[j],
                                 2.0 * pi * ((1.0 * self.Training[0][1]) / (1.0 * self.Training[0][2])),
                                 self.Buttons[j].number)


    def add_button(self, new):
        """

        Add new button to Cash
        :param new: Massive:
                    First element: Unit type
                    Second element: Button text
        :return:
        """
        self.animation_timer = ButtonAnimationTime
        self.Cash_Button = Button(BLC, self.x + self.width / 2 - ButtonPoleButtonXSize / 2,
                                  self.y + (self.height * 1.0) * ((len(self.Buttons) + 1.0) / (len(self.Buttons) + 2.0))
                                  - ButtonPoleButtonYSize / 2, ButtonPoleButtonXSize,
                                  ButtonPoleButtonYSize, 0, new[1], WHT, RED, new[0])

    def changeChosen(self, number):
        for i in range(len(self.Buttons)):
            if i == number:
                self.Buttons[i].chosen = True
                self.chosen = i
            else:
                self.Buttons[i].chosen = False
