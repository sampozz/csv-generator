# CSV Generator - v0.1

The purpose of this program is to create CSV files with all the data you need for development and testing.\
According with the GDPR, during the development process, personal information or sensitive data cannot be used. Therefore you should anonymize with fake information all the data before starting any activity that includes the use of it. \
The *CSV generator* helps you by creating all the data you need as you need it.

## Requirements
- Python 3.x
- docopt library (pip install docopt)   https://github.com/docopt/docopt
- exrex library (pip install exrex)     https://github.com/asciimoo/exrex

## Instructions
1 - Create the configuration of the data with `python generator.py config 'configuration-name'` and follow the guided process\
2 - Generate the csv file with `python generator.py start 'file-name.csv' -c 'configuration-name'`
