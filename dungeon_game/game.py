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
    'weapon': 'unarmed',
    'locations': {
        'player': [1, 1],
        'monster': None,
        'weapon': None,
        'door': None
    }
}


def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_map(grid_size):
    """Draws a map of selected size"""
    STATUS['game_grid'] = []  # Could be a tuple?
    STATUS['grid_size'] = grid_size
    x_coord = 1
    y_coord = 1
    grid_size_counter = grid_size * grid_size
    while grid_size_counter:
        STATUS['game_grid'].append([x_coord, y_coord])
        x_coord += 1
        if x_coord == grid_size + 1:
            y_coord += 1
            x_coord = 1
        grid_size_counter -= 1


def generate_random_coord(grid_size):
    """Generate random coordinate"""
    return random.randrange(1, grid_size)

print(generate_random_coord)


def set_locations():
    """Set the locations of the weapon and the monster"""
    STATUS['locations']['monster']


def get_locations():
    """Returns the locations dict."""
    return STATUS['locations']

# Too many returns - wy is this bad style?
def get_moves(character):
    """Check available moves"""
    if character == 'player':
        x_coord = get_locations()['player'][0]
        y_coord = get_locations()['player'][1]
    elif character == 'monster':
        x_coord = get_locations()['monster'][0]
        y_coord = get_locations()['monster'][1]
    if x_coord == 1 and y_coord == 1:
        return ['S', 'D']
    elif x_coord == STATUS['grid_size'] and y_coord == STATUS['grid_size']:
        return ['W', 'A']
    elif x_coord == 1 and y_coord == STATUS['grid_size']:
        return ['W', 'D']
    elif x_coord == STATUS['grid_size'] and y_coord == 1:
        return ['S', 'A']
    elif x_coord == 1:
        return ['W', 'D', 'S']
    elif y_coord == 1:
        return ['D', 'S', 'A']
    elif x_coord == STATUS['grid_size']:
        return ['W', 'S', 'A']
    elif y_coord == STATUS['grid_size']:
        return ['W', 'A', 'D']
    else:
        return ['W', 'D', 'S', 'A']


def move_player(move):
    """Moves the player sprite on the grid"""
    if move == 'W':
        STATUS['locations']['player'][1] -= 1
    elif move == 'S':
        STATUS['locations']['player'][1] += 1
    elif move == 'A':
        STATUS['locations']['player'][0] -= 1
    elif move == 'D':
        STATUS['locations']['player'][0] += 1
    print(STATUS['locations']['player'])


def move_monster():
    """Moves the monster a random square every turn"""


def get_dungeon_size():
    """Collect the player's choice of dungeon size. """
    size = input("Choose the size of the dungeon... (4 - 24)\n>")
    size = int(size)
    while size < 4 or size > 24:
        print("Pick a number between four and 24.")
        size = input("Choose the size of the dungeon... (4 - 24)")
    return size


def draw_dungeon():
    """Print the dungeon to the screen"""
    grid_size = STATUS['grid_size']
    cells = STATUS['game_grid']
    player = get_locations()['player']
    print(" _" * grid_size)
    tile = "|{}"
    for cell in cells:
        x, y = cell  #Surely this is just unpacking?
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


def monster_check():
    """Check how close the monster is"""
    player = get_locations()['player']
    monster = get_locations()['monster']
    if player[0] + 1 == monster[0]:
        return "There are sounds of scuffling to the right.."
    elif player[0] - 1 == monster[0]:
        return "There's a noise coing from ahead!"
    elif player[1] + 1 == monster[1]:
        return "Something's snuffling behind."
    elif player[1] - 1 == monster[1]:
        return "There's a scratching to the left.."
    else:
        return "Everything is quiet."


def parse_moves(moves):
    """Convert the actual move keys into legible text"""
    possible_moves = []
    for move in moves:
        if move == 'W':
            possible_moves.append('UP')
        elif move == 'D':
            possible_moves.append('RIGHT')
        elif move == 'S':
            possible_moves.append('DOWN')
        elif move == 'A':
            possible_moves.append('LEFT')
    return possible_moves


def run_game():
    """Main game control flow"""
    while True:
        draw_dungeon()
        valid_moves = get_moves('player')
        print("You're currently in room {}.".format(STATUS['locations']['player']))
        print("You are currently {}.".format(STATUS['weapon']))
        print("{}".format(monster_check()))
        print("You can move {}".format(', '.join(parse_moves(valid_moves))))
        move = input("> ").upper()
        while move not in valid_moves:
            clear_screen()
            print("There's no door that way... ")
            draw_dungeon()
            move = input("> ").upper()
            clear_screen()
        else:
            clear_screen()
            move_player(move)


def init():
    """Initiliase the game"""
    clear_screen()
    print("Welcome to the dungeon!\n**************************")
    print("Find the sword to kill the monster, then escape the dungeon.")
    create_map(get_dungeon_size())
    run_game()


init()
