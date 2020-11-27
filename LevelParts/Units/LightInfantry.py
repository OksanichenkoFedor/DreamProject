from Draws.UnitDraws import lightinfantry_draw
from LevelParts.Units.UnitAI.UnitAI import *


class LightInfantry(Unit):

    """

    Class of first unit light infantry

    : method __init__(): Initialise Light infantry. Do the super()__init__()
                                   life = life of swordsman
                                   unit_type = "swordsman"
                                   Receives side, coord
    : method update(screen, level): Redraw city. Defining the action of the swordsman
    : method reaction(level): Defining the action of the swordsman
    : method interaction_with_unit(self, unit: Unit, number, action): Method, that process situation, when self interact
                                                                      with another unit. Light Infantry can just attack
    : method interaction_with_district(self, unit: district, number, action): Method, that process situation, when self
                                                                              interact  with another unit. Light
                                                                              Infantry can just attack.
    : method process_interaction(action):
    """

    def __init__(self, side, coord):
        super().__init__(side, LightInfantryLife, coord, LightInfantryType)

    def update(self, screen, level):
        """

        :param screen: Surface, where the picture is rendered
        :param level: Level of the game

        """
        lightinfantry_draw(self, self.side, self.position(level), screen)
        info = Info(self, level)
        solution = unitAI(info)
        self.reaction(solution)

    def reaction(self, solution):
        """

        :param solution: Solution, which tell unit what to do

        """

        if solution[0] == "move forward":
            if self.side[1] == "left":
                self.coord[1] += LightInfantrySpeed
            else:
                self.coord[1] -= LightInfantrySpeed

    def interaction_with_object(self, object, number, action):
        if action[0] == "attack":
            object.life -= action[1]
        return object, number, True

    def process_interaction(self, action):
        pass
