from Draws.UnitDraws import unit_draw
from LevelParts.Units.UnitAI.UnitAI import *
from LevelParts.Units.Unit import *


class HeavyInfantry(Unit):

    """

    Class of first unit heavy infantry

    : method __init__(): Initialise Heavy infantry. Do the super()__init__()
                                   life = life of heavy unit
                                   unit_type = "heavy_unit"
                                   Receives side, coord
    : method update(screen, level): Redraw city. Defining the action of the heavy unit
    #: method reaction(level): Defining the action of the heavy unit
    : method interaction_with_unit(self, unit: Unit, number, action): Method, that process situation, when self interact
                                                                      with another unit. Heavy Infantry can just attack
    : method interaction_with_district(self, unit: district, number, action): Method, that process situation, when self
                                                                              interact  with another unit. Heavy
                                                                              Infantry can just attack.
    : method process_interaction(action):
    """

    def __init__(self, side, coord, images):
        if side[0] == "order":
            super().__init__(side, HeavyInfantryOrderLife, coord, HeavyInfantryType, images, HeavyInfantryOrderArmor,
                             HeavyInfantryOrderRange, HeavyInfantryOrderSpeed, HeavyInfantryOrderCooldown,
                             HeavyInfantryOrderDamage, HeavyInfantryOrderDamageSpread, HeavyInfantryOrderSideX,
                             HeavyInfantryOrderSideY, HeavyInfantryOrderTrainTime, HeavyInfantryOrderCost)
        else:
            super().__init__(side, HeavyInfantryUnionLife, coord, HeavyInfantryType, images, HeavyInfantryUnionArmor,
                             HeavyInfantryUnionRange, HeavyInfantryUnionSpeed, HeavyInfantryUnionCooldown,
                             HeavyInfantryUnionDamage, HeavyInfantryUnionDamageSpread, HeavyInfantryUnionSideX,
                             HeavyInfantryUnionSideY, HeavyInfantryUnionTrainTime, HeavyInfantryUnionCost)

    def update(self, level):
        """

        :param level: Level of the game

        """
        if self.interact_timer > 0:
            self.interact_timer -= 1
        info = Info(self, level)
        solution = unitAI(info)
        return self.reaction(solution, level)

    def draw(self, screen, level):
        unit_draw(self, self.side, self.position(level), screen, self.give_current_image(), self.XSize, self.YSize)
