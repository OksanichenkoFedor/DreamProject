from Const.Units import *
from LevelParts.Interactable import Interactable


class Unit(Interactable):
    """

    Abstract class of unit
    : field self.coord: Massive, which say, where unit is.
                            1.) First element - string - say where it is:
                                a.)"left" - unit is located on left road
                                b.)"battle_pole" - unit is located on battle pole
                                c.)"right" - unit is located on right road
                            2.) Second element
                                a.) If unit on roads, say on which from up to down (integer)
                                b.) If unit on pole, say first coord in map
                            3.) Third element
                                a.) If unit on road, say how much of the road did he pass (float from 0 to 1)
                                b.) If unit on pole, say second coord in map
    : field self.type: Tell us, which type this unit is. We need this for AI
    : field self.armor: Armor of unit (damage -> max(damage-armor,0))

    : method __init__(side, life, coord, unit_type, armor): Initialise Unit. Receives side, life, coord, unit_type,
                                                            armor.
    : method update(screen, level): Update unit, and redraw it. Also in this function we analise situation.
                                    Receives screen, level.
    : method reaction(solution): Realise an action determined by the solution
    : method position(): Give position x, y, of this soldier in whole screen
    : method interaction_with_interactable(object, number, action): Function, that realise interaction (action) self with
                                                          object(object, number). Object can be Unit of District


    """

    def __init__(self, side, life, coord, unit_type, armor=0):
        super().__init__(side, life)
        self.coord = coord
        self.type = unit_type
        self.armor = armor

    def update(self, screen, level):
        pass

    def reaction(self, solution):
        """

        :return: Solution: Solution, which tell unit what to do. Massive:
                                                             1.) String, that say, what, we will do
                                                             2.) Parameters, dependent on what we would do

        """

        if solution[0] == "move forward":
            if self.side[1] == "left":
                self.coord[1] += LightInfantrySpeed
            else:
                self.coord[1] -= LightInfantrySpeed

    def position(self, level):
        """

        :param level: Level of this game

        """
        if self.coord[0] == "left":

            for i in range(1, len(level.map.total_coords_L[self.coord[1]])):
                point_coord_next = level.map.total_coords_L[self.coord[1]][i]
                point_coord_cur = level.map.total_coords_L[self.coord[1]][i - 1]
                if (self.coord[2] - point_coord_next) * (self.coord[2] - point_coord_cur) <= 0:
                    x_next = level.map.Left_Roads[i][0]
                    y_next = level.map.Left_Roads[i][1]
                    x_prev = level.map.Left_Roads[i - 1][0]
                    y_prev = level.map.Left_Roads[i - 1][0]

                    t = (self.coord[2] - level.map.total_coords_L[self.coord[1]][i - 1]) / (
                            level.map.total_coords_L[self.coord[1]][i] - level.map.total_coords_L[self.coord[1]][
                        i - 1])

                    return int(x_prev + t * (x_next - x_prev) + level.map.x), int(
                        y_prev + t * (y_next - y_prev) + level.map.y)

        elif self.coord[0] == "right":
            for i in range(1, len(level.map.total_coords_R[self.coord[1]])):
                point_coord_next = level.map.total_coords_R[self.coord[1]][i]
                point_coord_cur = level.map.total_coords_R[self.coord[1]][i - 1]
                if (self.coord[2] - point_coord_next) * (self.coord[2] - point_coord_cur) <= 0:
                    x_next = level.map.Right_Roads[i][0]
                    y_next = level.map.Right_Roads[i][1]
                    x_prev = level.map.Right_Roads[i - 1][0]
                    y_prev = level.map.Right_Roads[i - 1][0]

                    t = (self.coord[2] - level.map.total_coords_R[self.coord[1]][i - 1]) / (
                            level.map.total_coords_R[self.coord[1]][i] - level.map.total_coords_R[self.coord[1]][
                        i - 1])

                    return int(x_prev + t * (x_next - x_prev) + level.map.x), int(
                        y_prev + t * (y_next - y_prev) + level.map.y)
        elif self.coord[0] == "battle_pole":
            return int(self.coord[1] + level.map.x), int(self.coord[2] + level.map.y)

    def interaction_with_interactable(self, interactable, number, action):
        """

        Function, that realise interaction with object (unit or district)
        :param interactable: Interactable that will be attacked
        :param number: Number of index of object, that we will attack, in massive
        :param action: Action, that we perform in relation to the object
                              1.) String, that say, what, we will do
                              2.) Parameters, dependent on what we would do
        :return: 1.) Changed interactable
                 2.) Number of index of object, that we will attack, in massive
                 3.) is_attack: If interact with enemy object (check, by comparing fields side[1] of self and object), then
                                True, else False
        """
        if self.side[1] == interactable.side[1]:
            interactable.process_interaction(action)
            return interactable, number, False
        else:
            interactable.process_interaction(action)
            return interactable, number, True


if __name__ == "__main__":
    print("This module is not for direct call!")
