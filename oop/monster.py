"""Monster Class"""
import random

from combat import Combat


COLORS = ["Yellow", "Red", "Pink", "Green"]


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = "claws"
    sound = "snicker"

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
        return '{} {}, HP: {}, XP: {}.'.format(self.color.title(),
                                               self.__class__.__name__,
                                               self.hit_points,
                                               self.experience)

    def battlecry(self):
        """returns monster's sound"""
        return self.sound.upper()



class Goblin(Monster):
    max_hit_points = 3
    max_experience = 4
    sound = 'sneer'

class Troll(Monster):
    min_hit_points = 5
    max_hit_points = 50
    min_experience = 2
    max_experience = 3
    sound = 'hurrumph'

class Dragon(Monster):
    min_hit_points = 2
    max_hit_points = 5000
    min_experience = 1
    max_experience = 100
    sound = 'Roar'
