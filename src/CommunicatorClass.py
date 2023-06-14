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
from utils.Observer import WatchDog # TODO: this is a temporary solution, need to be improved

from src.SimulationDatabaseClass import SimulationDatabase
from src.DomainsWithGenDisClass import DomainsWithGenDis
from src.SensorsClass import Sensors
from src.MatplotlibCanvasClass import *

kSkip_Rows: int = 1

class Communicator:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.basic_magnification: float = 0.01 # TODO: this is only for the friday's meeting
        self.critical_value: float = 0.1 # TODO: this is only for the friday's meeting
        self.compared_point_sensors_index: int = 0 # TODO: this is only for the friday's meeting
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
    
    def __updateFlightTest(self, time_scale, gen_dis_responses: np.ndarray, factor: float) -> None:
        self.domains_with_gen_dis.addGenDisToUnstructuredGrid( \
            self.flight_test_grid, gen_dis_responses.T[-1], self.basic_magnification * factor)
        self.flight_test_time_domain_canvas.plot(time_scale, gen_dis_responses)
        pass
    
    def __updateSimulation(self, time_scale, gen_dis_responses: np.ndarray) -> None:
        self.domains_with_gen_dis.addGenDisToUnstructuredGrid( \
            self.simulation_grid, gen_dis_responses.T[-1], self.basic_magnification)
        self.simulation_time_domain_canvas.plot(time_scale, gen_dis_responses)
        pass
    
    def __getFactor(self, \
        flight_test_compared_point_value: float, simulation_compared_point_value: float) -> float:
        if np.abs(flight_test_compared_point_value) < self.critical_value:
            return 1.0
        else:
            return np.abs(simulation_compared_point_value / flight_test_compared_point_value)
            pass
        pass
    
    def __processSensorsFile(self, sensors_file: str) -> None:
        # * flight test's things
        height_in, mach_in = getHAndMaFromSensorsFile(sensors_file)
        sensors_data: np.ndarray = np.loadtxt(sensors_file, dtype=np.float64, skiprows=kSkip_Rows)
        flight_test_time_scale: np.ndarray = sensors_data.T[0]
        flight_test_time_scale -= flight_test_time_scale[0] # make the time scale start from 0
        latest_time: float = flight_test_time_scale[-1]
        flight_test_sensors_responses: np.ndarray = sensors_data[:][1:].T
        flight_test_compared_point_value: float = \
            flight_test_sensors_responses[self.compared_point_sensors_index][-1]
        flight_test_gen_dis_responses: np.ndarray = \
            self.sensors.getGenDisResponse(flight_test_sensors_responses)
        # * simulation's things
        simulation_time_scale, simulation_gen_dis_responses, simulation_compared_point_value, \
            height, mach = self.simulation_database.getDataAtGivenTime( \
                height_in, mach_in, latest_time)
        # factor
        factor: float = self.__getFactor(\
            flight_test_compared_point_value, simulation_compared_point_value)
        # * update
        self.__updateFlightTest(flight_test_time_scale, flight_test_gen_dis_responses, factor)
        self.__updateSimulation(simulation_time_scale, simulation_gen_dis_responses)
        # TODO: this is only for the friday's meeting
        print("height: " + str(height) + ", mach: " + str(mach) + ", factor: " + str(factor))
        pass
    
    def callBackForWatchDog(self, event_src_path: str) -> None:
        pure_file_name: str = event_src_path.split('\\')[-1].split('/')[-1]
        if isWatchDogSensorsFile(pure_file_name) == True:
            self.__processSensorsFile(event_src_path)
            pass
        pass
    
    def feedWatchDog(self, eyesore_path: str) -> None:
        self.watchdog: WatchDog = WatchDog(eyesore_path, self.callBackForWatchDog)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("src: CommunicatorClass.py is imported.")