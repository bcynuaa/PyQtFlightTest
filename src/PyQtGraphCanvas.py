'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-07-08 09:58:30
 # @ license: Mozilla Public License 2.0
 # @ description: the class of pyqtgraph canvas to replace matplotlib canvas, for perfomance issue
 '''

import numpy as np
import pyqtgraph as pg

from pglive.sources.live_plot_widget import LivePlotWidget
from pglive.sources.live_plot import LiveLinePlot
from pglive.sources.data_connector import DataConnector

max_length: int = 2000

# give me 50 different colors' lists in pyqtgraph

colors_list: list = [
    # "b", "g", "r", "c", "m", "y", "k",
    pg.mkColor(0, 0, 255), pg.mkColor(0, 255, 0), pg.mkColor(255, 0, 0), pg.mkColor(0, 255, 255), pg.mkColor(255, 0, 255), pg.mkColor(255, 255, 0), pg.mkColor(0, 0, 0), pg.mkColor(255, 255, 255),
    pg.mkColor(0, 0, 128), pg.mkColor(0, 128, 0), pg.mkColor(128, 0, 0), pg.mkColor(0, 128, 128), pg.mkColor(128, 0, 128), pg.mkColor(128, 128, 0), pg.mkColor(128, 128, 128), pg.mkColor(128, 128, 128),
    pg.mkColor(0, 0, 64), pg.mkColor(0, 64, 0), pg.mkColor(64, 0, 0), pg.mkColor(0, 64, 64), pg.mkColor(64, 0, 64), pg.mkColor(64, 64, 0), pg.mkColor(64, 64, 64), pg.mkColor(64, 64, 64),
    pg.mkColor(0, 0, 32), pg.mkColor(0, 32, 0), pg.mkColor(32, 0, 0), pg.mkColor(0, 32, 32), pg.mkColor(32, 0, 32), pg.mkColor(32, 32, 0), pg.mkColor(32, 32, 32), pg.mkColor(32, 32, 32),
    pg.mkColor(0, 0, 16), pg.mkColor(0, 16, 0), pg.mkColor(16, 0, 0), pg.mkColor(0, 16, 16), pg.mkColor(16, 0, 16), pg.mkColor(16, 16, 0), pg.mkColor(16, 16, 16), pg.mkColor(16, 16, 16),
    pg.mkColor(0, 0, 8), pg.mkColor(0, 8, 0), pg.mkColor(8, 0, 0), pg.mkColor(0, 8, 8), pg.mkColor(8, 0, 8), pg.mkColor(8, 8, 0), pg.mkColor(8, 8, 8), pg.mkColor(8, 8, 8),
    pg.mkColor(0, 0, 4), pg.mkColor(0, 4, 0), pg.mkColor(4, 0, 0), pg.mkColor(0, 4, 4), pg.mkColor(4, 0, 4), pg.mkColor(4, 4, 0), pg.mkColor(4, 4, 4), pg.mkColor(4, 4, 4),
    pg.mkColor(0, 0, 2), pg.mkColor(0, 2, 0), pg.mkColor(2, 0, 0), pg.mkColor(0, 2, 2), pg.mkColor(2, 0, 2), pg.mkColor(2, 2, 0), pg.mkColor(2, 2, 2), pg.mkColor(2, 2, 2),
]

class TimeDomainCanvas:
    
    def __init__(self) -> None:
        # self.canvas: pg.PlotWidget = pg.PlotWidget(enableMenu=True, background=pg.mkColor(255, 255, 255))
        self.canvas: LivePlotWidget = LivePlotWidget(enableMenu=True, background=pg.mkColor(255, 255, 255))
        self.canvas.enableMouse(False)
        pass
    
    def initializeCurves(self, n_curves: int) -> None:
        self.curves: list = []
        self.data_connectors: list = []
        for i in range(n_curves):
            curve: LiveLinePlot = LiveLinePlot(
                    pen=({"color": colors_list[i], "width": 1}),
                    skipFiniteCheck=True)
            data_connector: DataConnector = DataConnector(curve, max_points=max_length)
            self.canvas.addItem(curve)
            self.curves.append(curve)
            self.data_connectors.append(data_connector)
            # data_connector.cb_set_data(
            pass
        pass
    
    def plot(self, x: np.ndarray, y: np.ndarray) -> None:
        # clear curves
        for i in range(len(self.curves)):
            self.curves[i].clear()
            length: int = min(max_length, len(x))
            self.data_connectors[i].cb_set_data(y[i][len(x)-length: len(x)], x[len(x)-length: len(x)])
            pass       
        pass
    
    # def initializeCurves(self, n_curves: int) -> None:
    #     # x: np.ndarray = np.linspace(0, 10, 101)
    #     # y: np.ndarray = np.sin(x)
    #     self.curves: list = []
    #     self.n_curves: int = n_curves
    #     for i in range(n_curves):
    #         # alpha should be
    #         curve: pg.PlotCurveItem = pg.PlotCurveItem(
    #             pen=(
    #                 {"color": colors_list[i], "width": 1}
    #             ),
    #             skipFiniteCheck=True
    #         )
    #         # curve: LiveLinePlot = LiveLinePlot(
    #         #     pen=(
    #         #         {"color": colors_list[i], "width": 1}),
    #         #         skipFiniteCheck=True
    #         # )
    #         self.canvas.addItem(curve)
    #         # curve.setData(x, y+i)
    #         self.curves.append(curve)
    #         pass
    #     print("initialize curves")
    #     pass
    
    # def plot(self, x: np.ndarray, y: np.ndarray) -> None:
    #     # clear curves
    #     for i in range(self.n_curves):
    #         self.curves[i].clear()
    #         length: int = min(max_length, len(x))
    #         self.curves[i].setData(x[len(x)-length: len(x)], y[i][len(x)-length: len(x)])
    #         pass
    #     self.canvas.setRange(xRange=[x[len(x)-length], x[len(x)-1]], update=True)
    #     pass
    
    pass