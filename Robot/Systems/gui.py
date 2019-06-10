#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
from ser import *

from Vision.ImagePreProcess import *
from Vision.Image import *
from Vision.Undistort import *
from Vision.camDisplay import *
from Vision.LiveMeasure import *
from Vision import geo

import keyboard
import os
import sys
import numpy as np
import cv2

from PyQt4 import QtGui
from PyQt4.QtCore import (QEvent, QThread, Qt, pyqtSignal, pyqtSlot, QUrl)
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
    changedist = pyqtSignal(str)
    changePixmap = pyqtSignal(QImage)
    changePixmap3 = pyqtSignal(QImage)
    changePixmap2 = pyqtSignal(QImage)
    changen = pyqtSignal(str)
    changet = pyqtSignal(str)
    changesq = pyqtSignal(str)
    changel = pyqtSignal(str)
    changec = pyqtSignal(str)
    def __init__(self, parent=None, mode=0):
        QThread.__init__(self, parent=parent)
        self._isRunning = True
        self.mode = mode
    def run(self):
        self.op = None
        self.op2 = None
        self.op3 = None
        if self._isRunning:
            print("heeeeere")
            #os.system("fuser -k /dev/video0")
            self.op = Operation(0)

            self.op2 = None
            if self.mode == 1:
                self.op2 = Display(1)
            elif self.mode == 0:
                print("here!!!")
                self.op2 = Operation(1)
            else:
                self.op2 = LiveMeasure()
            self.op3 = Operation(2)
        while self._isRunning:
           ret, img = self.op.get()
           if self.mode == 1:
               n,t,sq,l,c,img_2 = self.op2.get()
           elif self.mode == 0:
               ret, img_2 = self.op2.get()
           elif self.mode == 2:
               text, img_2 = self.op2.get()
           ret, img_3 = self.op3.get()
           convertToQtFormat = QImage(img.data, img.shape[1],img.shape[0],QImage.Format_RGB888).rgbSwapped()
           if img_2 is not None: 
               convertToQtFormat_2 = QImage(img_2.data, img_2.shape[1],img_2.shape[0],QImage.Format_RGB888).rgbSwapped()
               p_2 = convertToQtFormat_2.scaled(960,540,Qt.KeepAspectRatio)
               self.changePixmap2.emit(p_2)
           convertToQtFormat_2 = QImage(img_2.data, img_2.shape[1],img_2.shape[0],QImage.Format_RGB888).rgbSwapped()
           convertToQtFormat_3 = QImage(img_3.data, img_3.shape[1],img_3.shape[0],QImage.Format_RGB888).rgbSwapped()
           p = convertToQtFormat.scaled(960,540,Qt.KeepAspectRatio)
           p_3 = convertToQtFormat_3.scaled(960,540,Qt.KeepAspectRatio)
           self.changePixmap.emit(p)
           
           self.changePixmap3.emit(p_3)
           if self.mode == 2:
               self.changedist.emit(text)            
           if self.mode == 1:
               self.changen.emit(n)
               self.changet.emit(t)
               self.changesq.emit(sq)
               self.changel.emit(l)
               self.changec.emit(c)
        if not self._isRunning:
            self.op.close()
            self.op2.close()
            self.op3.close()
            # del self.op
            # del self.op2
            # del self.op3
        print("Deleted operations")
    def close(self):
        self._isRunning = False
        # self.op.close()
        # self.op2.close()
        # self.op3.close()


class App(QWidget):
    keyPressed = pyqtSignal(int)
    def __init__(self):
        super(App, self).__init__()
        self.title = "45C Robotics 2019"
        self.initUI()
        self.setStyleSheet(open('/home/robotics45c/Desktop/rov2019/Robot/Systems/style.css').read())
        self.keyPressed.connect(self.on_key)
    def keyReleaseEvent(self, event):
        super(App, self).keyReleaseEvent(event)
        if (event.isAutoRepeat()):
            print('autorepeat')
            return
        else:
            self.keyPressed.emit(event.key())
        event.accept()

    @pyqtSlot(str)
    def setDist(self, text):
        self.dist_label.setText(text)
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
        self.keyPressed.connect(self.on_key)

        self.setWindowTitle(self.title)
        self.resize(1920,1080)
        # Number of shapes
        self.n_label = QLabel(self) 
        self.n_label.setText('--- Number of shapes ---')
        self.n_label.setAlignment(Qt.AlignRight)
        self.n_label.adjustSize()          
        self.n_label.move(1600,525)     
        # Distance
        self.dist_label = QLabel(self) 
        #self.n_label.setText('--- Distance---')
        self.dist_label.setAlignment(Qt.AlignRight)
        self.dist_label.adjustSize()          
        self.dist_label.move(1600,525)     

        # T Species
        self.t_label = QLabel(self)
        self.t_label.setText('--- # of Triangles ---')
        self.t_label.setAlignment(Qt.AlignRight)
        self.t_label.adjustSize()          
        self.t_label.move(1705,555)
        # Sq Species
        self.sq_label = QLabel(self)
        self.sq_label.setText('--- # of Squares ---')
        self.sq_label.setAlignment(Qt.AlignRight)
        self.sq_label.adjustSize()          
        self.sq_label.move(1705,585)
        # Lines Species
        self.l_label = QLabel(self)
        self.l_label.setText('--- # of Lines ---')
        self.l_label.setAlignment(Qt.AlignRight)
        self.l_label.adjustSize() 
        self.l_label.move(1705,615)
        # Circles Species
        self.c_label = QLabel(self)
        self.c_label.setText('--- # of Circles ---')
        self.c_label.setAlignment(Qt.AlignRight)
        self.c_label.adjustSize()    
        self.c_label.move(1705,645)
      
        # Title label
        self.title_label = QLabel(self)
        self.title_label.setText('--- Operator Data ---')
        self.title_label.setAlignment(Qt.AlignRight)
        self.title_label.move(40,495)
        self.title_label.adjustSize()         
        # Temperature Inside Housing
        self.t_housing_in_label = QLabel(self)
        self.t_housing_in_label.setText('Temperature inside housing:')
        self.t_housing_in_label.setAlignment(Qt.AlignRight)
        self.t_housing_in_label.move(40,525)
        self.t_housing_in_label.adjustSize() 
        # Temperature Outside Housing
        self.t_housing_o_label = QLabel(self)
        self.t_housing_o_label.setText('Temperature outside housing:')
        self.t_housing_o_label.setAlignment(Qt.AlignRight)
        self.t_housing_o_label.move(40,555)
        self.t_housing_o_label.adjustSize() 
        # Humidity inside housing
        self.h_housing_in_label = QLabel(self)
        self.h_housing_in_label.setText('Humidity inside housing:')
        self.h_housing_in_label.setAlignment(Qt.AlignRight)
        self.h_housing_in_label.move(40,585)
        self.h_housing_in_label.adjustSize() 
        # Leak Sensor
        self.leak_sensor_label = QLabel(self)
        self.leak_sensor_label.setText('Leak sensor:')
        self.leak_sensor_label.setAlignment(Qt.AlignRight)
        self.leak_sensor_label.move(40,615)
        self.leak_sensor_label.adjustSize() 
        # x
        self.x_label = QLabel(self)
        self.x_label.setText('X:')
        self.x_label.setAlignment(Qt.AlignRight)
        self.x_label.move(40,645)
        self.x_label.adjustSize() 
        # y
        self.y_label = QLabel(self)
        self.y_label.setText('Y:')
        self.y_label.setAlignment(Qt.AlignRight)
        self.y_label.move(40,675)
        self.y_label.adjustSize() 
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
        self.th = VideoThread(self,1)
        s_th = TThread(self) #serial
        self.th.changedist.connect(self.setDist)
        self.th.changePixmap.connect(self.setImage)
        self.th.changePixmap2.connect(self.setImage2)
        self.th.changePixmap3.connect(self.setImage3)
        self.th.changen.connect(self.setNumShapes)
        self.th.changet.connect(self.setNumTriangles)
        self.th.changesq.connect(self.setNumSquares)
        self.th.changel.connect(self.setNumLines)
        self.th.changec.connect(self.setNumCircles)
        s_th.changeText1.connect(self.setText1) 
        s_th.changeText1.connect(self.setText1) 
        s_th.changeText2.connect(self.setText2) 
        s_th.changeText3.connect(self.setText3) 
        s_th.changeText4.connect(self.setText4) 
        s_th.changeText5.connect(self.setText5) 
        s_th.changeText6.connect(self.setText6) 
        self.th.start()
        s_th.start()
        self.history = []
        self.status = 0
        self.mode_status = True # for keeping track of mode
    def on_key(self, event):
        if event == Qt.Key_Return:
            print("Pressed")
            self.status += 1
            if self.status % 2 == 0:
                self.th.close()
                print("Number: {}".format(self.status))
                if self.mode_status:
                    self.th = VideoThread(self, 2)
                    self.mode_status = False
                else:
                    self.th = VideoThread(self,1)
                    self.mode_status = True
                print("Mode 2: {}".format(self.mode_status))
                #self.th.quit()
                #self.th.wait()
                #print('Deleted VideoThread')
                self.th.changedist.connect(self.setDist)
                self.th.changePixmap.connect(self.setImage)
                self.th.changePixmap2.connect(self.setImage2)
                self.th.changePixmap3.connect(self.setImage3)
                self.th.changen.connect(self.setNumShapes)
                self.th.changet.connect(self.setNumTriangles)
                self.th.changesq.connect(self.setNumSquares)
                self.th.changel.connect(self.setNumLines)
                self.th.changec.connect(self.setNumCircles)
                self.th.start()
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
