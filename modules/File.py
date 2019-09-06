# Imports
from os import path, getcwd
from random import choice

class File:

    def __init__(self, file_name, file_del=','):
        self.type = 'File'
        self.file_name = file_name
        self.file_del = file_del
        self.values = ''


    def generate(self):
        if self.values == '':
            if not path.isfile(getcwd() + '/config/' + self.file_name):
                raise Exception('Cannot find "' + self.file_name + '"')
            f = open(getcwd() + '/config/' + self.file_name, 'r')
            self.values = f.read().split(self.file_del)
            f.close()
        return choice(self.values)