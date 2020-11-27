from LevelParts.Interactable import Interactable


class District(Interactable):
    # TODO Создать родительский класс для районов
    """

    Abstract class of district

    : field self.master: Not dungeon, but master. Says how much masters are there
    : field self.x: First coord of left-up point of district
    : field self.y: Second coord of left-up point of district
    : field self.level: Level of the district

    : method self.__init__(side ,life, x, y): Initialise District. Receives side, life, x, y
    : method self.under_attack(damage): Processes taking damage (amount of damage is given (damage) )

    """

    def __init__(self, side, life, x, y):
        super().__init__(side, life)
        self.level = 1
        self.master = 0
        self.x = x
        self.y = y

    def under_attack(self, damage):
        self.life -= damage

    def process_interaction(self, action):
        """

        Function, which process interaction with self
        :param action: Action, that we perform in relation to the district
                              1.) String, that say, what, we will do
                              2.) Parameters, dependent on what we would do
        """
        self.life -= action[1]


if __name__ == "__main__":
    print("This module is not for direct call!")
