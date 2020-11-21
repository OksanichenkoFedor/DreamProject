from Draws.CityDraws import *
from LevelParts.City.District import *
from Const.City import *


class CityCentre(District):
    """

    District "City Centre"

    """
    def __init__(self, side, x, y):
        super().__init__(side, CityCentreLife, x, y)

    def update(self, screen):
        """

        :param screen: Surface, where the picture is rendered
        :return: Draw city centre

        """
        if self.side[0] == "order":
            order_city_centre_draw(self, screen)
        else:
            union_city_centre_draw(self, screen)
        pass

