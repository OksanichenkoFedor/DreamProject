from Const.Units import *
from LevelParts.Interactable import Interactable
from Const.Level import *

class Unit(Interactable):
    """

    Abstract class of unit
    : field self.coord: Massive, which say, where unit is.
                            1.) First element - string - say where it is:
                                a.)"left" - unit is located on left road
                                b.)"battle_pole" - unit is located on battle pole
                                c.)"right" - unit is located on right road
                                d.)"Buffer" - unit is in buffer
                            2.) Second element
                                a.) If unit on roads, say on which from up to down (integer)
                                b.) If unit on pole, say first coord in map
                            3.) Third element
                                a.) If unit on road, say how much of the road did he pass (float from 0 to 1)
                                b.) If unit on pole, say second coord in map
    : field self.type: Tell us, which type this unit is. We need this for AI
    : field self.armor: Armor of unit (damage -> max(damage-armor,0))
    : field self.attack_range: Range of unit attack
    : field self.images: Massive of dictionary of images.
                                                         1.) Key = String, that tell type of images
                                                         2.) Massive of number of images, massive of images

    : field self.speed: Speed of unit
    : field self.cooldown: Time of recharge
    : field self.interact_timer: Timer, which check recharging
    : field self.animation_timer: Massive, first element shows which type of animation this unit have
                                           second tell the time of animation
    : field self.damage: Unit damage
    : field self.damage_spread: Shows random error of unit damage
    : field self.XSize: First coordinate size of unit image
    : field self.YSize: First coordinate size of unit image
    : field self.train_timer: Total time of train
    : field self.train_time: Time, left for train
    : field self.animation: String, which teel type of current animation
    : field self.animation_timer: Time, left for animation
    : field self.animation_total_time: Total time of current animation
    : field self.cost: Cost of this unit
    : field self.is_buffed: Boolean, which is true if unit buffed

    : method __init__(side, life, coord, unit_type, armor): Initialise Unit. Receives side, life, coord, unit_type,
                                                                                      image, armor, attack_range, speed,
                                                                                      cooldown, damage, damage_spread.
    : method update(screen, level): Update unit, and redraw it. Also in this function we analise situation.
                                    Receives screen, level.
    : method reaction(solution): Realise an action determined by the solution
    : method position(): Give position x, y, of this soldier in whole screen
    : method change_buffer_place(): Change x, y in buffer, when situation is changed


    """

    def __init__(self, side, life, coord, unit_type, images, armor, attack_range, speed, cooldown, damage, damage_spread,
                 XSize, YSize, train_time, cost):
        super().__init__(side, life)
        self.coord = []
        self.coord.append(coord[0])
        self.coord.append(coord[1])
        self.coord.append(coord[2])
        self.type = unit_type
        self.armor = armor
        self.range = attack_range
        self.images = images
        self.speed = speed
        self.cooldown = cooldown
        self.interact_timer = self.cooldown
        self.damage = damage
        self.damage_spread = damage_spread
        self.XSize = XSize
        self.YSize = YSize
        self.train_timer = train_time
        self.train_time = train_time
        self.animation = MotionlessAnimationType
        self.animation_timer = 1
        self.animation_time = 0
        self.cost = cost
        self.is_buffed = False

    def update(self, level):
        pass

    def draw(self, screen, level):
        pass

    def reaction(self, solution, level):
        """
        :param solution: Solution, which tell unit what to do. Massive:
                                                               1.) String, that say, what, we will do
                                                               2.) Parameters, dependent on what we would do
               level: Level of this game

        :return: Something that depends on the solution. if nothing to return, return 0
        """
        # Написать нормальное перемещение по дорогам
        if solution[0] == "move forward":
            self.change_animation(MovementAnimationType)
            if self.side[1] == "left":    #Юнит из левого города
                if self.coord[0] == "left":    #Юнит на левой дороге
                    if self.coord[2] < 1:
                        road_num = self.coord[1]
                        road_length = level.map.total_length_L[road_num]
                        self.coord[2] += self.speed/road_length
                        self.coord[2] = min(1, self.coord[2])
                    else:
                        self.coord[0] = "battle_pole"
                        _ = self.coord[1]
                        self.coord[1] = level.map.Left_Roads[_][-1][0]
                        self.coord[2] = level.map.Left_Roads[_][-1][1]



                elif self.coord[0] == "right":    #Юнит на правой дороге
                    if self.coord[2] > 0:
                        road_num = self.coord[1]
                        road_length = level.map.total_length_R[road_num]
                        self.coord[2] -= self.speed / road_length
                        self.coord[2] = max(0, self.coord[2])


                elif self.coord[0] == "battle_pole":
                    road_num, distance = level.map.nearest_road(self.coord[1], self.coord[2], "left")
                    if (distance - self.speed) > 0:
                        cos = (level.map.Right_Roads[road_num][-1][0] - self.coord[1]) / distance
                        sin = (level.map.Right_Roads[road_num][-1][1] - self.coord[2]) / distance
                        self.coord[1] += self.speed * cos
                        self.coord[2] += self.speed * sin
                    else:
                        self.coord[0] = "right"
                        self.coord[1] = road_num
                        self.coord[2] = 1

            elif self.side[1] == "right":    #Юнит из правого города

                if self.coord[0] == "left":    #Юнит на левой дороге
                    if self.coord[2] > 0:
                        road_num = self.coord[1]
                        road_length = level.map.total_length_L[road_num]
                        self.coord[2] -= self.speed/road_length
                        self.coord[2] = max(0, self.coord[2])


                elif self.coord[0] == "right":    #Юнит на правой дороге
                    if self.coord[2] < 1:
                        road_num = self.coord[1]
                        road_length = level.map.total_length_R[road_num]
                        self.coord[2] += self.speed/road_length
                        self.coord[2] = min(1, self.coord[2])
                    else:
                        self.coord[0] = "battle_pole"
                        _ = self.coord[1]
                        self.coord[1] = level.map.Right_Roads[_][-1][0]
                        self.coord[2] = level.map.Right_Roads[_][-1][1]

                elif self.coord[0] == "battle_pole":
                    road_num, distance = level.map.nearest_road(self.coord[1], self.coord[2], "right")
                    if (distance - self.speed) > 0:
                        cos = (+level.map.Left_Roads[road_num][-1][0] - self.coord[1]) / distance
                        sin = (level.map.Left_Roads[road_num][-1][1] - self.coord[2]) / distance
                        self.coord[1] += self.speed * cos
                        self.coord[2] += self.speed * sin
                    else:
                        self.coord[0] = "left"
                        self.coord[1] = road_num
                        self.coord[2] = 1


        elif solution[0] == "interact":
            if self.interact_timer == 0:
                self.animation = DealingDamageAnimationType
                solution[1].process_interaction(solution[2])
                self.interact_timer = self.cooldown

        elif solution[0] == "moving to unit":
            self.change_animation(MovementAnimationType)
            if self.coord[0] == "battle_pole":
                self.coord[1] += solution[1]*self.speed
                self.coord[2] += solution[2]*self.speed
            elif self.coord[0] == "left":
                road_num = self.coord[1]
                road_length = level.map.total_length_L[road_num]
                self.coord[2] += (1.0*solution[1]*self.speed) / road_length
            elif self.coord[0] == "right":
                road_num = self.coord[1]
                road_length = level.map.total_length_R[road_num]
                self.coord[2] += (1.0*solution[1]*self.speed) / road_length

    def position(self, level):
        """

        :param level: Level of this game

        """
        if self.coord[0] == "left":

            for i in range(1, len(level.map.total_coords_L[self.coord[1]])):
                point_coord_next = level.map.total_coords_L[self.coord[1]][i]
                point_coord_cur = level.map.total_coords_L[self.coord[1]][i - 1]
                if (self.coord[2] - point_coord_next) * (self.coord[2] - point_coord_cur) <= 0:
                    x_next = level.map.Left_Roads[self.coord[1]][i][0]
                    y_next = level.map.Left_Roads[self.coord[1]][i][1]
                    x_prev = level.map.Left_Roads[self.coord[1]][i - 1][0]
                    y_prev = level.map.Left_Roads[self.coord[1]][i - 1][1]

                    t = (self.coord[2] - level.map.total_coords_L[self.coord[1]][i - 1]) / (level.map.total_coords_L[self.coord[1]][i] - level.map.total_coords_L[self.coord[1]][i - 1])
                    return (int(x_prev + t * (x_next - x_prev) ), int(y_prev + t * (y_next - y_prev) ))

        elif self.coord[0] == "right":
            for i in range(1, len(level.map.total_coords_R[self.coord[1]])):
                point_coord_next = level.map.total_coords_R[self.coord[1]][i]
                point_coord_cur = level.map.total_coords_R[self.coord[1]][i - 1]
                if (self.coord[2] - point_coord_next) * (self.coord[2] - point_coord_cur) <= 0:
                    x_next = level.map.Right_Roads[self.coord[1]][i][0]
                    y_next = level.map.Right_Roads[self.coord[1]][i][1]
                    x_prev = level.map.Right_Roads[self.coord[1]][i - 1][0]
                    y_prev = level.map.Right_Roads[self.coord[1]][i - 1][1]

                    t = (self.coord[2] - level.map.total_coords_R[self.coord[1]][i - 1]) / (level.map.total_coords_R[self.coord[1]][i] - level.map.total_coords_R[self.coord[1]][i - 1])

                    return (int(x_prev + t * (x_next - x_prev)), int(y_prev + t * (y_next - y_prev)))
        elif self.coord[0] == "battle_pole":
            return (int(self.coord[1] ), int(self.coord[2]))
        elif self.coord[0] == "buffered":
            return (int(self.coord[1] ), int(self.coord[2]))

    def process_interaction(self, action):
        """

                Function, which process interaction with self
                :param action: Action, that we perform in relation to the unit
                                      1.) String, that say, what, we will do
                                      2.) Parameters, dependent on what we would do
                """
        if action[0] == "attacked":
            self.change_animation(TakingDamageAnimationType)
            self.life -= max(action[1]-self.armor, 0)
        elif action[0] == "healed":
            self.life = min(action[1] + self.life, self.full_life)
        elif action[0] == "increased":
            if not self.is_buffed:
                self.XSize *= BuffSizeIncreasing
                self.YSize *= BuffSizeIncreasing
                self.is_buffed = True
            self.damage *= action[1]/100 + 1.0
            self.damage_spread *= action[1]/100 + 1.0

    def change_buffer_place(self, x, y):
        """

        :param x: New first coordinate
        :param y: New second coordinate
        :return: Change coord of unit
        """
        if self.coord[0] == "buffered":
            self.coord[1] = x
            self.coord[2] = y

    def give_current_image(self):
        """

        :return: Current image

        """
        if self.animation == DealingDamageAnimationType:
            fase = (self.interact_timer * 1.0) / (self.cooldown * 1.0) - 0.001
            image_number = int(fase * (animation_duration[self.animation] - 1.0))
            return self.images[DealingDamageAnimationType][1][image_number]
        else:
            return self.images[MotionlessAnimationType][1][0]




    def change_animation(self, animation):
        pass


if __name__ == "__main__":
    print("This module is not for direct call!")
