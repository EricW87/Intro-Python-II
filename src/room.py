# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.list = []
    
    def printName(self):
        return self.name

    def printDescription(self):
        return self.description

    def addItem(self, item):
        self.list.append(item)

    def printItems(self):
        if(len(self.list) > 0):
            [item.printName() for item in self.list]
        else:
            print("No Items in this room")

    def getItem(self, name):
        if(len(self.list) > 0):
            for i in self.list:
                if(i.name == name):
                    return i
        
        return False

    def removeItem(self, item):
        self.list.remove(item)
