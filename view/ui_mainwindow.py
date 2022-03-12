# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(990, 522)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.display = QLabel(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(10, 10, 640, 480))
        self.display.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(660, 40, 321, 141))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 301, 91))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.BlurValue = QSlider(self.widget)
        self.BlurValue.setObjectName(u"BlurValue")
        self.BlurValue.setOrientation(Qt.Horizontal)
        self.BlurValue.setTickPosition(QSlider.TicksBelow)

        self.gridLayout.addWidget(self.BlurValue, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.BrightValue = QSlider(self.widget)
        self.BrightValue.setObjectName(u"BrightValue")
        self.BrightValue.setOrientation(Qt.Horizontal)
        self.BrightValue.setTickPosition(QSlider.TicksBelow)

        self.gridLayout.addWidget(self.BrightValue, 1, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(660, 190, 321, 121))
        self.widget1 = QWidget(self.groupBox_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 20, 301, 91))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.ThesholdValue_1 = QSlider(self.widget1)
        self.ThesholdValue_1.setObjectName(u"ThesholdValue_1")
        self.ThesholdValue_1.setMaximum(255)
        self.ThesholdValue_1.setOrientation(Qt.Horizontal)
        self.ThesholdValue_1.setTickPosition(QSlider.TicksBelow)

        self.gridLayout_2.addWidget(self.ThesholdValue_1, 0, 1, 1, 1)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.ThreshValue_2 = QSlider(self.widget1)
        self.ThreshValue_2.setObjectName(u"ThreshValue_2")
        self.ThreshValue_2.setMaximum(255)
        self.ThreshValue_2.setSingleStep(1)
        self.ThreshValue_2.setOrientation(Qt.Horizontal)
        self.ThreshValue_2.setTickPosition(QSlider.TicksBelow)

        self.gridLayout_2.addWidget(self.ThreshValue_2, 1, 1, 1, 1)

        self.CameraMode = QRadioButton(self.centralwidget)
        self.CameraMode.setObjectName(u"CameraMode")
        self.CameraMode.setGeometry(QRect(670, 10, 111, 20))
        self.ImageMode = QRadioButton(self.centralwidget)
        self.ImageMode.setObjectName(u"ImageMode")
        self.ImageMode.setGeometry(QRect(790, 10, 89, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(670, 470, 71, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(670, 440, 81, 21))
        self.modeStatus = QLabel(self.centralwidget)
        self.modeStatus.setObjectName(u"modeStatus")
        self.modeStatus.setGeometry(QRect(750, 440, 161, 21))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(660, 320, 311, 101))
        self.btn_save = QPushButton(self.groupBox_3)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(10, 30, 141, 61))
        self.btn_start = QPushButton(self.groupBox_3)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(160, 30, 141, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"License Plate Recognition", None))
        self.display.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Video/Image Quality", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Blur", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Threshold Adjustment", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Threshold 1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Threshold 2", None))
        self.CameraMode.setText(QCoreApplication.translate("MainWindow", u"Camera Mode", None))
        self.ImageMode.setText(QCoreApplication.translate("MainWindow", u"Image Mode", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version: 1.0.0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current Mode:", None))
        self.modeStatus.setText(QCoreApplication.translate("MainWindow", u"............................", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u" Action", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save Picture", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start Analysis", None))
    # retranslateUi

