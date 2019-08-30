#!/usr/bin/env python3
"""Data Anonymizer - v0.1

Usage:
  anonymizer.py start <file_name> --use-config=<configuration_name> [-n=<rows_number>]
  anonymizer.py config <configuration_name> 
  anonymizer.py list
  anonymizer.py export <configuration_name> <file_name>
  anonymizer.py (-h | --help)
  anonymizer.py --version

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
from config.configurator import *
import textwrap

# Information
__author__      = 'Samuele Pozzani'
__version__     = '0.1 - 2019/08/29'
__manteiner__   = 'Samuele Pozzani'
__email__       = 'samuele.pozzani@gmail.com'
__license__     = 'MIT License'


def main():
    arguments = docopt(__doc__, version='Data Anonymizer - v0.1')
    
    try:
        if arguments['start']:
            pass
        elif arguments['config']:
            pass
        elif arguments['list']:
            pass
        elif arguments['export']:
            pass
    except Exception as e:
        print("Fatal error! ", e)
    finally:
        print("Program terminated! Goodbye.\n")


if __name__ == '__main__':
    main()
