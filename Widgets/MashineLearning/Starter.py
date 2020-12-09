from Const.Units import *
from Const.Level import *
import pygame


def true_image_import():
    union_unit_types = [LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, AlchemistType]
    order_unit_types = [LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, HealerType]

    Another_Images = {}
    Another_Images["castle union"] = 0
    Another_Images["square"] = pygame.image.load('images/ploschad.png').convert_alpha()
    Another_Images["castle order"] = pygame.image.load('images/zdanie_orden.png').convert_alpha()
    Another_Images["bruschatka"] = pygame.image.load('images/bruschatka.png').convert_alpha()

    Union_Units_Images = {}
    for unit_type in union_unit_types:
        Union_Units_Images[unit_type] = {}

    Order_Units_Images = {}
    for unit_type in order_unit_types:
        Order_Units_Images[unit_type] = {}

    return Another_Images, Union_Units_Images, Order_Units_Images



