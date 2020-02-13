# begin imports
# external imports
import sys
# internal imports
from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Ask player for their name and initialize
player = Player(input('Enter your player name: '), room['outside'])

# TODO remove test print before deployment
print(player.name, player.current_room)

# TODO create a game rules printout

# Actual REPL game loop here
while True:
    print(player.current_room)
    action = input('What do you do: ')

    # input action/error check and action
    if len(action) == 1:
        # quit if q is entered
        if action == 'q':
            print(f'Thank you for playing {player.name}!')
            sys.exit()
        # move north action
        elif action == 'n':
            if player.current_room.n_to is None:
                print('That is not a valid direction.')
            else:
                player.current_room = player.current_room.n_to
                print(f'You walk to the north and '
                      f'enter the {player.current_room.name}')
        # move south action
        elif action == 's':
            if player.current_room.s_to is None:
                print('That is not a valid direction.')
            else:
                player.current_room = player.current_room.s_to
                print(f'You walk to the south and '
                      f'enter the {player.current_room.name}')
        # move east action
        elif action == 'e':
            if player.current_room.e_to is None:
                print('That is not a valid direction.')
            else:
                player.current_room = player.current_room.e_to
                print(f'You walk to the east and '
                      f'enter the {player.current_room.name}')
        # move west action
        elif action == 'w':
            if player.current_room.w_to is None:
                print('That is not a valid direction.')
            else:
                player.current_room = player.current_room.w_to
                print(f'You walk to the west and '
                      f'enter the {player.current_room.name}')
    break

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
