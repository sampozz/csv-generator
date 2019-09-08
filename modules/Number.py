# Imports
from random import uniform, randint

class Number:

    def __init__(self, type_n='random', max_n=9999, min_n=-9999):
        self.type = 'Number'
        self.type_n = type_n    # integer | float | random
        self.max_n = max_n
        self.min_n = min_n

    
    def generate(self):
        if self.max_n < self.min_n:
            self.max_n, self.min_n = self.min_n, self.max_n
        n = uniform(self.min_n, self.max_n)
        if self.type_n == 'integer' or (self.type_n == 'random' and randint(0, 10) % 2):
            n = int(n)
        return str(n)