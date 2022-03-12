from PySide6 import QtWidgets,QtCore,QtGui
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog)
from PySide6.QtGui import QImage
import sys
import cv2, imutils
import time
import numpy as np
import cv2
import pyshine as ps
from view.ui_mainwindow import Ui_MainWindow
from module import *
class MainGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initialize value:
        self.ui.filename = 'Snapshot '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png' # Will hold the image address location
        self.tmp = None # Will hold the temporary image for display
        self.brightness_value_now = 0 # Updated brightness value
        self.blur_value_now = 0 # Updated blur value
        self.fps=0
        self.started = False
        self.mode='cam'
        self.color_selected_text= 'Default'
        self.readBefore = False

        # Setting button Signal:
        self.ui.CameraMode.clicked.connect(lambda: UI_Function.videoMode(self))
        self.ui.ImageMode.clicked.connect(lambda: UI_Function.imageMode(self))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainGUI()
    window.show()
    app.exec()