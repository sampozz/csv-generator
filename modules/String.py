# Imports
from random import choice, randint

class String:

    def __init__(self, max_length=10, min_length=0):
        self.type = 'String'
        self.max_length = float(max_length)
        self.min_length = float(min_length)

    
    def generate(self):
        string = ''
        for i in range(randint(self.min_length, self.max_length)):
            string += choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return string

    
    def config(self, current=None):
        if current == None:
            max_length = '10'
            min_length = '0'
        else:
            max_length = current.max_length
            min_length = current.min_length
        while True:
            print('\nEdit the configuration of the column (type: String):')
            print('''
[1] Maximum length: ''' + max_length + '''
[2] Minimum length: ''' + min_length + '''
[0] Save column configuration and exit''')
            selection = input('Select an option: ')
            while selection == '' or not selection.isdigit():
                selection = input('Select an option: ')
            if selection == '0':
                break
            elif selection == '1':
                selection = input('\nSelect the maximum length: ')
                while not selection.isdigit():
                    selection = input('\nSelect the maximum length: ')
                max_length = selection
            elif selection == '2':
                selection = input('\nSelect the minimum length: ')
                while not selection.isdigit():
                    selection = input('\nSelect the minimum length: ')
                min_length = selection

        self.max_length = max_length
        self.min_length = min_length