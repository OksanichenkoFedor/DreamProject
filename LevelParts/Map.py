class Map:
    """

    Class of level Map
    :field x: First coordinate of left up corner of map
    :field y: Second coordinate of left up corner of map
    :field width: Width of picture of map
    :field height: Height of picture of map
    :field number_of_left_roads: Number of left roads
    :field Left_Roads: Massive of left roads, each road has number of tuple, which contains coordinates of nodes of road
    :field number_of_right_roads: Number of right roads
    :field Right_Roads: Massive of right roads, each road has number of tuple, which contains coordinates of nodes of road
    :field Pole_Points: Massive of point of battle pole
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
        file_obj = open(file_name, "r")

        self.number_of_left_roads = int(file_obj.readline())
        self.number_of_right_roads = int(file_obj.readline())
        self.Left_Roads = []
        self.Right_Roads = []
        self.Pole_Points = []
        for i in range(self.number_of_left_roads):
            self.Left_Roads.append([])
            points_number = int(file_obj.readline())
            for j in range(points_number):
                self.Left_Roads[i].append((int(file_obj.readline()) + int(x), int(file_obj.readline()) + int(y)))
        for i in range(self.number_of_right_roads):
            self.Right_Roads.append([])
            points_number = int(file_obj.readline())
            for j in range(points_number):
                self.Right_Roads[i].append((int(file_obj.readline()) + int(x), int(file_obj.readline()) + int(y)))
        self.polygon_points_number = int(file_obj.readline())
        for i in range(self.polygon_points_number):
            self.Pole_Points.append((int(file_obj.readline()) + int(x), int(file_obj.readline()) + int(y)))


if __name__ == "__main__":
    print("This module is not for direct call!")
