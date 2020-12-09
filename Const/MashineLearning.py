from Const.Units import LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, HealerType, \
    AlchemistType

DamageCost = [10.0, 5.0, 5.0, 5.0]
TrainUnitCost = {LightInfantryType: 1, HeavyInfantryType: 1, CavalryType: 1, LongDistanceSoldierType: 1, HealerType: 1,
                 AlchemistType: 1}
UnitNumber = {LightInfantryType: 0, HeavyInfantryType: 1, CavalryType: 2, LongDistanceSoldierType: 3, HealerType: 4,
                 AlchemistType: 4}

ThrowUnitCost = 2

WinCost = 1000

MaxGameTime = 5000

NNLayers = [75, 20, 20, 20, 4]

ReluF = "relu"

Tanh = "tanh"

NNFunctions = [Tanh, ReluF, ReluF, ReluF, Tanh]