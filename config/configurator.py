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
                columns[k] = String(v['max_length'], v['min_length'], v['regex'])
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
        mkdir(getcwd() + '/config/' + config_name)  

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
            rmtree(getcwd() + '/config/' + config_name)
            return
          
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
                ret = File()
                ret.config(config_name)      
            # Column type: number
            elif col_type == '2':        
                ret = Number()
                ret.config()      
            # Column type: boolean
            elif col_type == '3':
                ret = Boolean()
                ret.config()     
            # Column type: string
            elif col_type == '4':
                ret = String()
                ret.config()
        except Exception as e:
            print('Error occured:', e)
        return col_name, ret  