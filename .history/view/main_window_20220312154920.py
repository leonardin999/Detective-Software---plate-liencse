# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#
# Subscribe to PyShine Youtube channel for more detail!

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QImage
import cv2, imutils
import time
import numpy as np
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import numpy as np
import cv2
import pyshine as ps


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(498, 522)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("images/H.png"))
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
		self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
		self.verticalSlider.setObjectName("verticalSlider")
		self.gridLayout.addWidget(self.verticalSlider, 0, 0, 1, 1)
		self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
		self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
		self.verticalSlider_2.setObjectName("verticalSlider_2")
		self.gridLayout.addWidget(self.verticalSlider_2, 0, 1, 1, 1)
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
		self.horizontalLayout.addLayout(self.gridLayout)
		self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout_2.addWidget(self.pushButton)
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout_2.addWidget(self.pushButton_2)
		self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
		spacerItem = QtWidgets.QSpacerItem(313, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow","license plate Recognition"))
		self.pushButton_2.setText(_translate("MainWindow", "Start"))
		self.label_2.setText(_translate("MainWindow", "Brightness"))
		self.label_3.setText(_translate("MainWindow", "Blur"))
		self.pushButton.setText(_translate("MainWindow", "Take picture"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
