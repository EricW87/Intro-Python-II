# Write a class to hold player information, e.g. what room they are in
# currently.
import time

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.room = current_room
        self.list = []

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
    
    def command(self, choice):
        split_choice = choice.split()

        if(len(split_choice) == 1):
            return self.move(choice)
        elif(len(split_choice) == 2):
            self.action(split_choice)
            return "continue"
        else:
            print("Invalid Command: Please enter a direction(n,s,e,w)\n or a command(get/take/drop item_name")
            return "continue"

    def move(self, choice):
        if(choice == "n"):
            self.moveNorth()
        elif(choice == "s"):
            self.moveSouth()
        elif(choice == "e"):
            self.moveEast()
        elif(choice == "w"):
            self.moveWest()
        elif(choice == "i" or choice == "inventory"):
            self.printInventory()
        elif(choice != "q"):
            return "Invalid choice"

        return choice

    def action(self, split_choice):
        if(split_choice[0] == "get" or split_choice[0] == "take"):
            item = self.room.getItem(split_choice[1])

            if(item):
                self.addItem(item)
                self.room.removeItem(item)
                item.on_take()
            else:
                print("There is no " + split_choice[1] + " in this room.")
        elif(split_choice[0] == "drop"):
            item = self.getItem(split_choice[1])

            if(item):
                self.removeItem(item)
                self.room.addItem(item)
                item.on_drop()
            else:
                print("You are not holding the " + split_choice[1] + ".")
        else:
            print("Invalid Command: Please enter a direction(n,s,e,w)\n or a command(get/take/drop item_name")
    
    def printInventory(self):
        if(len(self.list) > 0):
            for i in self.list:
                print(i.getName() + " : " + i.getDescription())
                time.sleep(2)
        else:
            print("You have no items.")
            time.sleep(1)


    def printRoomName(self):
        if(self.room):
            print(self.room.printName())

    def printDescription(self):
        if(self.room):
            print(self.room.printDescription())
    
    def addItem(self, item):
        self.list.append(item)

    def removeItem(self, item):
        self.list.remove(item)
    
    def getItem(self, name):
        if(len(self.list) > 0):
            for i in self.list:
                if(i.name == name):
                    return i
        
        return False

    def printItems(self):
        if(len(self.list) > 0):
            [item.printName() for item in self.list]
        else:
            print("You are holding no items.")