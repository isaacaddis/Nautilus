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
    changePixmap3 = pyqtSignal(QImage)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
    def run(self):
        op = cv2.VideoCapture(0)
        op2 = cv2.VideoCapture(1)
        op3 = cv2.VideoCapture(2)
        while True:
            ret, img = op.read()
            ret, img_2 = op2.read()
            ret, img_3 = op2.read()
            rgbImage = img.copy()
            rgbImage_2 = img_2.copy()
            rgbImage_3 = img_3.copy()
            convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1],rgbImage.shape[0],QImage.Format_RGB888).rgbSwapped()
            convertToQtFormat_2 = QImage(rgbImage_2.data, rgbImage_2.shape[1],rgbImage_2.shape[0],QImage.Format_RGB888).rgbSwapped()
            convertToQtFormat_3 = QImage(rgbImage_3.data, rgbImage_3.shape[1],rgbImage_3.shape[0],QImage.Format_RGB888).rgbSwapped()
            p = convertToQtFormat.scaled(960,540,Qt.KeepAspectRatio)
            p_2 = convertToQtFormat_2.scaled(960,540,Qt.KeepAspectRatio)
            p_3 = convertToQtFormat_3.scaled(960,540,Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
            self.changePixmap2.emit(p_2)
            self.changePixmap3.emit(p_3)
class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.title = "45C Robotics 2019"
        self.initUI()
        self.setStyleSheet(open('style.css').read())
        self.setWindowFlags(Qt.FramelessWindowHint)
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.videoCom.setPixmap(QPixmap.fromImage(image))
    @pyqtSlot(QImage)
    def setImage2(self, image):
        self.videoCom2.setPixmap(QPixmap.fromImage(image))
    @pyqtSlot(QImage)
    def setImage3(self, image):
        self.videoCom3.setPixmap(QPixmap.fromImage(image))
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
        self.videoCom.move(80,0)
        self.videoCom.resize(1200,540)
        # Video component 2
        self.videoCom2 = QLabel(self)
        self.videoCom2.move(1100,0)
        self.videoCom2.resize(1200,540)
        # Video component 3
        self.videoCom3 = QLabel(self)
        self.videoCom3.move(540,540)
        self.videoCom3.resize(1920,540)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.changePixmap2.connect(self.setImage2)
        th.changePixmap3.connect(self.setImage3)
        th.start()
    def abort(self):
        self.close()
if __name__ == "__main__":
    os.system("fuser -k /dev/video0")
    os.system("fuser -k /dev/video1")
    os.system("fuser -k /dev/video3")
    app = QApplication(sys.argv)
    run = App()
    run.show()
    sys.exit(app.exec_())
