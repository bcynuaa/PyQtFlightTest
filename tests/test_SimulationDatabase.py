'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-05 14:13:15
 # @ license: Mozilla Public License 2.0
 # @ description: the file is used to test SimulationDatabase
 '''

import pprint

from src.SimulationDatabaseClass import SimulationDatabase

database_file_path: str = "..//..//TestData//ProjectFlightTest2//SimulationDatabase//"
sd: SimulationDatabase = SimulationDatabase()
sd.loadDatabaseFromPath(database_file_path)

print("the database files:")
for key in sd.database_files_dict.keys():
    print(key, "-> height(km):")
    pprint.pprint(sd.database_files_dict[key])
    pass
print("the database's H and Ma", sd.getDatabaseDictKeys())
print("when H=9.4 and Ma=0.89, the cloest database is: ", sd.getDatabaseFileDictData(9.4, 0.89))
print("the database's table's shape: ", sd.getDatabaseDictData(9.4, 0.89)[0].shape)

# the result should be:

# the database files:
# 9.5 -> height(km):
# {0.8: '..//..//TestData//ProjectFlightTest2//SimulationDatabase//simulation2.dat',
#  0.94: '..//..//TestData//ProjectFlightTest2//SimulationDatabase//simulation1.dat',
#  1.3: '..//..//TestData//ProjectFlightTest2//SimulationDatabase//simulation3.dat'}
# the database's H and Ma [(9.5, 0.94), (9.5, 0.8), (9.5, 1.3)]
# when H=9.4 and Ma=0.89, the cloest database is:  ('..//..//TestData//ProjectFlightTest2//SimulationDatabase//simulation1.dat', 9.5, 0.94)
# the database's table's shape:  (6269, 7)