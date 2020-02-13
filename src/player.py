class Player:
    def __init__(self, name, current_room,
                 items=[]
                 ):
        self.name = name
        self.current_room = current_room
        self.items = items

    def move(self, command):
        direction = command[0]
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print('That movement is currently not allowed')

    def inventory(self):
        if len(self.items) == 0:
            print('You currently have no items in your inventory.')
        else:
            print('You currently have ' +
                  ', '.join(
                      self.items[item].name for item in range(len(self.items))
                      ) +
                  ' in your inventory.')

    def on_take(self, item):
        hldr = None
        for x in range(len(self.current_room.items)):
            if self.current_room.items[x].name == item:
                hldr = x
        if hldr is not None:
            self.current_room.items[hldr].on_take()
            self.items.append(self.current_room.items.pop(hldr))
        else:
            print(f'You cannot find the {item} in this room.')

    def on_drop(self, item):
        hldr = None
        for x in range(len(self.items)):
            if self.items[x].name == item:
                hldr = x
        if hldr is not None:
            self.items[hldr].on_drop()
            self.current_room.items.append(self.items.pop(hldr))
        else:
            print(f'You do not have {item} in your inventory.')
