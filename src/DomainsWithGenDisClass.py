'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-05 17:18:03
 # @ license: Mozilla Public License 2.0
 # @ description: this class of domains with general displacement
 # ! gen_dis means general displacement
 '''
 
import os
import numpy as np

from config.Name import kScalarsList, kDefault_Scalar

from config.PyvistaSettings import *

from utils.RegularExpression import getDomainFilesList

class DomainsWithGenDis:
    
    def __init__(self) -> None:
        pass
    
    def loadDomainFilesFromPath(self, data_path: str) -> None:
        self.data_path: str = data_path
        self.__findDomainFiles()
        self.__processDomainFiles()
        pass
    
    def __findDomainFiles(self) -> None:
        # find the domain files from the data path
        self.domain_files_list: list = getDomainFilesList(os.listdir(self.data_path))
        # join domain files path with data path
        self.domain_files_list = [os.path.join(self.data_path, domain_file) \
            for domain_file in self.domain_files_list]
        self.n_domains: int = len(self.domain_files_list)
        pass
    
    def __processDomainFiles(self) -> None:
        multi_blocks: pyvista.core.composite.MultiBlock = pyvista.MultiBlock()
        for domain_file in self.domain_files_list:
            multi_blocks.append( pyvista.get_reader(domain_file).read() )
            pass
        self.unstructured_grid: pyvista.UnstructuredGrid = multi_blocks.combine()
        self.n_points: int = self.unstructured_grid.n_points
        self.n_cells: int = self.unstructured_grid.n_cells
        self.basic_position: np.ndarray = np.array(self.unstructured_grid.points, dtype=np.float64)
        param: list = list( self.unstructured_grid.point_data.keys() )
        param.sort()
        self.n_gen_dis: int = len(param) // 3
        phi_list: list = []
        for j in range(self.n_gen_dis):
            phi_j: np.ndarray = np.array([self.n_points, 3], dtype=np.float64)
            for i in range(3):
                phi_j.T[i] = np.array( \
                    self.unstructured_grid.point_data[param[i*self.n_gen_dis + j]], dtype=np.float64)
                pass
            phi_list.append(phi_j)
            pass
        self.phi_3Darray: np.ndarray = np.array(phi_list, dtype=np.float64)
        self.unstructured_grid.point_data.clear()
        self.unstructured_grid.cell_data.clear()
        for scalar in kScalarsList:
            self.unstructured_grid.point_data[scalar] = np.zeros(self.n_points, dtype=np.float64)
            pass
        # self.unstructured_grid.active_scalars_name should be set as kDefault_Scalar
        self.unstructured_grid.set_active_scalars(kDefault_Scalar)
        pass
    
    def getGenDis(self, gen_dis_response: np.ndarray) -> np.ndarray:
        return (self.phi_3Darray.T @ gen_dis_response).T
        pass
    
    def getUnstructuredGrid(self, \
        gen_dis_response: np.ndarray, magnification: float) -> pyvista.UnstructuredGrid:
        unstructured_grid: pyvista.UnstructuredGrid = self.unstructured_grid.copy()
        gen_dis: np.ndarray = self.getGenDis(gen_dis_response)
        unstructured_grid.points += gen_dis * magnification
        for i in range(len(kScalarsList)):
            unstructured_grid.point_data[kScalarsList[i]] = gen_dis.T[i]
            pass
        pass
    
    pass

print("src: DomainsWithGenDisClass.py is imported.")