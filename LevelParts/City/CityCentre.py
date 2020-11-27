from Draws.CityDraws import *
from LevelParts.City.District import *
from Const.City import *


class CityCentre(District):
    """

    Class of district "City Centre"

    : method __init__(side, x, y): Initialise City Centre. Do the super()__init__() life = life of city centre.
                                   Receives side, x, y
    : method update(screen): Update district and redraw it

    """
    def __init__(self, side, x, y):
        super().__init__(side, CityCentreLife, x, y, CityCentreNumber)

    def update(self, screen):
        """

        :param screen: Surface, where the picture is rendered

        """
        if self.side[0] == "order":
            order_city_centre_draw(self, self.side[1], screen)
        else:
            union_city_centre_draw(self, self.side[1], screen)
        pass

