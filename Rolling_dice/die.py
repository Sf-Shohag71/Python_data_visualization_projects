from random import randint

class Die:
    """A class represent single die"""
    def __init__(self, num_sides=6):
        """Assume six sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return random number between 1 and number of side"""
        return randint(1, self.num_sides)