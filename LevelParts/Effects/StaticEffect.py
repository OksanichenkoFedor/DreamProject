class StaticEffect:
    """


    Abstract class, which realise effects

    : field self.x: First coordinate of effect
    : field self.y: Second coordinate of effect
    : field self.width: Width of effect
    : field self.height: Height of effect
    : field self.effect_time: Total time of effect life
    : field self.timer: Timer of effect
    : field self.is_exist: Boolean, which tell is this effect exist
    : field self.images: Massive of necessary images

    : method __init__: Initialise Effect.
    : method update: Update effect
    """
    # TODO Создать родительский класс для различных эффектов (смерти юнитов, появление зданий, новых кнопок и тд)
    def __init__(self, x, y, w, h, effect_time, images):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.effect_time = effect_time
        self.timer = effect_time
        self.is_exist = True
        self.images = images

    def update(self, screen):
        pass


if __name__ == "__main__":
    print("This module is not for direct call!")
