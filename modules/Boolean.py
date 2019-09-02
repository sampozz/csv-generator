# Imports
from random import random

class Boolean():

    def __init__(self, option_1=True, option_2=False):
        self.type = 'Boolean'
        self.option_1 = option_1
        self.option_2 = option_2

    
    def generate(self):
        if int(random(0, 10)) % 2:
            return self.option_1
        return self.option_2