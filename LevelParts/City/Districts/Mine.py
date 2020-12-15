from Draws.CityDraws import *
from LevelParts.City.Districts.District import *
from Const.City import *


class Mine(District):
    """

    Class of district "Mine"

    : method __init__(side, x, y): Initialise Mine
    : method update(screen): Update district and redraw it

    """
    def __init__(self, side, x, y, image_mine, image_master):
        super().__init__(side, MineLife, x, y, MineNumber, image_master)
        self.image_mine = image_mine

    def update(self, money):
        if self.master > 0:
            return money + (((self.life * 1.0) / (MineLife * 1.0)) * MineAdditionalSpeed + MineDefaultSpeed)*2.0
        else:
            return money + (((self.life * 1.0) / (MineLife * 1.0)) * MineAdditionalSpeed + MineDefaultSpeed)

    def draw(self, screen):
        mine_draw(self, screen, self.image_mine, self.master)


