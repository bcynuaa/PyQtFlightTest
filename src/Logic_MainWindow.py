'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-08 16:39:26
 # @ license: Mozilla Public License 2.0
 # @ description: the class of logic of main window
 '''

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from config.Name import *
from config.MainWindowSettings import *

from ui.Ui_MainWindow import Ui_MainWindow

from src.CommunicatorClass import Communicator

class MainWindow(Ui_MainWindow, QMainWindow):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PyQtFlightTest")
        self.communicator: Communicator = Communicator()
        self.__initializeAll()
        pass
    
    def __initializeAll(self) -> None:
        self.__initializeTextBrowser()
        self.__initializeListWidget()
        self.__initializePyvista()
        self.__initilizeMatplotlib()
        pass
    
    def __writeToInfoTextBrowser(self, message: str) -> None:
        message = kSplit_Line + "\n" + getCurrentTime() + message + "\n" + kSplit_Line
        self.info_text_browser.append(message)
        self.info_text_browser.moveCursor(self.info_text_browser.textCursor().End)
        pass
    
    def __initializeTextBrowser(self) -> None:
        self.info_text_browser.clear()
        self.info_text_browser.setMaximumWidth(kText_Browser_Width)
        self.info_text_browser.setMarkdown("# Hello!\n")
        self.__writeToInfoTextBrowser(kWelcome_Info)
        self.info_text_browser.moveCursor(self.info_text_browser.textCursor().Start)
        pass
    
    def __initializeListWidget(self) -> None:
        # ref: 
        # - https://www.cnblogs.com/jyroy/p/9457882.html
        self.switch_stack_list_widget.setMaximumWidth(kList_View_Width)
        for key in kList_Widget_Dict:
            self.switch_stack_list_widget.insertItem(key, kList_Widget_Dict[key])
            pass
        self.switch_stack_list_widget.currentRowChanged.connect( \
            self.right_stacked_widget.setCurrentIndex)
        pass
    
    def __initializePyvista(self) -> None:
        # flight test group box
        self.main_page_flight_test_group_box.setMinimumHeight(kGroup_Box_Height)
        self.main_page_flight_test_group_box_layout = QVBoxLayout( \
            self.main_page_flight_test_group_box)
        self.main_page_flight_test_group_box_layout.addWidget( \
            self.communicator.flight_test_plotter)
        # simulation group box
        self.main_page_simulation_group_box.setMinimumHeight(kGroup_Box_Height)
        self.main_page_simulation_group_box_layout = QVBoxLayout( \
            self.main_page_simulation_group_box)
        self.main_page_simulation_group_box_layout.addWidget( \
            self.communicator.simulation_plotter)
        pass
    
    def __initilizeMatplotlib(self) -> None:
        # * flight test tabs
        self.main_page_flight_test_tab_widget.setCurrentIndex(0)
        self.main_page_flight_test_tab_widget.setMinimumHeight(kTab_Height)
        # * flight test time tab
        self.main_page_flight_test_tab_widget.setTabText(0, kTab_Name_Time_Domain)
        self.main_page_flight_test_time_domain_matplotlib_tab_layout = QVBoxLayout( \
            self.main_page_flight_test_time_tab)
        self.main_page_flight_test_time_domain_matplotlib_tab_layout.addWidget( \
            self.communicator.flight_test_time_domain_canvas.toolbar)
        self.main_page_flight_test_time_domain_matplotlib_tab_layout.addWidget( \
            self.communicator.flight_test_time_domain_canvas.canvas)
        # * flight test frequency tab
        self.main_page_flight_test_tab_widget.setTabText(1, kTab_Name_Frequency_Domain)
        self.main_page_flight_test_frequency_domain_matplotlib_tab_layout = QVBoxLayout( \
            self.main_page_flight_test_frequency_tab)
        self.main_page_flight_test_frequency_domain_matplotlib_tab_layout.addWidget( \
            self.communicator.flight_test_frequency_domain_canvas.toolbar)
        self.main_page_flight_test_frequency_domain_matplotlib_tab_layout.addWidget( \
            self.communicator.flight_test_frequency_domain_canvas.canvas)
        # * simulation tabs
        self.main_page_simulation_tab_widget.setCurrentIndex(0)
        self.main_page_simulation_tab_widget.setMinimumHeight(kTab_Height)
        # * simulation time tab
        self.main_page_simulation_tab_widget.setTabText(0, kTab_Name_Time_Domain)
        self.main_page_simulation_time_tab_layout = QVBoxLayout( \
            self.main_page_simulation_time_tab)
        self.main_page_simulation_time_tab_layout.addWidget( \
            self.communicator.simulation_time_domain_canvas.toolbar)
        self.main_page_simulation_time_tab_layout.addWidget( \
            self.communicator.simulation_time_domain_canvas.canvas)
        # * simulation frequency tab
        self.main_page_simulation_tab_widget.setTabText(1, kTab_Name_Frequency_Domain)
        self.main_page_simulation_frequency_tab_layout = QVBoxLayout( \
            self.main_page_simulation_frequency_tab)
        self.main_page_simulation_frequency_tab_layout.addWidget( \
            self.communicator.simulation_frequency_domain_canvas.toolbar)
        self.main_page_simulation_frequency_tab_layout.addWidget( \
            self.communicator.simulation_frequency_domain_canvas.canvas)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def closeEvent(self, event: QCloseEvent) -> None:
        # ref:
        # https://blog.csdn.net/weixin_43930603/article/details/104938939
        self.communicator.close()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass