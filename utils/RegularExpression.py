'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-04 20:22:18
 # @ license: Mozilla Public License 2.0
 # @ description: the file contains the regular expression used in the program
 '''

import re

def getHAndMaFromDatabaseFile(database_file: str) -> tuple:
    # get the first line of the file, which should look like 'H9.5Ma0.94'
    with open(database_file, 'r') as f:
        first_line: str = f.readline()
        pass
    # get the H and Ma
    H: float = float(re.findall(r'H\d+\.\d+', first_line)[0][1:])
    Ma: float = float(re.findall(r'Ma\d+\.\d+', first_line)[0][2:])
    return H, Ma
    pass