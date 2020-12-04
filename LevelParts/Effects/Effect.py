class Effect:
    """


    Abstract class, which realise effects

    : field self.x: First coordinate of effect
    : field self.y: Second coordinate of effect
    : field self.width: Width of effect
    : field self.height: Height of effect
    : field self.effect_time: Total time of effect life
    : field self.timer: Timer of effect

    : method __init__: Initialise Effect.
    : method update: Update effect
    """
    # TODO Создать родительский класс для различных эффектов (смерти юнитов, появление зданий, новых кнопок и тд)
    def __init__(self):
        pass

    def update(self):
        pass


if __name__ == "__main__":
    print("This module is not for direct call!")
