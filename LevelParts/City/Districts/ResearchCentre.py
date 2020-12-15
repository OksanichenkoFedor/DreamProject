from Draws.CityDraws import *
from LevelParts.City.Districts.District import *
from Const.City import *


class ResearchCentre(District):
    """

    Class of district "Mine"

    : method __init__(side, x, y): Initialise Mine
    : method update(screen): Update district and redraw it

    """
    def __init__(self, side, x, y, image_research_centre, image_master):
        super().__init__(side, ResearchCentreLife, x, y, ResearchCentreNumber, image_master)
        self.image_research_centre = image_research_centre

    def update(self, tech):
        if self.master > 0:
            return tech + ((self.life * 1.0) / (
                        ResearchCentreLife * 1.0) * ResearchCentreAdditionalSpeed + ResearchCentreDefaultSpeed)*2.0
        else:
            return tech + ((self.life * 1.0) / (
                        ResearchCentreLife * 1.0) * ResearchCentreAdditionalSpeed + ResearchCentreDefaultSpeed)

    def draw(self, screen):
        research_centre_draw(self, screen, self.image_research_centre, self.image_master)