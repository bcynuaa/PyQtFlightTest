'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-07 19:07:07
 # @ license: Mozilla Public License 2.0
 # @ description: the class of communicator, which is a middle layer between the GUI and the backend
 '''
 
from pyvistaqt import BackgroundPlotter, QtInteractor
 
from config.PyvistaSettings import *
from config.MatplotlibSettings import *

from src.SimulationDatabaseClass import SimulationDatabase
from src.DomainsWithGenDisClass import DomainsWithGenDis
from src.SensorsClass import Sensors

class Communicator:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.basic_magnification: float = 0.01
        self.simulation_database: SimulationDatabase = SimulationDatabase()
        self.domains_with_gen_dis: DomainsWithGenDis = DomainsWithGenDis()
        self.sensors: Sensors = Sensors()
        self.__initializePyvista()
        pass
    
    def __initializePyvista(self) -> None:
        self.flight_test_plotter: QtInteractor = QtInteractor()
        self.simulation_plotter: QtInteractor = QtInteractor()
        self.flight_test_plotter.add_mesh(pyvista.Sphere())
        self.simulation_plotter.add_mesh(pyvista.Sphere())
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadDomainFilesFromPath(self, data_path: str) -> None:
        self.domains_with_gen_dis.loadDomainFilesFromPath(data_path)
        self.flight_test_grid: pyvista.UnstructuredGrid = \
            self.domains_with_gen_dis.unstructured_grid.copy()
        self.simulation_grid: pyvista.UnstructuredGrid = \
            self.domains_with_gen_dis.unstructured_grid.copy()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass