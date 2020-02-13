class Room:
    # define initial conditions
    def __init__(
        self, name, description,
        items=[],
        n_to=None,
        s_to=None,
        e_to=None,
        w_to=None
            ):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    # define the string output when class is called
    '''
    The output of the string methon sould be:
    The room player is in -new line
    The room discription.
    '''
    def __str__(self):
        # create item printout
        if len(self.items) == 0:
            item_printout = 'There are currently no items in this room.'
        else:
            item_printout = ('The item(s) in this room are ' +
                             ' '.join(self.items[x].name
                                      for x in range(len(self.items))) + '.'
                             )
        return (f'You are currently in the {self.name}.\n \n'
                f'{self.description}\n \n'
                f'{item_printout}\n'
                )
