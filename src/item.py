class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __eq__(self, other):
        self.name == other.name

    def on_take(self):
        print(f'You place the {self.name} in your inventory.')

    def on_drop(self):
        print(f'You drop the {self.name} on the floor of the room.')
