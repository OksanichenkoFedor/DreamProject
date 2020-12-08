from LevelParts.Effects.StaticEffect import StaticEffect
from Const.Effects import *
from Draws.EffectDraws import *


class Death(StaticEffect):
    """

    Effect of death
    : field images[0]: Image of blood puddle
    : field images[1]: Image of dead unit

    """
    def __init__(self, x, y, w, h, images):
        super().__init__(x, y, w, h, DeathAnimationTime, images)

    def update(self, screen):
        if self.timer > 0:
            blood_puddle_draw(self.x, self.y, self.width * (
                        BloodSize1 + (BloodSize0 - BloodSize1) * ((1.0 * self.timer) / (self.effect_time * 1.0)))
                        , self.height * (BloodSize1 + (BloodSize0 - BloodSize1) * ((1.0 * self.timer) /
                        (self.effect_time * 1.0))), self.images[0], screen)
            dead_unit_draw(self.x, self.y, self.width/2, self.height/2, self.images[1], screen)
            self.timer -= 1
        else:
            self.is_exist = False



