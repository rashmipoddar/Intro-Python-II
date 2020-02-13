from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Add items to room :
room['outside'].items = [Item('torch', 'show light'), Item('knife', 'protect self')]
room['foyer'].items = [Item('sword', 'old rusty sword')]
room['overlook'].itmes = [Item('shield', 'wear it')]
room['narrow'].items = [Item('chain', 'gold chain')]
room['treasure'].items = [Item('coins', 'gold coins')]

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('player1', room['outside'])
# print(type(player1))


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    print(player1.current_room.name)
    print(player1.current_room.description)
    for item in player1.current_room.items:
        print(item.name, item.description)
    for item in player1.items:
        print(f'item with player: {item.name}')
        print(f'item with player: {item.description}')
    # direction = input('Please choose n, s, e or w to continue or choose q to quit or items --- ').lower().split()
    direction = [val for val in input('Please choose n, s, e or w to continue or choose q to quit or items --- ').split()] 
    

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    print(direction)
    if len(direction) == 1:
        direction = direction[0]
        # print(direction)
        
        new_room = None
        if direction in ['n', 's', 'e', 'w', 'q', 'i', 'inventory']:
            if direction == 'q':
                print('Thank you for playing')
                print('Goodbye')
                exit()
            elif direction == 'inventory' or 'i':
                print('inside the conditional for inventory')
                for item in player1.items:
                    print(f'The items available for use are {item.name} {item.description}')
            elif direction == 'n':
                new_room = player1.current_room.n_to
            elif direction == 's':
                new_room = player1.current_room.s_to
            elif direction == 'e':
                new_room = player1.current_room.e_to
            elif direction == 'w':
                new_room = player1.current_room.w_to
            if new_room:  
                player1.current_room = new_room
            else:
                print('This is not a valid direction for this room')
        else:
            print('Please enter a valid input')

    else: 
        # print(direction)
        if direction[0] == 'take':
            for item in player1.current_room.items:
                if (item.name) == direction[1]:
                    print('Item available')
                    player1.current_room.items.remove(item)
                    player1.items.append(item)
                    Item.on_take(item)
                    for item in player1.items:
                        print(item.name)
                        print(item.description)
            else:
                print('Item not available in the room')
        elif direction[0] == 'drop':
            print('trying to drop an item')
            print(player1.items)
            if player1.items:
                for item in player1.items:
                    if(item.name) == direction[1]:
                        print('Item available with player')
                        player1.items.remove(item)
                        player1.current_room.items.append(item)
                        Item.on_drop(item)
                        for item in player1.items:
                            print(item.name)
                            print(item.description)
                    else:
                        print('Item not available with player')
            else:
                print('You do not have items to drop')