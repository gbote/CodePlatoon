import math

class Computer:
    def __init__(self, number_of_cores):
        self.number_of_cores = number_of_cores
    
    def compute(self):
        print(round(math.pi, self.number_of_cores))
