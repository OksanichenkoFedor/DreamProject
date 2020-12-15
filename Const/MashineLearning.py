from Const.Units import LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, HealerType, \
    AlchemistType

DamageCost = [500.0, 50.0, 50.0, 50.0]
TrainUnitCost = {LightInfantryType: 0, HeavyInfantryType: 0, CavalryType: 0, LongDistanceSoldierType: 0, HealerType: 0,
                 AlchemistType: 0}
UnitNumber = {LightInfantryType: 0, HeavyInfantryType: 1, CavalryType: 2, LongDistanceSoldierType: 3, HealerType: 4,
                 AlchemistType: 4}
UnitTypeOrder = {0: LightInfantryType, 1: HeavyInfantryType, 2: CavalryType, 3: LongDistanceSoldierType, 4: HealerType}
UnitTypeUnion = {0: LightInfantryType, 1: HeavyInfantryType, 2: CavalryType, 3: LongDistanceSoldierType,
                 4: AlchemistType}


ThrowUnitCost = 0

WinCost = 1000

TimeCost = 0.00

MaxGameTime = 20000

NNLayers = [81, 100, 11]

ParentsNumber = 10

ChildsNumber = 50

StartRate = 1

LearningRate = 0.1

ReluF = "relu"

Tanh = "tanh"

NNFunctions = [ReluF, ReluF]

