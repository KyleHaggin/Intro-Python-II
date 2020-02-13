# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # define initial conditions
    def __init__(
        self, name, description,
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

    # define the string output when class is called
    '''
    The output of the string methon sould be:
    The room player is in -new line
    The room discription.
    '''
    def __str__(self):
        return (f'You are currently in the {self.name}.\n'
                f'{self.description}'
                )
