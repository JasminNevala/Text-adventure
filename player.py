import world
import items
import random
import enemies


class Player:
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock(), items.Dagger(), items.CrustyBread()]
        self.hp = 100
        self.victory = False
        self.x = 1
        self.y = 2
        self.hp = 100

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
        best_weapon = self.most_powerful_weapon()
       # print("Your best weapon is your {}".format(best_weapon))

    def most_powerful_weapon(self):
        max_dmg = 0
        best_weapon = None
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        return best_weapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    """def move(self, dx, dy):  #This might be deleted later
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())"""

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {} !".format(enemy.name))
        else:
            print("{} HP is {}".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    """def flee(self, tile):
        #Moves the player randomly to an adjacent tile
        available_moves = tiles.MapTile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])"""

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal:")
            print("{}. {}.".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice)-1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, try again.")




