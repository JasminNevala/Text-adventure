import world
from player import Player
import items


def play():
    print("Escape from Cave terror!")
    player = Player()
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print("Go North!")
        elif action_input in ['s', 'S']:
            print("Go South!")
        elif action_input in ['w', 'W']:
            print("Go West!")
        elif action_input in ['e', 'E']:
            print("Go East!")
        elif action_input in ['i', 'I']:
            player.print_inventory()
        else:
            print("Invalid action!")


def get_player_command():
    return input("Action: ")


play()

""""" world.load_tiles()  #This is for possible later use
    player = Player()
    # These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_txt())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input("Action: ")
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break"""""

"""if __name__ == "__main__":
    play()"""
