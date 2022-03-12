from PySide6 import QtWidgets,QtCore,QtGui
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog)
from PySide6.QtGui import QImage
import sys
import cv2, imutils
import time
import numpy as np
import cv2
import pyshine as ps
from .view.ui_mainwindow import Ui_MainWindow

class MainGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainGUI()
    window.show()
    app.exec()