'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-04 19:06:09
 # @ license: Mozilla Public License 2.0
 # @ description: the main entry of the program
 '''

import sys
import os

os.environ["QT_API"] = "pyside2"

from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui

from qt_material import apply_stylesheet

from src.Logic_MainWindow import *

if __name__ == "__main__":
    # add this line to support high dpi
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # TODO: choose suitable qt material theme
    # from qt_material import list_themes
    # list_themes()
    apply_stylesheet(app, theme="light_blue.xml")
    window.show()
    sys.exit(app.exec_())
    pass