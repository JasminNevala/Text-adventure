class Enemy:
    """The base class for all the enemies"""

    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return self.name


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=20, damage=15)


class BatColony(Enemy):
    def __init__(self):
        super().__init__(name="Bat Colony", hp=100, damage=4)


class RockMonster(Enemy):
    def __init__(self):
        super().__init__(name="Rock Monster", hp=80, damage=15)