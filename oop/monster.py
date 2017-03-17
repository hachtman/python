class Monster:
    def __init__(self, **kwargs):
        self.hit_points = kwargs.get('hit_points', 1)
        self.weapon = kwargs.get('weapon', 1)
        self.color = kwargs.get('color', 1)
        self.sound = kwargs.get('sound', 1)

    def battlecry(self):
        return self.sound.upper()
