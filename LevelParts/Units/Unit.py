


class Unit:
    """

    Abstract class of unit
    : field self.side[0]: String, which say, what type of unit we have: "Order" , "Union"
    : field self.side[1]: A string that tells which side the given city is located on. If side=="left", than this is city, located in the left side of the level
                                                                               If side=="right", than this is city, located in the right side of the level
    : field self.life: Life of the unit
    : field self.coord: Massive, which say, where unit is.
                                                          1.) First element - string - say where it is: a.)"left" - unit is located on left road
                                                                                                        b.)"battle_pole" - unit is located on battle pole
                                                                                                        c.)"right" - unit is located on right road
                                                          2.) Second element a.) If unit on roads, say on which from up to down (integer)
                                                                             b.) If unit on pole, say first coord in map
                                                          3.) Third element  a.) If unit on road, say how much of the road did he pass (float from 0 to 1)
                                                                             b.) If unit on pole, say second coord in map
    : field self.type: Tell us, which type this unit is. We need this for AI

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
        Does the action described in object solution
        :param solution:
        :return:
        """
        pass


if __name__ == "__main__":
    print("This module is not for direct call!")
