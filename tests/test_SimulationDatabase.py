'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-05 14:13:15
 # @ license: Mozilla Public License 2.0
 # @ description: this file is to test SimulationDatabase
 '''

from src.SimulationDatabase import SimulationDatabase

database_file_path: str = "..//..//TestData//ProjectFlightTest2//SimulationDatabase//"
sd: SimulationDatabase = SimulationDatabase()
sd.loadDatabaseFromPath(database_file_path)

print(sd.database_file_dict)
print(sd.getDatabaseDictKeys())
print(sd.getDatabaseFileDictData(9.4, 0.87))
print(sd.getDatabaseDictData(9.4, 0.87))