# Imports
from random import random, randint

class Number:

    def __init__(self, type_n='random', max_n=9999, min_n=-9999):
        self.type = 'Number'
        self.type_n = type_n    # int | float | random
        self.max_n = max_n
        self.min_n = min_n
        if max_n < min_n:
            max_n, min_n = min_n, max_n

    
    def generate(self):
        n = randint(self.min_n, self.max_n) + random() 
        if self.type_n == 'int' or (self.type_n == 'random' and randint(0, 10) % 2):
            n = int(n)
        return str(n)