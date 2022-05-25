import random as r

class Dice:

    def __init__(self, values):
        self.current_value = '_'
        self.possible_vals = list(values)

    def __str__(self):
        return self.value

    def get_value(self):
        return self.current_value

    def roll(self):
        random_side = r.randint(0,5)
        self.current_value = self.possible_vals[random_side]