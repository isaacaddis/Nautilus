#!/usr/bin/env python
#from Vision.Image import Operation
import sys
sys.path.insert(0,'/home/robotics45c/Desktop/rov2019/Robot/Systems/Vision/')
from Image import Operation
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
        '''
            4 usb port setup
        '''
        op = Operation()
        op2 = Operation()
        op3 = Operation()
        op4 = Operation()
        op_list = [op,op2,op3,op4]
        n = 0
        for i in op_list:
            i.setPort(n)
            n+=1
        img = op.retrieval()
        img_2 = op2.retrieval()
        img_3 = op3.retrieval()
        img_4 = op4.retrieval()
        img_list = [img,img_2,img_3,img_4]
        if op.status() and op2.status() and op3.status() and op4.status():
            while True:
                for rgbImage in img_list:
                    convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1],rgbImage.shape[0],QImage.Format_RGB888)
                    p = convertToQtFormat.scaled(960,540,Qt.KeepAspectRatio)
                    self.changePixmap.emit(p)
        else:
            print("One or more of your cameras is not working as intended. Please re-evaluate your setup and re-run the script.")
class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.title = "45C Robotics 2019"
        self.initUI()
        self.setStyleSheet(open('style.css').read())
        '''
            Utilities
        '''
        self.setWindowFlags(Qt.FramelessWindowHint)
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.videoCom.setPixmap(QPixmap.fromImage(image))
    @pyqtSlot(QImage)
    def setImage2(self, image):
        self.videoCom2.setPixmap(QPixmap.fromImage(image))
    @classmethod
    def setText(self, text):
        self.temp_label.setText(text)
    def initUI(self):
        self.temp_label = QLabel()
        #self.temp_label.setReadOnly(True)
        self.temp_label.setAlignment(Qt.AlignRight)
        self.temp_label.setText('text')
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
        #th = Thread(self)
        #th_2 = Thread(self)
        #th.changePixmap.connect(self.setImage)
        #th.changePixmap2.connect(self.setImage2)
        #th.start()
    def abort(self):
        self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = App()
    run.show()
    if keyboard.is_pressed('space'):
        sys.exit(app.exec_())
    sys.exit(app.exec_())
