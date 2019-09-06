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
[0] Import from file
[1] Number
[2] Boolean
[3] String
'''

class Configurator:

    def __init__(self):
        self.search_configs()


    def search_configs(self):
        self.__configs = {}
        for root, dirs, files in walk(getcwd() + '/config/', topdown=False):
            for name in dirs:
                if not name == '__pycache__':
                    with open(getcwd() + '/config/' + name + '/' + name + '.json', 'r') as f:
                        self.__configs[name] = self.CustomJSONDecoder(load(f))


    def print_configs(self):
        for key in self.__configs.keys():
            st = key + ' -- '
            for col in self.__configs[key].keys():
                st += col + ', '
            print(st[:-2])


    def use_config(self, config_name):
        if config_name in self.__configs.keys():
            return self.__configs[config_name]
        raise Exception('Cannot find the config "' + config_name + '"')


    def export(self):
        pass

    
    def CustomJSONDecoder(self, json_obj):
        columns = {}
        for k, v in json_obj.items():
            if v['type'] == 'File':
                columns[k] = File(v['file_name'], v['file_del'])
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
            col_type = input('\n' + column_types + 'Select the number: ')
            while col_type == '' or not col_type.isdigit() or not col_type in ['0', '1', '2']:
                col_type = input('\n' + column_types + 'Select the number: ')

            # Column type: import from file
            print('\nChoose the file from which the generator will get the values of the column randomly')
            if col_type == '0':
                file_name = input('Insert the file name: ')
                while not path.isfile(file_name):
                    print('Cannot find the file "' + file_name + '"')
                    file_name = input('Insert the file name: ')

                file_del = input('Insert the delimiter character (default: ","): ')
                if file_del == '':
                    file_del = ','
                files.append(file_name)

                creating_columns[col_name] = File(config_name + '/' + path.basename(file_name), file_del)
                continue
                    
            # Column type: number
            if col_type == '1':
                num_type = 'a'
                while not num_type.isdigit() or not num_type in ['0', '1', '2']:
                    num_type = input('\n' + '''Integer or floating point? 
[0] Integer
[1] Floating point
[2] Random (default)
Select the number: ''')
                if num_type == '0':
                    num_type = 'int'
                elif num_type == '1':
                    num_type = 'float'
                else:
                    num_type = 'random'
                print('Selected: ' + num_type)

                max_n = input('Select the maximum number [default: 9999]: ')
                if max_n == '':
                    max_n = '9999'
                while not max_n.isdigit():
                    print('It has to be a number...')
                    max_n = input('Select the maximum number [default: 9999]: ')
                
                min_n = input('Select the minimum number [default: -9999]: ')
                if min_n == '':
                    min_n = '-9999'
                while not min_n.isdigit() and min_n != '-9999':
                    print('It has to be a number...')
                    min_n = input('Select the minimum number [default: -9999]: ')

                creating_columns[col_name] = Number(num_type, float(max_n), float(min_n))
                continue

            # Column type: boolean
            if col_type == '2':
                print('\n' + 'Select the 2 options of the column (eg. [1, 0] - [True, False] - [Male, Female])')
                option_1 = input('What is the first option? ')
                option_2 = input('What is the second option? ')

                creating_columns[col_name] = Boolean(option_1, option_2)
                continue
            
            # Column type: string
            if col_type == '3':
                max_length = input('Select the maximum length [default: 10]: ')
                if max_length == '':
                    max_length = '10'
                while not max_length.isdigit():
                    print('It has to be a number...')
                    max_length = input('Select the maximum length [default: 10]: ')
                
                min_length = input('Select the minimum length [default: 0]: ')
                if min_length == '':
                    min_length = '0'
                while not min_length.isdigit():
                    print('It has to be a number...')
                    min_length = input('Select the minimum length [default: 0]: ')

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