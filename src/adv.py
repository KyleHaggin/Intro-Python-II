# begin imports
# external imports
import sys
# internal imports
from room import Room
from player import Player
from item import Item

# Declare all the items
items = {
    'gold': Item('gold', 'A valuable gold coin.'),
    'sword': Item('sword', 'A chipped iron sword.'),
}


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from
west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Populate rooms with items
room['treasure'].items.extend([items['gold']])

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Ask player for their name and initialize starting room
player = Player(input('Enter your player name: '), room['outside'])
# Add items to player inventory
player.items.extend([items['sword']])
# TODO create a game rules printout

# Actual REPL game loop here
while True:
    # print the current room, its description, and items in the room
    print('\n')
    print(player.current_room)
    action = input('What do you do: ')

    # add new lines to help with output readability
    print('\n \n')

    # input action/error check and action
    # turn everything into lower case to preven errors and bloat
    action = action.lower()
    # split input to determine action type
    action = action.split()
    # [verb] actions
    if len(action) == 1:
        # quit if q is entered
        if action[0] in ['q', 'quit']:
            print(f'Thank you for playing {player.name}!')
            sys.exit()
        # Check inventory
        elif action[0] in ['i', 'inventory']:
            player.inventory()
        # Movement commands
        elif action[0] in [
            'n', 'north',
            's', 'south',
            'e', 'east',
            'w', 'west'
                    ]:
            player.move(action[0])
        # Error check
        else:
            print('Not a valid one word entry.')
    # [verb] [object] actions
    elif len(action) == 2:
        # Pickup item in current room to inventory
        if action[0] in ['get', 'take']:
            player.on_take(action[1])
        # Drop item in inventory to current room
        elif action[0] in ['drop']:
            player.on_drop(action[1])
        # [verb] [object] move command
        elif action[0] in ['move', 'go']:
            player.move(action[1])
        elif action[0] in['describe', 'd']:
            player.describe_item(action[1])
        # Error check
        else:
            print('Not a valid two word entry.')
    else:
        print('Not a valid entry.')
