class Player:
    def __init__(self, name, current_room,
                 items=[]
                 ):
        self.name = name
        self.current_room = current_room
        self.items = items

    def move(self, direction):
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print('That movement is currently not allowed')

    def inventory(self):
        if len(self.items.name) == 0:
            print('You currently have no items in your inventory.')
        else:
            print('You currently have ' +
                  ', '.join(item for item in self.items.name) +
                  ' in your inventory.')

    def on_take(self, item):
        if item in self.current_room.items.name:
            print(f'You place the {item} in your inventory.')
        else:
            print(f'You cannot find the {item} in this room.')

    def on_drop(self, item):
        if item in self.items.name:
            print(f'You drop the {item} on the floor of the room.')
        else:
            print(f'You do not have {item} in your inventory.')
