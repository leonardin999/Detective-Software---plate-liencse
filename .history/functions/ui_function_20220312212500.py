
from PySide6.QtWidgets import QFileDialog
from gui import *
import os

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
            self.ui.btn_start.setText('Start')
        else:
            self.started=True
            self.ui.btn_start.setText('Stop')


        if self.mode=='cam':
            vid = cv2.VideoCapture(0)
        else:
            if ext in video_file_ext:
                vid = cv2.VideoCapture(self.ui.filename)


        cnt=0
        frames_to_count=20
        st = 0
        fps=0
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
                self.update()
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
        text  =  self.color_selected_text
        rgb=self.lipstick_RGB
        image = ps.putBText(image,text,text_offset_x=10,text_offset_y=10,font_scale=0.5,background_RGB=rgb,text_RGB=(255,255,255))

        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def brightness_value(self,value):
        """ This function will take value from the slider
            for the brightness from 0 to 99
        """
        try:
            self.brightness_value_now = value
            self.update()
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