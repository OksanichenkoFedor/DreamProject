import pygame
from Draws.LevelDraws import button_draw


class Button:
    """

    Simple button

    :field color: Color of button body
    :field x: First coordinate of button
    :field y: Second coordinate of button
    :field length: X-side of button body
    :field height: Y-side of button body
    :field width: Argument for drawing sides of button
    :field text: String, that we will draw on button
    :field text_color: Color of button text
    :field chosen: Boolean, which tell is this button is chosen button

    :method __init__: Initialise Button. Receives color, x, y, length, height, width, text, text_color.
    :method update(): Update the button and draw it
    :method is_pressed: Tell information about is button pressed (True) or no(False)

    """

    def __init__(self, color, x, y, length, height, width, text, text_color, chosen_color=False, unit_type=None):
        self.color = color
        if not chosen_color:
            self.chosen_color = color
        else:
            self.chosen_color = chosen_color
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width
        self.text = text
        self.text_color = text_color
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)
        self.chosen = False
        self.type = unit_type

    def update_button(self, x, y):
        self.x = x
        self.y = y

    def draw_button(self, screen):
        button_draw(screen, self)
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)

    def is_pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print("Some button was pressed!")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
