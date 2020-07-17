from room import Room
from player import Player
from item import Item
import time

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

items = {
    'sword': Item("Sword", "A rusty looking sword."),
    'ring': Item("Ring", "An ancient ring imbued with unknown power."),
    'light': Item("Lantern", "It has a little oil left."),
    'boots': Item("Boots", "As good as new"),
    'bone': Item("Bone", "It's over a foot long")
}

# Put the items in the rooms
room['outside'].addItem(items['boots'])
room['foyer'].addItem(items['sword'])
room['overlook'].addItem(items['light'])
room['narrow'].addItem(items['bone'])
room['treasure'].addItem(items['ring'])

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
player = Player("Eric", room['outside'])

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
choice = "new"
while choice != "q":
    if choice == "Invalid choice":
        print("Invalid choice: Please enter a direction(n, s, e, w)\n or a command(get/take/drop item_name)\n or i for inventory,\n or q to quit")
    else:
        time.sleep(1)
        print("\n-----------------\n")
        print("Room name:")
        player.printRoomName()
        print("\nRoom description:")
        player.printDescription()
        print("\nItems in the room:")
        player.room.printItems()
        print("\nYour items:")
        player.printItems()
    
    choice = input("\nEnter command: ")
    choice = player.command(choice)