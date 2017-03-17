# 2d game with basic ascii graphics.
# Move around the grid.

# Draw the grid.
# Randomise player, door and monster.
# Draw player on grid
# take iput for movement
# move player unless invalid move
# check win loss
# clear screen and redraw grid.

"""Dungeon RPG"""
import random
import os

STATUS = {
    'grid_size': 5,
    'door_open?': False,
    'player': {
        'weapon': False,
    },
    'locations': {
        'player': [1, 1],
        'monster': None,
        'door': None
    }
}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_map(grid_size):
    """Draws a map of selected size"""
    STATUS['game_grid'] = []  # Could be a tuple?
    STATUS['grid_size'] = grid_size
    x_coord = 1
    y_coord = 1
    grid_size_counter = grid_size * grid_size
    while (grid_size_counter):
        STATUS['game_grid'].append([x_coord, y_coord])
        x_coord += 1
        if (x_coord == grid_size + 1):
            y_coord += 1
            x_coord = 1
        grid_size_counter -= 1


def set_locations():
    """Set the locations of the weapon and the monster"""


def get_locations():
    """Returns the locations dict."""
    return STATUS['locations']


def get_moves():
    x_coord = get_locations()['player'][0]
    y_coord = get_locations()['player'][1]
    # If player's y coord is 0, they can't move down
    # If player's y coord is grid size, they can't move up
    # If player's x coord is 0, they can't move left
    # If player's x coord is grid size, they can't move right
    if (x_coord == 1 and y_coord == 1):
        return ['UP', 'RIGHT']
    elif (x_coord == STATUS['grid_size'] and y_coord == STATUS['grid_size']):
        return ['DOWN', 'LEFT']
    elif (x_coord == 1 and y_coord == STATUS['grid_size']):
        return ['UP', 'RIGHT']
    elif (x_coord == STATUS['grid_size'] and y_coord == 1):
        return ['UP', 'LEFT']
    elif (x_coord == 1):
        return ['UP', 'RIGHT', 'DOWN']
    elif (y_coord == 1):
        return ['RIGHT', 'UP', 'LEFT']
    elif (x_coord == STATUS['grid_size']):
        return ['UP', 'DOWN', 'LEFT']
    elif (y_coord == STATUS['grid_size']):
        return ['DOWN', 'LEFT', 'RIGHT']
    else:
        return ['UP', 'RIGHT', 'DOWN', 'LEFT']


print(get_moves())


def move_player(move):
    if (move == 'UP'):
        STATUS['locations']['player'][1] -= 1
    elif (move == 'DOWN'):
        STATUS['locations']['player'][1] += 1
    elif (move == 'LEFT'):
        STATUS['locations']['player'][0] -= 1
    else:
        STATUS['locations']['player'][0] += 1
    print(STATUS['locations']['player'])


def get_dungeon_size():
    size = input("Choose the size of the dungeon... (4 - 24)\n>")
    size = int(size)
    while (size < 4 or size > 24):
        print("Pick a number between four and 24.")
        size = input("Choose the size of the dungeon... (4 - 24)")
    return size


def draw_dungeon():
    grid_size = STATUS['grid_size']
    cells = STATUS['game_grid']
    player = get_locations()['player']
    print(" _" * grid_size)
    tile = "|{}"
    for cell in cells:
        x, y = cell
        if x < grid_size:
            line_end = ''
            if cell == player:
                output = tile.format("P")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("P|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def run_game():
    while True:
        valid_moves = get_moves()
        print("You're currently in room {}.".format(STATUS['locations']['player']))
        print("You can move {}".format(valid_moves))
        move = input("> ").upper()
        while move not in valid_moves:
            clear_screen()
            draw_dungeon()
            print("There's no door that way... ")
            move = input("> ").upper()
        else:
            clear_screen()
            move_player(move)
            draw_dungeon()


def init():
    clear_screen()
    print("Welcome to the dungeon!\n*************************")
    print("Find the sword to kill the monster, then escape the dungeon.")
    create_map(get_dungeon_size())
    run_game()


init()
