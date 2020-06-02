import player


class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def __str__(self):
        print("{} : {}".format(self.hotkey, self.name))


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=player.Player.move_north, name='Move North', hotkey='n')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=player.Player.move_south, name='Move South', hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=player.Player.move_east, name='Move East', hotkey='e')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=player.Player.move_east, name='Move West', hotkey='w')


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=player.Player.print_inventory, name='View inventory', hotkey='i')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=player.Player.attack, name='Attack', hotkey='a', enemy=enemy)


class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=player.Player.flee, name="Flee", hotkey='f', tile=tile)
