#!/usr/bin/env python
#from Vision.Image import Operation
import os
import sys
import numpy as np
import cv2
from PyQt4 import QtGui
from PyQt4.QtCore import (QThread, Qt, pyqtSignal, pyqtSlot, QUrl)
from PyQt4.QtGui import (QPixmap, QImage, QApplication, QWidget, QLabel)
class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    changePixmap2 = pyqtSignal(QImage)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
    def run(self):
        op = cv2.VideoCapture(0)
        op2 = cv2.VideoCapture(1)
        while True:
            ret, img = op.read()
            #img = vis.integrate(img)
            ret, img_2 = op2.read()
            #img_2 = vis.integrate(img_2)
            rgbImage = img.copy()
            rgbImage_2 = img_2.copy()
            convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1],rgbImage.shape[0],QImage.Format_RGB888)
            convertToQtFormat_2 = QImage(rgbImage_2.data, rgbImage_2.shape[1],rgbImage.shape[0],QImage.Format_RGB888)
            p = convertToQtFormat.scaled(960,540,Qt.KeepAspectRatio)
            p_2 = convertToQtFormat_2.scaled(960,540,Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
            self.changePixmap2.emit(p_2)
class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.title = "45C Robotics 2019"
        self.initUI()
        #self.setStyleSheet(open('style.css').read())
        #self.setWindowFlags(Qt.FramelessWindowHint)
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.videoCom.setPixmap(QPixmap.fromImage(image))
    @pyqtSlot(QImage)
    def setImage2(self, image):
        self.videoCom2.setPixmap(QPixmap.fromImage(image))
    def initUI(self):
        self.temp_label = QLabel()
        #self.temp_label.setReadOnly(True)
        self.temp_label.setAlignment(Qt.AlignRight)
        self.temp_label.setText('text')
        self.temp_label.setOpenExternalLinks(True)
        self.temp_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setWindowTitle(self.title)
        self.resize(1920,1080)
        # Video component 1
        self.videoCom = QLabel(self)
        self.videoCom.move(240,240)
        self.videoCom.resize(480,270)
        # Video component 2
        self.videoCom2 = QLabel(self)
        self.videoCom2.move(960,240)
        self.videoCom2.resize(480,270)
        # Video component 3
        '''
        self.videoCom3 = QLabel(self)
        self.videoCom3.move(240,520)
        self.videoCom3.resize(480,270)
        # Video component 4
        self.videoCom4 = QLabel(self)
        self.videoCom4.move(960,520)
        self.videoCom4.resize(480,270)
        '''
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.changePixmap2.connect(self.setImage2)
        th.start()
    def abort(self):
        self.close()
if __name__ == "__main__":
    os.system("fuser -k /dev/video0")
    os.system("fuser -k /dev/video1")
    app = QApplication(sys.argv)
    run = App()
    run.show()
    sys.exit(app.exec_())
