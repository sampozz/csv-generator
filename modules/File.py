# Imports
from os import path, getcwd
from random import choice

class File:

    def __init__(self, file_name, file_del=',', ignore_nl='true'):
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