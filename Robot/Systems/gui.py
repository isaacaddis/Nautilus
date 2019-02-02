#!/usr/bin/env python
#from Vision.Image import Operation
import sys
sys.path.insert(0,'/home/robotics45c/Desktop/rov2019/Robot/Systems/Vision/')
from Image import Operation
from ImagePreProcess import (ImagePreProcess, WhatsCrackin)
import numpy as np
import cv2
import keyboard
import speedowidget
from PyQt4 import QtGui
from PyQt4.QtCore import (QThread, Qt, pyqtSignal, pyqtSlot, QUrl)
from PyQt4.QtGui import (QPixmap, QImage, QApplication, QWidget, QLabel)
class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    changePixmap2 = pyqtSignal(QImage)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
    def run(self):
        # ONE USB PORT SETUP
        op = Operation()
        proc = ImagePreProcess()
        #assert op.status()
        while True:
            img = op.retrieval()
            rgbImage = img.copy()
            convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1],rgbImage.shape[0],QImage.Format_RGB888)
            #LOAD IMAGE PIPELINE HERE
            p = convertToQtFormat.scaled(960,540,Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.title = "45C Robotics 2019"
        self.initUI()
        self.setStyleSheet(open('style.css').read())
        #self.setWindowFlags(Qt.FramelessWindowHint)
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.videoCom.setPixmap(QPixmap.fromImage(image))
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
        self.videoCom.move(120,240)
        self.videoCom.resize(960,540)
        # Video component 2
        self.videoCom2 = QLabel(self)
        self.videoCom2.move(1080,240)
        self.videoCom2.resize(1080,540)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
    def abort(self):
        self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = App()
    run.show()
    if keyboard.is_pressed('space'):
        sys.exit(app.exec_())
    sys.exit(app.exec_())
