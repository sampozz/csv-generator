# Imports
from exrex import getone

class String:

    def __init__(self, max_length=10, min_length=0, regex='None'):
        self.type = 'String'
        self.max_length = int(max_length)
        self.min_length = int(min_length)
        self.regex = regex

    
    def generate(self):
        if self.regex.lower() == 'none':    
            if self.min_length > self.max_length:
                self.min_length, self.max_length = self.max_length, self.min_length
            string = getone('[ -~]{' + str(self.min_length) + ',' + str(self.max_length) + '}')
        else:
            string = getone(self.regex)
        return string
        

    def config(self, current=None):
        if current == None:
            max_length = '10'
            min_length = '0'
            regex = 'None'
        else:
            max_length = current.max_length
            min_length = current.min_length
            regex = current.regex
        while True:
            print('\nEdit the configuration of the column (type: String):')
            print('''
[1] Regex match ('None' to ignore): ''' + regex + '''
[2] Maximum length (if regex is None): ''' + max_length + '''
[3] Minimum length (if regex is None): ''' + min_length + '''
[0] Save column configuration and exit''')
            selection = input('Select an option: ')
            while selection == '' or not selection.isdigit():
                selection = input('Select an option: ')
            if selection == '0':
                break
            elif selection == '2':
                selection = input('\nSelect the maximum length: ')
                while not selection.isdigit():
                    selection = input('\nSelect the maximum length: ')
                max_length = selection
            elif selection == '3':
                selection = input('\nSelect the minimum length: ')
                while not selection.isdigit():
                    selection = input('\nSelect the minimum length: ')
                min_length = selection
            elif selection == '1':
                regex = input('\nInsert regular expression (\'None\' to ignore): ')

        self.max_length = max_length
        self.min_length = min_length