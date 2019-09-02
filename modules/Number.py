# Imports
from random import random

class Number:

    def __init__(self, type_n='random', max_n=9999, min_n=-9999):
        self.type = 'Number'
        self.type_n = type_n    # int | float | random
        self.max_n = max_n
        self.min_n = min_n
        if max_n < min_n:
            max_n, min_n = min_n, max_n

    
    def generate(self):
        self.n = self.min_n + random() * self.max_n
        if self.type_n == 'int' or (self.type_n == 'random' and int(1 + random() * 10) % 2):
            self.n = int(self.n)
        return str(self.n)