
from distutils.command.build import build
from http.client import OK
from re import M
from PySide6.QtWidgets import (QFileDialog,QMessageBox)
from PySide6.QtGui import QImage, QPixmap
from gui import *
import os
import cv2, imutils
import time
import numpy as np
import pyshine as ps

class UI_Function(MainGUI):

    def imageMode(self):
        """ This function will select the image mode"""
        self.mode='image'
        self.ui.modeStatus.setText('Image Activated')

    def videoMode(self):
        """ This function will select the video mode"""
        self.mode='cam'
        self.ui.modeStatus.setText('Video Activated')


    def load(self):
        """ This function will load the camera device, image file or video file, obtain the image
            and set it to label using the setPhoto function
        """
        video_file_ext = ['.MP4','.AVI']
        image_file_ext = ['.PNG','.JPG','.JPEG','.BMP','.TIFF']

        ext=None
        if self.started==False:
            if self.mode=='image':
                self.ui.filename = QFileDialog.getOpenFileName(filter="Image or Video(mp4) (*.*)")[0]
                ext = os.path.splitext(self.filename)[1].upper()


        if self.started:
            self.started=False
            self.ui.btn_start.setText('Start Analysis')
        else:
            self.started=True
            self.ui.btn_start.setText('Stop Analysis')


        if self.mode=='cam':
            vid = cv2.VideoCapture(0)
        else:
            if ext in video_file_ext:
                vid = cv2.VideoCapture(self.ui.filename)

        if self.mode==None:
            UI_Function.notification(self)
            return


        cnt=0
        frames_to_count=20
        st = 0
        self.fps=0
        self.ui.btn_save.setEnabled(True)
        self.ui.CameraMode.setEnabled(False)
        self.ui.ImageMode.setEnabled(False)
        while(True):
            if self.mode == 'cam':
                _, self.image = vid.read()
                self.image = imutils.resize(self.image,height=480)
            else:
                if ext in video_file_ext:
                    try:
                        _, self.image = vid.read()
                        self.image = imutils.resize(self.image,width=480)
                    except Exception as e:
                        print(e)
                        pass
                elif ext in image_file_ext:
                    if self.readBefore == False:
                        self.image = cv2.imread(self.filename,cv2.IMREAD_COLOR)
                        self.image = imutils.resize(self.image,height=480)
                        self.readBefore	= True

            try:
                UI_Function.update(self)
            except Exception as e:
                print(e)
                self.started=False
                self.ui.btn_start.setText('Start')


            key = cv2.waitKey(1) & 0xFF
            time.sleep(0.01)

            if self.started==False:
                self.ui.CameraMode.setEnabled(True)
                self.ui.ImageMode.setEnabled(True)
                self.readBefore	= False
                break
                print('Loop break')
            #QtWidgets.QApplication.processEvents()

    def setPhoto(self,image):
        """ This function will take image input and resize it
            only for display purpose and convert it to QImage
            to set at the label.
        """
        self.tmp = image
        image = imutils.resize(image,height=480)
        text  =  'Live'
        rgb= [227,38,54]
        image = ps.putBText(image,text,text_offset_x=10,text_offset_y=10,font_scale=1,background_RGB=rgb,text_RGB=(255,255,255))

        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.ui.display.setPixmap(QPixmap.fromImage(image))

    def brightness_value(self,value):
        """ This function will take value from the slider
            for the brightness from 0 to 99
        """
        try:
            self.brightness_value_now = value
            UI_Function.update(self)
        except Exception as e:
            print(e)
            pass


    def blur_value(self,value):
        """ This function will take value from the slider
            for the blur from 0 to 99 """
        try:
            self.blur_value_now = value
            self.update()
        except Exception as e:
            print(e)
            pass

    def changeBrightness(self,img,value):
        """ This function will take an image (img) and the brightness
            value. It will perform the brightness change using OpenCv
            and after split, will merge the img and return it.
        """
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        lim = 255 - value
        v[v>lim] = 255
        v[v<=lim] += value
        final_hsv = cv2.merge((h,s,v))
        img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
        return img

    def changeBlur(self,img,value):
        """ This function will take the img image and blur values as inputs.
            After perform blur operation using opencv function, it returns
            the image img.
        """
        kernel_size = (value+1,value+1) # +1 is to avoid 0
        img = cv2.blur(img,kernel_size)
        return img

    def update(self):
        """ This function will update the photo according to the
            current values of blur and brightness and set it to photo label.
        """
        img = UI_Function.changeBrightness(self,self.image,self.brightness_value_now)
        img = UI_Function.changeBlur(self,img,self.blur_value_now)

        # Here we add display text to the image
        text  =  'FPS: '+str(self.fps)
        img = ps.putBText(img,text,text_offset_x=20,text_offset_y=50,vspace=20,hspace=10, font_scale=1,background_RGB=(10,20,222),text_RGB=(255,255,255))
        text = str(time.strftime("%H:%M %p"))
        img = ps.putBText(img,text,text_offset_x=self.image.shape[1]-200,text_offset_y=30,vspace=20,hspace=10, font_scale=1,background_RGB=(228,20,222),text_RGB=(255,255,255))
        text  =  f"Brightness: {self.brightness_value_now}"
        img = ps.putBText(img,text,text_offset_x=80,text_offset_y=425,vspace=20,hspace=10, font_scale=1,background_RGB=(20,210,4),text_RGB=(255,255,255))
        text  =  f'Blur: {self.blur_value_now}: '
        img = ps.putBText(img,text,text_offset_x=self.image.shape[1]-200,text_offset_y=425,vspace=20,hspace=10, font_scale=1,background_RGB=(210,20,4),text_RGB=(255,255,255))


        UI_Function.setPhoto(self,img)

    def notification(self, event = None):
        """
        This function will generate the Dialog to inform user to complete the process before running.
        """
        msg = QMessageBox()
        msg.setWindowTitle("Mode Activate?!")
        msg.setText("Please choose activated mode before loading the object!")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        button = msg.exec_()
        if button == QMessageBox.Ok:
            self.mode = 'cam'
            self.ui.CameraMode.nextCheckState()
            self.ui.modeStatus.setText('Video Activated')
        else:
            return


