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


    def __edit(self, config_name, config):
        print('\nAvailable columns:')
        for col in config.keys():
            print(' - ' + col + ', type: ' + config[col].type)
        cmd = ''
        while cmd == '' or not 'exit' in cmd.lower():
            print('''\nType:
    edit <column-name>  # To edit the selected column
    new                 # To create a new column
    del <column-name>    # To delete the selected column
    exit                # To save the configuration and exit''')
            cmd = input('> ')
            if 'edit' in cmd.lower():
                pass
            elif 'new' in cmd.lower():
                col_name, col = self.__new_column(config_name)
                if col != None:
                    config[col_name] = col
            elif 'del' in cmd.lower():
                pass
            elif 'exit' in cmd.lower():
                break
            else:
                cmd = input('> ')
        dump(config, open(getcwd() + '/config/' + config_name + '/' + config_name + '.json', 'w'), cls=CustomJSONEncoder, indent=4)
        print('Configuration successfully saved!')
        return


    def create_configuration(self, config_name):
        '''Interactive and guided configuration
        '''
        # Check if configuration already exists
        if config_name in self.__configs.keys():
            print('''A configuration called "''' + config_name + '''" already exists!
[1] Edit
[2] Replace
[0] Exit''')
            selection = input('Select an option: ')
            while selection == '' or not selection in ['0', '1', '2']:
                selection = input('Select an option: ')
            if selection == '0':
                return
            elif selection == '1':
                self.__edit(config_name, self.__configs[config_name])
                return
            elif selection == '2':
                # Overwrite configuration
                rmtree(getcwd() + '/config/' + config_name)

        # Creating new configuration 
        creating_columns = {}
        print('\nCreating new configuration: ' + config_name)

        while True:
            add_new = input('\nAdd a new column? [Y/n] ')
            while not add_new.upper() in ['Y', 'N', '']:
                add_new = input('Add a new column? [Y/n] ')
            if add_new.upper() == 'N':
                break

            col_name, col = self.__new_column(config_name)
            if col != None:
                creating_columns[col_name] = col

        if len(creating_columns) == 0:
            print('No column has been created. Cannot save the configuration')
            return

        # Creating configuration
        mkdir(getcwd() + '/config/' + config_name)            
        dump(creating_columns, open(getcwd() + '/config/' + config_name + '/' + config_name + '.json', 'w'), cls=CustomJSONEncoder, indent=4)
        print('Configuration successfully created!')
        return


    def __new_column(self, config_name):
        # Creating new column
        col_name = input('\nInsert the name of the column: ')
        while col_name == '':
            col_name = input('Insert the name of the column: ')
        print('''What is the type of the column?
[1] Import from file
[2] Number
[3] Boolean
[4] String
[0] Exit''')
        col_type = input('Select an option: ')
        while col_type == '' or not col_type in ['0', '1', '2', '3', '4']:
            col_type = input('Select an option: ')
        try:
            ret = None
            # Column type: import from file
            if col_type == '1':
                ret = self.__file_conf(config_name)                 
            # Column type: number
            elif col_type == '2':        
                ret = self.__number_conf()          
            # Column type: boolean
            elif col_type == '3':
                ret = self.__boolean_conf()        
            # Column type: string
            elif col_type == '4':
                ret = self.__string_conf()
        except Exception as e:
            print('Error occured:', e)
        return col_name, ret  

    
    def __file_conf(self, config_name, current=None):
        if current == None:
            print('\nChoose the file from which the generator will get the values of the column randomly')
            file_name = input('Insert the file name: ')
            while not path.isfile(file_name):
                print('Cannot find the file "' + file_name + '"')
                file_name = input('Insert the file name: ')
            file_del = ','
            ignore_nl = 'true'
        else:
            file_name = path.basename(current.file_name)
            file_del = current.file_del
            ignore_nl = current.ignore_nl
        while True:
            print('\nEdit the configuration of the column (type: Import from file):')
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
        copyfile(file_name, getcwd() + '/config/' + config_name + '/' + path.basename(file_name))
        return File(config_name + '/' + path.basename(file_name), file_del, ignore_nl)


    def __number_conf(self, current=None):
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
        return Number(num_type, float(max_n), float(min_n))


    def __boolean_conf(self):
        print('\n' + 'Select the 2 options of the column (eg. [1, 0] - [True, False] - [Male, Female])')
        option_1 = input('What is the first option? ')
        option_2 = input('What is the second option? ')
        return Boolean(option_1, option_2)

    
    def __string_conf(self, current=None):
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
        return String(int(max_length), int(min_length))