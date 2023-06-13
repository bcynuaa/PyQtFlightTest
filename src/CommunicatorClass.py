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

from utils.RegularExpression import isWatchDogSensorsFile, getHAndMaFromSensorsFile

from src.SimulationDatabaseClass import SimulationDatabase
from src.DomainsWithGenDisClass import DomainsWithGenDis
from src.SensorsClass import Sensors
from src.MatplotlibCanvasClass import *

class Communicator:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.basic_magnification: float = 0.01
        self.critical_value: float = 10.0
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
        self.flight_test_time_domain_canvas: TimeDomainCanvas = TimeDomainCanvas()
        self.flight_test_frequency_domain_canvas: FrequencyDomainCanvas = FrequencyDomainCanvas()
        self.simulation_time_domain_canvas: TimeDomainCanvas = TimeDomainCanvas()
        self.simulation_frequency_domain_canvas: FrequencyDomainCanvas = FrequencyDomainCanvas()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __addMeshToPlotter(self, plotter: QtInteractor, mesh) -> None:
        plotter.add_mesh(mesh, \
            opacity=pyvista.global_theme.opacity, \
                cmap=pyvista.global_theme.cmap)
        plotter.add_axes()
        plotter.add_bounding_box()
        plotter.show_grid()
        pass
    
    def __addMeshToFlightTestPlotter(self, mesh) -> None:
        self.__addMeshToPlotter(self.flight_test_plotter, mesh)
        pass
    
    def __addMeshToSimulationPlotter(self, mesh) -> None:
        self.__addMeshToPlotter(self.simulation_plotter, mesh)
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
    
    # TODO: below is only for the friday's meeting
    
    def __processSensorsFile(self, sensors_file: str) -> None:
        height_in, mach_in = getHAndMaFromSensorsFile(sensors_file)
        sensors_data: np.ndarray = np.loadtxt(sensors_file, dtype=np.float64, skiprows=1).T
        sensors_data[0] -= sensors_data[0][0] # set the initial time to 0
        time_latest: float = sensors_data[0][-1] # get the latest time
        gen_dis_response_simulation: np.ndarray = \
            self.simulation_database.getGenDisResponse(height_in, mach_in, time_latest)
        pass
    
    def callBackForWatchDog(self, event_src_path: str) -> None:
        pure_file_name: str = event_src_path.split('\\')[-1].split('/')[0]
        if isWatchDogSensorsFile(pure_file_name) == True:
            self.__processSensorsFile(event_src_path)
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("src: CommunicatorClass.py is imported.")