import sys
import numpy as np
import cv2
import speedowidget
from Vision.ImagePreProcess import ImagePreProcess
from Vision.Image import Operation
from PyQt4 import QtGui
from PyQt4.QtCore import (QThread, Qt, pyqtSignal, pyqtSlot, QUrl)
from PyQt4.QtGui import (QPixmap, QImage, QApplication, QWidget, QLabel)
class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    changePixmap2 = pyqtSignal(QImage)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
    def run(self):
        cap = cv2.VideoCapture(0)
        cap2 = cv2.VideoCapture(1)
        while cap.isOpened() and cap2.isOpened():
            ret, frame = cap.read()
            ret2, frame2 = cap2.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1],rgbImage.shape[0],QImage.Format_RGB888)
                p = convertToQtFormat.scaled(960,540,Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
            if ret2:
                rgbImage2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                convertToQtFormat2 = QImage(rgbImage2.data, rgbImage2.shape[1],rgbImage2.shape[0],QImage.Format_RGB888)
                p2 = convertToQtFormat2.scaled(960,540,Qt.KeepAspectRatio)
                self.changePixmap2.emit(p2)
        #cap.release()
        #cap2.release()
class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.title = "45C Robotics 2019"
        self.initUI()
        self.setStyleSheet(open('materialize.min.css').read())
        self.setStyleSheet(open('style.css').read())
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.videoCom.setPixmap(QPixmap.fromImage(image))
    @pyqtSlot(QImage)
    def setImage2(self, image):
        self.videoCom2.setPixmap(QPixmap.fromImage(image))
    def initUI(self):
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
        th.changePixmap2.connect(self.setImage2)
        th.start()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = App()
    #widget = speedowidget.speedowidget()
    #widget.show()
    #widget.resize(200,200)
    run.show()
    sys.exit(app.exec_())
