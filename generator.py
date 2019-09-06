#!/usr/bin/env python3
"""Data Anonymizer - v0.1

Usage:
  generator.py start <file_name> --use-config=<configuration_name> [-n=<rows_number>]
  generator.py config <configuration_name> 
  generator.py list
  generator.py export <configuration_name> <file_name>
  generator.py (-h | --help)
  generator.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --use-config=configuration_name
                Specify the configuration to use
  -n=rows_number
                Specify the number of rows to write [default: 100]
"""

# Imports
from docopt import docopt
from config.Configurator import Configurator
from modules.start import start_generator
import textwrap

# Information
__author__      = 'Samuele Pozzani'
__version__     = '0.1 - 2019/08/29'
__manteiner__   = 'Samuele Pozzani'
__email__       = 'samuele.pozzani@gmail.com'
__license__     = 'MIT License'


def main():
    arguments = docopt(__doc__, version='Data Anonymizer - v0.1')
    
    #try:
    config = Configurator()
    if arguments['start']:
        start_generator(arguments['<file_name>'], config.use_config(arguments['--use-config']))
    elif arguments['config']:
        config.create(arguments['<configuration_name>'])
    elif arguments['list']:
        config.print_configs()
    elif arguments['export']:
        pass
    # except Exception as e:
    #     print("Fatal error! ", e)
    # finally:
    #     print("Program terminated! Goodbye.\n")


if __name__ == '__main__':
    main()
