#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
from ser import *

from Vision.ImagePreProcess import *
from Vision.Image import *
from Vision.Undistort import *
from Vision.camDisplay import *
from Vision import geo

import keyboard
import os
import sys
import numpy as np
import cv2

from PyQt4 import QtGui
from PyQt4.QtCore import (QThread, Qt, pyqtSignal, pyqtSlot, QUrl)
from PyQt4.QtGui import (QPixmap, QImage, QApplication, QWidget, QLabel)

class TThread(QThread):
    changeText1 = pyqtSignal(str)
    changeText2 = pyqtSignal(str)
    changeText3 = pyqtSignal(str)
    changeText4 = pyqtSignal(str)
    changeText5 = pyqtSignal(str)
    changeText6 = pyqtSignal(str)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        wait_for_input = pyqtSignal(int)
    def run(self):
        s = SerialUtil()
        while True:
            msg = s.get()
            if msg is not None:        
                t_housing_in,t_housing_out,h_housing_in,leak_sensor,x,y = msg
                self.changeText1.emit('T_in housing: '+str(t_housing_in))
                self.changeText2.emit('T_out housing: '+str(t_housing_out))
                self.changeText3.emit('H_in housing: '+str(h_housing_in))
                self.changeText4.emit('Leak sensor: '+str(leak_sensor))
                self.changeText5.emit('X pos: '+str(x))
                self.changeText6.emit('Y pos: '+str(y))
class VideoThread(QThread):
    changePixmap = pyqtSignal(QImage)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
    def run(self):
        op = Operation(0)
        while True:
           ret, img = op.get()
           convertToQtFormat = QImage(img.data, img.shape[1],img.shape[0],QImage.Format_RGB888).rgbSwapped()
           p = convertToQtFormat.scaled(960,540,Qt.KeepAspectRatio)
           self.changePixmap.emit(p)
class VideoThread2(QThread):
    changePixmap2 = pyqtSignal(QImage)
    changen = pyqtSignal(str)
    changet = pyqtSignal(str)
    changesq = pyqtSignal(str)
    changel = pyqtSignal(str)
    changec = pyqtSignal(str)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
    def run(self):
        op2 = Display(1)
        while True:
            n,t,sq,l,c,img_2 = op2.get(1)
            convertToQtFormat_2 = QImage(img_2.data, img_2.shape[1],img_2.shape[0],QImage.Format_RGB888).rgbSwapped()
            p_2 = convertToQtFormat_2.scaled(960,540,Qt.KeepAspectRatio)
            self.changen.emit(n)
            self.changet.emit(t)
            self.changesq.emit(sq)
            self.changel.emit(l)
            self.changec.emit(c)
            self.changePixmap2.emit(p_2)
class VideoThread3(QThread):
    changePixmap3 = pyqtSignal(QImage)
    def run(self):
        wc = WhatsCrackin()
        op3 = Operation(2)
        while True:
            ret, img_3 = op3.get()
            convertToQtFormat_3 = QImage(img_3.data, img_3.shape[1],img_3.shape[0],QImage.Format_RGB888).rgbSwapped()
            p_3 = convertToQtFormat_3.scaled(960,540,Qt.KeepAspectRatio)
            self.changePixmap3.emit(p_3)
class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.title = "45C Robotics 2019"
        self.initUI()
        self.setStyleSheet(open('/home/robotics45c/Desktop/rov2019/Robot/Systems/style.css').read())
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.videoCom.setPixmap(QPixmap.fromImage(image))
    @pyqtSlot(QImage)
    def setImage2(self, image):
        self.videoCom2.setPixmap(QPixmap.fromImage(image))
    @pyqtSlot(QImage)
    def setImage3(self, image):
        self.videoCom3.setPixmap(QPixmap.fromImage(image))   
    @pyqtSlot(str)
    def setText1(self, text):
        self.t_housing_in_label.setText(text)     
    @pyqtSlot(str)
    def setText2(self, text):
        self.t_housing_o_label.setText(text)     
    @pyqtSlot(str)
    def setText3(self, text):
        self.h_housing_in_label.setText(text)     
    @pyqtSlot(str)
    def setText4(self, text):
        self.leak_sensor_label.setText(text)     
    @pyqtSlot(str)
    def setText5(self, text):
        self.x_label.setText(text)     
    @pyqtSlot(str)
    def setText6(self, text):
        self.y_label.setText(text) 
    @pyqtSlot(str)
    def setNumShapes(self, text):
        self.n_label.setText(text)         
    @pyqtSlot(str)
    def setNumTriangles(self, text):
        self.t_label.setText(text)         
    @pyqtSlot(str)
    def setNumSquares(self, text):
        self.sq_label.setText(text)         
    @pyqtSlot(str)
    def setNumLines(self, text):
        self.l_label.setText(text)         
    @pyqtSlot(str)
    def setNumCircles(self, text):
        self.c_label.setText(text) 
    
    def initUI(self):
        print("Initialized serial comms")

        self.setWindowTitle(self.title)
        self.resize(1920,1080)
        # Number of shapes
        self.n_label = QLabel(self) 
        self.n_label.setText('--- Number of shapes ---')
        self.n_label.setAlignment(Qt.AlignRight)
        self.n_label.move(1710,525)         
        # T Species
        self.t_label = QLabel(self)
        self.t_label.setText('--- # of Triangles ---')
        self.t_label.setAlignment(Qt.AlignRight)
        self.t_label.move(1710,555)         
        # Sq Species
        self.sq_label = QLabel(self)
        self.sq_label.setText('--- # of Squares ---')
        self.sq_label.setAlignment(Qt.AlignRight)
        self.sq_label.move(1710,585)         
        # Lines Species
        self.l_label = QLabel(self)
        self.l_label.setText('--- # of Lines ---')
        self.l_label.setAlignment(Qt.AlignRight)
        self.l_label.move(1710,615)         
        # Circles Species
        self.c_label = QLabel(self)
        self.c_label.setText('--- # of Circles ---')
        self.c_label.setAlignment(Qt.AlignRight)
        self.c_label.move(1710,645)         
        # Title label
        self.title_label = QLabel(self)
        self.title_label.setText('--- Operator Data ---')
        self.title_label.setAlignment(Qt.AlignRight)
        self.title_label.move(40,495)        
        # Temperature Inside Housing
        self.t_housing_in_label = QLabel(self)
        self.t_housing_in_label.setText('Temperature inside housing:')
        self.t_housing_in_label.setAlignment(Qt.AlignRight)
        self.t_housing_in_label.move(40,525)
        # Temperature Outside Housing
        self.t_housing_o_label = QLabel(self)
        self.t_housing_o_label.setText('Temperature outside housing:')
        self.t_housing_o_label.setAlignment(Qt.AlignRight)
        self.t_housing_o_label.move(40,555)
        # Humidity inside housing
        self.h_housing_in_label = QLabel(self)
        self.h_housing_in_label.setText('Humidity inside housing:')
        self.h_housing_in_label.setAlignment(Qt.AlignRight)
        self.h_housing_in_label.move(40,585)
        # Leak Sensor
        self.leak_sensor_label = QLabel(self)
        self.leak_sensor_label.setText('Leak sensor:')
        self.leak_sensor_label.setAlignment(Qt.AlignRight)
        self.leak_sensor_label.move(40,615)
        # x
        self.x_label = QLabel(self)
        self.x_label.setText('X:')
        self.x_label.setAlignment(Qt.AlignRight)
        self.x_label.move(40,645)
        # y
        self.y_label = QLabel(self)
        self.y_label.setText('Y:')
        self.y_label.setAlignment(Qt.AlignRight)
        self.y_label.move(40,675)
        # Video component 1
        self.videoCom = QLabel(self)
        self.videoCom.move(150,0)
        self.videoCom.resize(925,500)
        # Video component 2
        self.videoCom2 = QLabel(self)
        self.videoCom2.move(1055,0)
        self.videoCom2.resize(855,500)
        # Video component 3
        self.videoCom3 = QLabel(self)
        self.videoCom3.move(580,540)
        self.videoCom3.resize(1200,540)
        th = VideoThread(self)
        th2 = VideoThread2(self)
        th3 = VideoThread3(self)
        s_th = TThread(self) #serial
        th.changePixmap.connect(self.setImage)
        th2.changePixmap2.connect(self.setImage2)
        th3.changePixmap3.connect(self.setImage3)
        th2.changen.connect(self.setNumShapes)
        th2.changet.connect(self.setNumTriangles)
        th2.changesq.connect(self.setNumSquares)
        th2.changel.connect(self.setNumLines)
        th2.changec.connect(self.setNumCircles)
        s_th.changeText1.connect(self.setText1) 
        s_th.changeText1.connect(self.setText1) 
        s_th.changeText2.connect(self.setText2) 
        s_th.changeText3.connect(self.setText3) 
        s_th.changeText4.connect(self.setText4) 
        s_th.changeText5.connect(self.setText5) 
        s_th.changeText6.connect(self.setText6) 
        th.start()
        th2.start()
        th3.start()
        s_th.start()
    def abort(self):
        self.close()
if __name__ == "__main__":
    os.system("fuser -k /dev/video0")
    os.system("fuser -k /dev/video1")
    os.system("fuser -k /dev/video2")
    app = QApplication(sys.argv)
    run = App()
    run.show()
    sys.exit(app.exec_())
