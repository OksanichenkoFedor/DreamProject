
class Unit:
    """

    Abstract class of unit
    : field self.side[0]: String, which say, what type of unit we have: "Order" , "Union"
    : field self.side[1]: A string that tells which side the given city is located on.
                            If side=="left", than this is city, located in the left side of the level
                            If side=="right", than this is city, located in the right side of the level
    : field self.life: Life of the unit
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

    : method __init__(side, life, coord, unit_type): Initialise Unit. Receives side, life, coord, unit_type
    : method update(screen, level): Update unit, and redraw it. Receives screen, level.
    : method reaction(level): Makes an action determined by the situation
    : method position(): Give position x, y, of this soldier in whole screen

    """

    def __init__(self, side, life, coord, unit_type):
        self.side = side
        self.life = life
        self.coord = coord
        self.type = unit_type

    def update(self, screen, level):
        pass

    def reaction(self, level):
        """

        :param level: Level of the game

        """
        pass

    def position(self, level):
        """

        :param level: Level of this game

        """
        if self.coord[0] == "left":


        elif self.coord[0] == "right":


        elif self.coord[0] == "battle_pole":
            return int(self.self.coord[1] + level.map.x), int(self.coord[2] + level.map.y)


        return int(self.coord[1] + level.map.x), int(self.coord[2] + level.map.y)


if __name__ == "__main__":
    print("This module is not for direct call!")
