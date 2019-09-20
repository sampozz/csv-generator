# Imports
from os import path, getcwd
from random import choice
from shutil import copyfile

class File:

    def __init__(self, file_name='', file_del=',', ignore_nl='true'):
        self.type = 'File'
        self.file_name = file_name
        self.file_del = file_del
        self.ignore_nl = ignore_nl
        self.values = ''


    def generate(self):
        if self.values == '':
            if not path.isfile(getcwd() + '/config/' + self.file_name):
                raise Exception('Cannot find "' + self.file_name + '"')
            try:
                f = open(getcwd() + '/config/' + self.file_name, 'r')
                if self.ignore_nl == 'true':
                    file_read = f.read().replace('\n', '')
                else:
                    file_read = f.read()
                self.values = file_read.split(self.file_del)
                f.close()
            except Exception as e:
                raise Exception('A problem occured while opening the file "' + self.file_name + '"')
        return choice(self.values)


    def config(self, config_name, current=None):
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

        copyfile(getcwd() + '/' + file_name, getcwd() + '/config/' + config_name + '/' + path.basename(file_name))
        self.file_name = config_name + '/' + file_name
        self.file_del = file_del
        self.ignore_nl = ignore_nl