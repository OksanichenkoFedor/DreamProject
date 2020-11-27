class Interactable:
    """

    Abstract class of objects, that the action is applied to

    : field self.side[0]: String, which say, what type of interactable we have: "Order" , "Union"
    : field self.side[1]: A string that tells which side the given interactable is located on.
                            If side=="left", than this is interactable, located in the left side of the level
                            If side=="right", than this is interactable, located in the right side of the level
    : field self.life: Life of the interactable

    : method __init__(side,life): Initialise interactable. Receives side, life
    : method process_interaction(action): Function, which process interaction (action) with self

    """

    def __init__(self, side, life):
        self.side = side
        self.life = life

    def process_interaction(self, action):
        """

        Function, which process interaction with self
        :param action: Action, that we perform in relation to the unit
                              1.) String, that say, what, we will do
                              2.) Parameters, dependent on what we would do
        """
        pass


if __name__ == "__main__":
    print("This module is not for direct call!")
