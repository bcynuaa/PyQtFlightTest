'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-04 19:40:40
 # @ license: Mozilla Public License 2.0
 # @ description: the class of simulation database
 '''

import os
import numpy as np

from config.Name import kData_File_Format, kDefault_Simulation_Name

from utils.RegularExpression import getHAndMaFromDatabaseFile
from utils.SubDict import insertToSubDict

kSkip_Rows: int = 1

class SimulationDatabase:
    
    def __init__(self) -> None:
        pass
    
    def loadDatabaseFromPath(self, database_path: str) -> None:
        self.database_path: str = database_path
        self.__findDatabaseFilesFromPath()
        self.__buildDatabase()
        pass
    
    def __findDatabaseFilesFromPath(self) -> None:
        database_file_list: list = os.listdir(self.database_path)
        self.database_file_list: list = []
        for database_file in database_file_list:
            # check the file format
            if database_file.startswith(kDefault_Simulation_Name) and \
                database_file.endswith(kData_File_Format):
                self.database_file_list.append(database_file)
                pass
            pass
        # join the path
        self.database_file_list = [os.path.join(self.database_path, database_file) \
            for database_file in self.database_file_list]
        # sort the file list
        self.database_file_list.sort()
        pass
    
    def updateDatabaseFromSingularFile(self, database_file: str) -> None:
        height, mach = getHAndMaFromDatabaseFile(database_file)
        # insert the database file to the database_file_dict
        insertToSubDict(self.database_file_dict, height, mach, database_file)
        # insert the data to the database_dict
        insertToSubDict(self.database_dict, height, mach, \
            np.loadtxt(database_file, dtype=np.float, skiprows=kSkip_Rows))
        pass
    
    def __buildDatabase(self) -> None:
        # build the database as a dict
        # while the dict should look like: self.database_dict[height][mach] = data
        # what's more, the data should be a numpy array
        # at the same time, a database_file_dict should be built
        self.database_file_dict = dict()
        self.database_dict: dict = dict()
        for database_file in self.database_file_list:
            # update the database from this file
            self.updateDatabaseFromSingularFile(database_file)
            pass
        pass
    
    pass