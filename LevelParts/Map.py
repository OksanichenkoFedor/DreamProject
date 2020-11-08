class Map:
    """

    Class of level Map
    :field x: First coordinate of left up corner of map
    :field y: Second coordinate of left up corner of map
    :field width: Width of picture of map
    :field height: Height of picture of map
    :method __init__: Initialise level map
    :method draw

    """

    # TODO Создать класс, который будет по файлу строить карту, а так же её рисовать
    def __init__(self, file_name, x, y, w, h):
        """

        Initialise level map
        :param file_name: Name of the file where we will get information about the map
        :param x: First coordinate of left up corner of map
        :param y: Second coordinate of left up corner of map
        :param w: Width of picture of map
        :param h: Height of picture of map

        """
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        file_obj = open(file_name)



if __name__ == "__main__":
    print("This module is not for direct call!")
