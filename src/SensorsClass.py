'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-07 17:38:53
 # @ license: Mozilla Public License 2.0
 # @ description: the class of sensors to mode
 '''

import numpy as np

from config.Name import kSplit_Line

from utils.RegularExpression import getHAndMaFromSensorsFile

class Sensors:
    
    """the class of sensors to mode
    - `sensors_mode_dis_file: str` -> the file of the sensors mode displacement
    - `mode_dis_matrix: np.ndarray` -> the matrix of the mode displacement
    - `n_sensors: int` -> the number of the sensors
    - `n_gen_dis: int` -> the number of the modes
    - `getGenDisResponse: function` -> the function of getting the general displacement response
    """
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        info: str = kSplit_Line + "\nSensors\n"
        info += "sensors mode displacement files: " + self.sensors_mode_dis_file + "\n"
        info += "number of sensors: " + str(self.n_sensors) + "\n"
        info += "number of general displacement: " + str(self.n_gen_dis) + "\n"
        info += kSplit_Line + "\n"
        return info
        pass
    
    def __repr__(self) -> str:
        return self.__str__()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadSensorsModeDisFile(self, sensors_mode_dis_file: str) -> None:
        self.sensors_mode_dis_file: str = sensors_mode_dis_file
        self.mode_dis_matrix: np.ndarray = np.loadtxt(sensors_mode_dis_file, dtype=np.float64)
        self.n_sensors, self.n_gen_dis = self.mode_dis_matrix.shape
        self.__determineGetGenDisResponseFunction()
        pass
    
    def __getGenDisResponse1(self, sensors_response: np.ndarray) -> np.ndarray:
        # sensors_response_i = mode_dis_matrix_ij gen_dis_response_j
        # and n_sensor = n_gen_dis
        # thus gen_dis_response_j = mode_dis_matrix_ij^-1 sensors_response_i
        # use np.linalg.solve to solve the equation
        return np.linalg.solve(self.mode_dis_matrix, sensors_response)
        pass
    
    def __getGenDisResponse2(self, sensors_response: np.ndarray) -> np.ndarray:
        # sensors_response_i = mode_dis_matrix_ij gen_dis_response_j
        # and n_sensor > n_gen_dis
        # thus gen_dis_response_j = mode_dis_matrix_ij^-1 sensors_response_i
        # use np.linalg.lstsq to solve the equation
        return np.linalg.lstsq(self.mode_dis_matrix, sensors_response, rcond=None)[0]
        pass
    
    def __getGenDisResponse3(self, sensors_response: np.ndarray) -> np.ndarray:
        # sensors_response_i = mode_dis_matrix_ij gen_dis_response_j
        # and n_sensor > n_gen_dis
        # thus gen_dis_response_j = mode_dis_matrix_ij^-1 sensors_response_i
        # the rest equals to 0
        # use np.linalg.lstsq to solve the equation
        gen_dis_response: np.ndarray = np.zeros(self.n_gen_dis, dtype=np.float64)
        gen_dis_response[0: self.n_sensors] = np.linalg.solve( \
            self.mode_dis_matrix[0: self.n_sensors, 0: self.n_sensors], sensors_response)
        return gen_dis_response
        pass
    
    def __determineGetGenDisResponseFunction(self) -> None:
        # here X_i = phi_ij q_j
        if self.n_sensors == self.n_gen_dis:
            self.getGenDisResponse: function = self.__getGenDisResponse1
            pass
        elif self.n_sensors > self.n_gen_dis:
            self.getGenDisResponse: function = self.__getGenDisResponse2
            pass
        elif self.n_sensors < self.n_gen_dis:
            self.getGenDisResponse: function = self.__getGenDisResponse3
            pass
        else:
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def connectToSensorsDataFile(self, sensors_data_file: str) -> None:
        self.sensors_data_file: str = sensors_data_file
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("src: SensorsToModeClass.py is imported.")