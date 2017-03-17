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
        'player': [3, 4],
        'monster': None,
        'door': None
    }
}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def draw_map(grid_size):
    """Draws a map of selected size"""
    game_grid = []  # Could be a tuple?
    STATUS['grid_size'] = grid_size
    x_coord = 1
    y_coord = 1
    grid_size_counter = grid_size * grid_size
    while (grid_size_counter):
        game_grid.append([x_coord, y_coord])
        x_coord += 1
        if (x_coord == grid_size + 1):
            y_coord += 1
            x_coord = 1
        grid_size_counter -= 1
    print(game_grid)


draw_map(5)

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
        return ['RIGHT', 'DOWN']
    elif (x_coord == STATUS['grid_size'] and y_coord == STATUS['grid_size']):
        return ['UP', 'LEFT']
    elif (x_coord == 1 and y_coord == STATUS['grid_size']):
        return ['UP', 'RIGHT']
    elif (x_coord == STATUS['grid_size'] and y_coord == 1):
        return ['DOWN', 'RIGHT']
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
        STATUS['locations']['player'][1] += 1
    elif (move == 'DOWN'):
        STATUS['locations']['player'][1] -= 1
    elif (move == 'LEFT'):
        STATUS['locations']['player'][0] -= 1
    else:
        STATUS['locations']['player'][1] += 1
    print(STATUS['locations']['player'])


def options():
    print("Welcome to the dungeon!\n*************************")
    print("Find the sword to kill the monster, then escape the dungeon.")
    while True:
        valid_moves = get_moves()
        print("You're currently in room {}.".format(STATUS['locations']['player']))
        print("You can move {}".format(valid_moves))

        move = input("> ").upper()
        if move not in valid_moves:
            print("Please try again: ")
            move = input("> ").upper()
        else:
            move_player(move)


options()
