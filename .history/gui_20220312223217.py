from PySide6 import QtWidgets,QtCore,QtGui
from PySide6.QtWidgets import (QApplication, QMainWindow)
import sys

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
        self.mode=None
        self.readBefore = False

        # Setting button Signal:
        self.ui.CameraMode.clicked.connect(lambda: UI_Function.videoMode(self))
        self.ui.ImageMode.clicked.connect(lambda: UI_Function.imageMode(self))
        self.ui.btn_start.clicked.connect(lambda: UI_Function.load(self))
        self.ui.btn_save.clicked.connect(lambda: UI_Function.savePhoto(self))
        self.ui.BlurValue.valueChanged['int'].connect(lambda: UI_Function.brightness_value(self))
        self.ui.BrightValue.valueChanged['int'].connect(lambda: UI_Function.blur_value(self))


if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = MainGUI()
    window.show()
    app.exec()