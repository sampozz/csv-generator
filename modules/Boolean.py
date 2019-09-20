# Imports
from random import randint

class Boolean():

    def __init__(self, option_1=True, option_2=False):
        self.type = 'Boolean'
        self.option_1 = option_1
        self.option_2 = option_2

    
    def generate(self):
        if randint(0, 10) % 2:
            return self.option_1
        return str(self.option_2)
    

    def config(self):
        print('\n' + 'Select the 2 options of the column (eg. [1, 0] - [True, False] - [Male, Female])')
        self.option_1 = input('What is the first option? ')
        self.option_2 = input('What is the second option? ')