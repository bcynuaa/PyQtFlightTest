'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-07 19:07:07
 # @ license: Mozilla Public License 2.0
 # @ description: the class of communicator, which is a middle layer between the GUI and the backend
 '''
 
from pyvistaqt import QtInteractor, BackgroundPlotter
 
from config.PyvistaSettings import *
from config.MatplotlibSettings import *

from src.SimulationDatabaseClass import SimulationDatabase
from src.DomainsWithGenDisClass import DomainsWithGenDis
from src.SensorsClass import Sensors
from src.MatplotlibCanvasClass import *

class Communicator:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.basic_magnification: float = 0.01
        self.whether_database_loaded: bool = False
        self.whether_domains_loaded: bool = False
        self.whether_sensors_mode_dis_loaded: bool = False
        self.simulation_database: SimulationDatabase = SimulationDatabase()
        self.domains_with_gen_dis: DomainsWithGenDis = DomainsWithGenDis()
        self.sensors: Sensors = Sensors()
        self.__initializePyvistaPlotter()
        self.__initializeMatplotlibCanvas()
        pass
    
    def __initializePyvistaPlotter(self) -> None:
        # flight test plotter
        self.flight_test_plotter: QtInteractor = QtInteractor()
        self.__addMeshToFlightTestPlotter(pyvista.Sphere())
        # simulation plotter
        self.simulation_plotter: QtInteractor = QtInteractor()
        self.__addMeshToSimulationPlotter(pyvista.Sphere())
        pass
    
    def __initializeMatplotlibCanvas(self) -> None:
        self.time_domain_canvas: TimeDomainCanvas = TimeDomainCanvas()
        self.frequency_domain_canvas: FrequencyDomainCanvas = FrequencyDomainCanvas()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __addMeshToFlightTestPlotter(self, mesh) -> None:
        self.flight_test_plotter.add_mesh(mesh) # TODO: pyvista settings
        self.flight_test_plotter.add_axes()
        self.flight_test_plotter.add_bounding_box()
        pass
    
    def __addMeshToSimulationPlotter(self, mesh) -> None:
        self.simulation_plotter.add_mesh(mesh) # TODO: pyvista settings
        self.simulation_plotter.add_axes()
        self.simulation_plotter.add_bounding_box()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadDatabaseFromPath(self, data_path: str) -> None:
        self.simulation_database.loadDatabaseFromPath(data_path)
        self.whether_database_loaded = True
        pass
    
    def __refreshPyvistaPlotter(self) -> None:
        # flight test plotter
        self.flight_test_plotter.clear()
        self.__addMeshToFlightTestPlotter(self.flight_test_grid)
        # simulation plotter
        self.simulation_plotter.clear()
        self.__addMeshToSimulationPlotter(self.simulation_grid)
        pass
    
    def loadDomainFilesFromPath(self, data_path: str) -> None:
        self.domains_with_gen_dis.loadDomainFilesFromPath(data_path)
        self.flight_test_grid: pyvista.UnstructuredGrid = \
            self.domains_with_gen_dis.unstructured_grid.copy()
        self.simulation_grid: pyvista.UnstructuredGrid = \
            self.domains_with_gen_dis.unstructured_grid.copy()
        self.__refreshPyvistaPlotter()
        self.whether_domains_loaded = True
        pass
    
    def loadSensorsModeDisFile(self, sensors_mode_dis_file: str) -> None:
        self.sensors.loadSensorsModeDisFile(sensors_mode_dis_file)
        self.whether_sensors_mode_dis_loaded = True
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def close(self) -> None:
        self.flight_test_plotter.close()
        self.simulation_plotter.close()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("src: CommunicatorClass.py is imported.")