class Item:
    """The base class for all items"""

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold", description="Round coin of value {}".format(str(self.amt)), value=self.amt)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Sword", description="A small weapon with some rust in it", value=10, damage=10)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock", description="A fist sized rock", value=1, damage=1)
