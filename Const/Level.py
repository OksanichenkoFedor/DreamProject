"""

Constants for the game level

"""
FPS = 50
DrawingCoefficient = 1.0
LevelXSize = 1500
LevelYSize = 850
MapXSize = 750
MapYSize = 850
CityXSize = 226
CityYSize = MapYSize
ButtonPoleXSize = 150
ButtonPoleYSize = CityYSize
ButtonAnimationTime = 50
ButtonPoleButtonXSize = ButtonPoleXSize*3.0/4.0
ButtonPoleButtonYSize = ButtonPoleButtonXSize*1.2
BuffSizeIncreasing = 1.1
TakingDamageAnimationType = "TakeDamage"
DealingDamageAnimationType = "DealDamage"
DeathAnimationType = "Death"
MovementAnimationType = "Movement"
MotionlessAnimationType = "Motionless"
animation_duration = {MotionlessAnimationType: 1, MovementAnimationType: 0, DealingDamageAnimationType: 4,
                      TakingDamageAnimationType: 0, DeathAnimationType: 0}
total_image_number = 129
number_of_bushes = 15
number_of_trees = 15
TreeXSize = 70
TreeYSize = 120
BushXSize = 50
BushYSize = 35
WHT = (255, 255, 255)
BLC = (0, 0, 0)
RED = (255, 0, 0)
BLU = (0, 0, 255)
GRY = (144, 144, 144)
GRN = (0, 255, 0)
DGR = (74, 141, 85)
map_drawer = "Widgets/MapEditor/map2.txt"
NumberOfRoads = 3
Win_Screen_Time = 200


if __name__ == "__main__":
    print("This module is not for direct call!")
