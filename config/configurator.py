"""Data Anonymizer configurator

Documentation in generator.py
"""

# Imports
from shutil import copyfile, rmtree
from json import dump, load
from os import walk, path, mkdir, getcwd
from random import random
from modules.Number import Number
from modules.Boolean import Boolean
from modules.String import String
from modules.File import File
from modules.CustomJSONEncoder import CustomJSONEncoder

column_types = '''What is the type of the column?
[1] Import from file
[2] Number
[3] Boolean
[4] String
[0] Save configuration and exit
'''

class Configurator:

    def __init__(self):
        self.search_configs()


    def search_configs(self):
        '''Import available configurations
        '''
        self.__configs = {}
        for root, dirs, files in walk(getcwd() + '/config/', topdown=False):
            for name in dirs:
                if not name == '__pycache__':
                    with open(getcwd() + '/config/' + name + '/' + name + '.json', 'r') as f:
                        self.__configs[name] = self.CustomJSONDecoder(load(f))


    def print_configs(self):
        '''print the list of available configurations 
        '''
        for key in self.__configs.keys():
            st = key + ' -- '
            for col in self.__configs[key].keys():
                st += col + ', '
            print(st[:-2])


    def use_config(self, config_name):
        '''Return the selected configuration
        '''
        if config_name in self.__configs.keys():
            return self.__configs[config_name]
        raise Exception('Cannot find the config "' + config_name + '"')


    def export(self):
        pass

    
    def CustomJSONDecoder(self, json_obj):
        '''Decode a json configuration 
        '''
        columns = {}
        for k, v in json_obj.items():
            if v['type'] == 'File':
                columns[k] = File(v['file_name'], v['file_del'], v['ignore_nl'])
            elif v['type'] == 'Number':
                columns[k] = Number(v['type_n'], v['max_n'], v['min_n'])
            elif v['type'] == 'Boolean':
                columns[k] = Boolean(v['option_1'], v['option_2'])
            elif v['type'] == 'String':
                columns[k] = String(v['max_length'], v['min_length'])
            else:
                raise Exception('Could not import configuration')
        return columns


    def create(self, config_name):
        '''Interactive and guided configuration
        '''
        # Check if configuration already exists
        if config_name in self.__configs.keys():
            replace = input('A configuration called "' + config_name + '" already exists!\nDo you want to replace it? [Y/n] ')
            while not replace.upper() in ['Y', 'N', '']:
                replace = input('Do you want to replace it? [Y/n] ')
            if replace.upper() == 'N':
                return
            # Overwrite configuration
            rmtree(getcwd() + '/config/' + config_name)

        # Creating new configuration 
        creating_columns = {}
        files = []
        print('\nCreating new configuration: ' + config_name)

        while True:
            add_new = input('\nAdd a new column? [Y/n] ')
            while not add_new.upper() in ['Y', 'N', '']:
                add_new = input('Add a new column? [Y/n] ')
            if add_new.upper() == 'N':
                break

            # Creating new column
            col_name = input('\nInsert the name of the column: ')
            while col_name == '':
                col_name = input('Insert the name of the column: ')
            col_type = input('\n' + column_types + 'Select an option: ')
            while col_type == '' or not col_type.isdigit() or not col_type in ['0', '1', '2', '3', '4']:
                col_type = input('\n' + column_types + 'Select an option: ')

            # Column type: import from file
            if col_type == '1':
                print('\nChoose the file from which the generator will get the values of the column randomly')
                file_name = input('Insert the file name: ')
                while not path.isfile(file_name):
                    print('Cannot find the file "' + file_name + '"')
                    file_name = input('Insert the file name: ')
                file_del = ','
                ignore_nl = 'true'
                while True:
                    print('\nEdit the configuration of the column "' + col_name + '":')
                    print('''
[1] File name: ''' + file_name + '''
[2] Value delimiter: ''' + file_del + '''
[3] Ignore new line char (\\n): ''' + ignore_nl + '''
[0] Save column configuration and exit''')
                    selection = input('Select an option: ')
                    while selection == '' or not selection.isdigit():
                        selection = input('Select an option: ')
                    if selection == '0':
                        break
                    elif selection == '1':
                        file_name = input('Insert the file name: ')
                        while not path.isfile(file_name):
                            print('Cannot find the file "' + file_name + '"')
                            file_name = input('Insert the file name: ')
                    elif selection == '2':
                        file_del = input('\nSelect the value delimiter: ')
                    elif selection == '3':
                        selection = input('\nIgnore new line? [Y/n]: ')
                        while not selection.lower() in ['y', 'n', '']:
                            selection = input('\nIgnore new line? [Y/n]: ')
                        if selection.lower() == 'n':
                            ignore_nl = 'false'
                        else:
                            ignore_nl = 'true'

                files.append(file_name)
                creating_columns[col_name] = File(config_name + '/' + path.basename(file_name), file_del, ignore_nl)
                continue
                    
            # Column type: number
            if col_type == '2':
                num_type = 'integer'
                max_n = '9999'
                min_n = '-9999'
                while True:
                    print('\nEdit the configuration of the column "' + col_name + '":')
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
                
                creating_columns[col_name] = Number(num_type, float(max_n), float(min_n))
                continue                

            # Column type: boolean
            if col_type == '3':
                print('\n' + 'Select the 2 options of the column (eg. [1, 0] - [True, False] - [Male, Female])')
                option_1 = input('What is the first option? ')
                option_2 = input('What is the second option? ')

                creating_columns[col_name] = Boolean(option_1, option_2)
                continue
            
            # Column type: string
            if col_type == '4':
                max_length = '10'
                min_length = '0'
                while True:
                    print('\nEdit the configuration of the column "' + col_name + '":')
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

                creating_columns[col_name] = String(int(max_length), int(min_length))
                continue

        if len(creating_columns) == 0:
            print('No column has been created. Cannot save the configuration')
            return

        # Creating configuration
        mkdir(getcwd() + '/config/' + config_name)
        for file in files:
            copyfile(file, getcwd() + '/config/' + config_name + '/' + path.basename(file))
        dump(creating_columns, open(getcwd() + '/config/' + config_name + '/' + config_name + '.json', 'w'), cls=CustomJSONEncoder, indent=4)
        print('Configuration successfully created!')
        return