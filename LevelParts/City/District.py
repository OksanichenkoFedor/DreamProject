class District:
    # TODO Создать родительский класс для районов
    """

    Abstract class of building
    : field self.side[0]: String, which say, what type of district we have: "Order" , "Union"
    : field self.side[1]: A string that tells which side the given city is located on. If side=="left", than this is city, located in the left side of the level
                                                                               If side=="right", than this is city, located in the right side of the level
    : field self.master: Not dungeon, but master. Says how much masters are there
    : field self.life: Life of district
    : field self.x: First coord of left-up point of district
    : field self.y: Second coord of left-up point of district
    : field self.level: Level of the district

    """
    def __init__(self, side, life, x, y):
        self.side = side
        self.level = 1
        self.master = 0
        self.life = life
        self.x = x
        self.y = y


    def under_attack(self, damage):
        """

        :param damage:
        :return:
        """
        self.life -= damage


if __name__ == "__main__":
    print("This module is not for direct call!")