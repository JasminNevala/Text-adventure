import world
from player import Player
from collections import OrderedDict


def play():
    print("Escape from Cave terror!")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_txt())
        room.modify_player(player)
        choose_action(room, player)
        if choose_action in ['n', 'N']:
            player.move_north()
        elif choose_action in ['s', 'S']:
            player.move_south()
        elif choose_action in ['w', 'W']:
            player.move_west()
        elif choose_action in ['e', 'E']:
            player.move_east()
        elif choose_action in ['i', 'I']:
            player.print_inventory()
        elif choose_action in ['a', 'A']:
            player.attack()
        elif choose_action in ['h', 'H']:
            player.heal()
        else:
            print("Invalid action!")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print inventory")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
        if player.hp < 100:
            action_adder(actions, 'h', player.heal, "Heal")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")


play()
