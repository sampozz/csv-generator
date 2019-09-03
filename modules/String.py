# Imports
from random import choice, randint

class String:

    def __init__(self, max_length=10, min_length=0):
        self.type = 'String'
        self.max_length = max_length
        self.min_length = min_length

    
    def generate(self):
        string = ''
        for i in range(randint(self.min_length, self.max_length)):
            string += choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return string