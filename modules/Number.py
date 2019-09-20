# Imports
from random import uniform, randint

class Number:

    def __init__(self, type_n='random', max_n=9999, min_n=-9999):
        self.type = 'Number'
        self.type_n = type_n    # integer | float | random
        self.max_n = float(max_n)
        self.min_n = float(min_n)

    
    def generate(self):
        if self.max_n < self.min_n:
            self.max_n, self.min_n = self.min_n, self.max_n
        n = uniform(self.min_n, self.max_n)
        if self.type_n == 'integer' or (self.type_n == 'random' and randint(0, 10) % 2):
            n = int(n)
        return str(n)

    
    def config(self, current=None):
        if current == None:
            num_type = 'integer'
            max_n = '9999'
            min_n = '-9999'
        else:
            num_type = current.num_type
            max_n = current.max_n
            min_n = current.min_n
        while True:
            print('\nEdit the configuration of the column (type: Number):')
            print('''
[1] Number type: ''' + num_type + '''
[2] Maximum number: ''' + max_n + '''
[3] Minimum number: ''' + min_n + '''
[0] Save column configuration and exit''')
            selection = input('Select an option: ')
            while selection == '' or not selection.isdigit():
                selection = input('Select an option: ')
            if selection == '0':
                break
            elif selection == '1':
                selection = input('\nSelect a type [integer, float, random]: ')
                while not selection in ['integer', 'float', 'random']:
                    selection = input('Select a type [integer, float, random]: ')
                num_type = selection
            elif selection == '2':
                selection = input('\nSelect the maximum number: ')
                while not selection.replace('-', '').replace('.', '').isdigit():
                    selection = input('\nSelect the maximum number: ')
                max_n = selection
            elif selection == '3':
                selection = input('\nSelect the minimum number: ')
                while not selection.replace('-', '').replace('.', '').isdigit():
                    selection = input('\nSelect the minimum number: ')
                min_n = selection

        self.type_n = num_type
        self.max_n = max_n
        self.min_n = min_n