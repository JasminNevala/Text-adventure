from Classes import enemies
from Classes import items
from Classes import actions
from Classes import world


class MapTile():
    """A template that all other tiles will expand on. An abstract base class"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_txt(self):
        # will warn us if we accidentally create a MapTile directly
        raise NotImplementedError

    def modify_player(self, player):
        # will warn us if we accidentally create a MapTile directly
        raise NotImplementedError

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast)
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest)
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all available actions in this room"""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    def intro_txt(self):
        # overriding method in MapTile
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        # room has no action for player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def intro_txt(self):
        pass

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def intro_txt(self):
        pass

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("The enemy does {} damage. You have {} HP remaining".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class EmptyCavePath(MapTile):
    def intro_txt(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_txt(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_txt(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_txt(self):
        if self.enemy.is_alive():
            return """
            An ugly ogre lumbers in front of you!
            """
        else:
            return """
            The corpse of a dead ogre rots on the ground.
            """


class FindGoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(15))

    def intro_txt(self):
        return """
        Your notice something shiny in the corner.
        It's gold! You pick it up.
        """


class LeaveCaveRoom(MapTile):
    def intro_txt(self):
        """You see a bright light in the distance...
         ... it grows as you get closer! It's sunlight!
            Victory is yours!
                """

    def modify_player(self, player):
        player.victory = True