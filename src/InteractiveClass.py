'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-07 19:07:07
 # @ license: Mozilla Public License 2.0
 # @ description: the class of interactive, which is a middle layer between the GUI and the backend
 '''
 
from config.PyvistaSettings import *
from config.MatplotlibSettings import *

from src.SimulationDatabaseClass import SimulationDatabase
from src.DomainsWithGenDisClass import DomainsWithGenDis
from src.SensorsClass import Sensors

class Interactive:
    
    def __init__(self) -> None:
        self.simulation_database: SimulationDatabase = SimulationDatabase()
        self.domains_with_gen_dis: DomainsWithGenDis = DomainsWithGenDis()
        self.sensors: Sensors = Sensors()
        pass
    
    pass