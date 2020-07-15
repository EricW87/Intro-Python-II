# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.room = current_room

    def moveNorth(self):
        if(self.room.n_to):
            self.room = self.room.n_to
            print("You move North")
        else:
            print("You can't go that way.")

    def moveSouth(self):
        if(self.room.s_to):
            self.room = self.room.s_to
            print("You move South")
        else:
            print("You can't go that way.")

    def moveEast(self):
        if(self.room.e_to):
            self.room = self.room.e_to
            print("You move East")
        else:
            print("You can't go that way.")

    def moveWest(self):
        if(self.room.w_to):
            self.room = self.room.w_to
            print("You move West")
        else:
            print("You can't go that way.")
    
    def move(self, choice):
        if(choice == "n"):
            self.moveNorth()
        elif(choice == "s"):
            self.moveSouth()
        elif(choice == "e"):
            self.moveEast()
        elif(choice == "w"):
            self.moveWest()
        elif(choice != "q"):
            return "Invalid choice"

        return choice


    def printRoomName(self):
        if(self.room):
            print("You are " + self.room.printName())

    def printDescription(self):
        if(self.room):
            print(self.room.printDescription())