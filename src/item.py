
class Item:
    def __init__(self, name="none", description="none"):
        self.name = name
        self.description = description

    def printName(self):
        print(self.name)

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def on_take(self):
        print("You pick up the " + self.name)

    def on_drop(self):
        print("You drop the " + self.name)