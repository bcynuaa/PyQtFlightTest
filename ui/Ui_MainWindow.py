# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1160, 791)
        MainWindow.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")
        self.actionLoad_Domains = QAction(MainWindow)
        self.actionLoad_Domains.setObjectName(u"actionLoad_Domains")
        self.actionLoad_Simulation_Database = QAction(MainWindow)
        self.actionLoad_Simulation_Database.setObjectName(u"actionLoad_Simulation_Database")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.main_horizontal_layout = QHBoxLayout()
        self.main_horizontal_layout.setObjectName(u"main_horizontal_layout")
        self.left_vertical_layout = QVBoxLayout()
        self.left_vertical_layout.setObjectName(u"left_vertical_layout")
        self.switch_stack_list_widget = QListWidget(self.centralwidget)
        self.switch_stack_list_widget.setObjectName(u"switch_stack_list_widget")

        self.left_vertical_layout.addWidget(self.switch_stack_list_widget)

        self.info_text_browser = QTextBrowser(self.centralwidget)
        self.info_text_browser.setObjectName(u"info_text_browser")

        self.left_vertical_layout.addWidget(self.info_text_browser)


        self.main_horizontal_layout.addLayout(self.left_vertical_layout)

        self.right_stacked_widget = QStackedWidget(self.centralwidget)
        self.right_stacked_widget.setObjectName(u"right_stacked_widget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.verticalLayout_3 = QVBoxLayout(self.main_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_page_vertical_layout = QVBoxLayout()
        self.main_page_vertical_layout.setObjectName(u"main_page_vertical_layout")
        self.main_page_pyvista_horizontal_layout = QHBoxLayout()
        self.main_page_pyvista_horizontal_layout.setObjectName(u"main_page_pyvista_horizontal_layout")
        self.main_page_flight_test_group_box = QGroupBox(self.main_page)
        self.main_page_flight_test_group_box.setObjectName(u"main_page_flight_test_group_box")

        self.main_page_pyvista_horizontal_layout.addWidget(self.main_page_flight_test_group_box)

        self.main_page_simulation_group_box = QGroupBox(self.main_page)
        self.main_page_simulation_group_box.setObjectName(u"main_page_simulation_group_box")

        self.main_page_pyvista_horizontal_layout.addWidget(self.main_page_simulation_group_box)


        self.main_page_vertical_layout.addLayout(self.main_page_pyvista_horizontal_layout)

        self.main_page_tab_widget = QTabWidget(self.main_page)
        self.main_page_tab_widget.setObjectName(u"main_page_tab_widget")
        self.main_page_time_domain_matplotlib_tab = QWidget()
        self.main_page_time_domain_matplotlib_tab.setObjectName(u"main_page_time_domain_matplotlib_tab")
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.main_page_time_domain_matplotlib_tab.setFont(font)
        self.main_page_tab_widget.addTab(self.main_page_time_domain_matplotlib_tab, "")
        self.main_page_frequency_domain_matplotlib_tab = QWidget()
        self.main_page_frequency_domain_matplotlib_tab.setObjectName(u"main_page_frequency_domain_matplotlib_tab")
        self.main_page_frequency_domain_matplotlib_tab.setFont(font)
        self.main_page_tab_widget.addTab(self.main_page_frequency_domain_matplotlib_tab, "")

        self.main_page_vertical_layout.addWidget(self.main_page_tab_widget)


        self.verticalLayout_3.addLayout(self.main_page_vertical_layout)

        self.right_stacked_widget.addWidget(self.main_page)
        self.signal_page = QWidget()
        self.signal_page.setObjectName(u"signal_page")
        self.right_stacked_widget.addWidget(self.signal_page)
        self.simulation_page = QWidget()
        self.simulation_page.setObjectName(u"simulation_page")
        self.right_stacked_widget.addWidget(self.simulation_page)

        self.main_horizontal_layout.addWidget(self.right_stacked_widget)


        self.horizontalLayout_3.addLayout(self.main_horizontal_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1160, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuOption = QMenu(self.menubar)
        self.menuOption.setObjectName(u"menuOption")
        self.menuTool = QMenu(self.menubar)
        self.menuTool.setObjectName(u"menuTool")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menuFile.addAction(self.actionLoad_Domains)
        self.menuFile.addAction(self.actionLoad_Simulation_Database)

        self.retranslateUi(MainWindow)

        self.main_page_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad_Domains.setText(QCoreApplication.translate("MainWindow", u"Load Domains", None))
        self.actionLoad_Simulation_Database.setText(QCoreApplication.translate("MainWindow", u"Load Simulation Database", None))
        self.main_page_flight_test_group_box.setTitle(QCoreApplication.translate("MainWindow", u"\u8bd5\u98de\u6a21\u578b", None))
        self.main_page_simulation_group_box.setTitle(QCoreApplication.translate("MainWindow", u"\u4eff\u771f\u6a21\u578b", None))
        self.main_page_tab_widget.setTabText(self.main_page_tab_widget.indexOf(self.main_page_time_domain_matplotlib_tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.main_page_tab_widget.setTabText(self.main_page_tab_widget.indexOf(self.main_page_frequency_domain_matplotlib_tab), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuOption.setTitle(QCoreApplication.translate("MainWindow", u"Option", None))
        self.menuTool.setTitle(QCoreApplication.translate("MainWindow", u"Tool", None))
    # retranslateUi

