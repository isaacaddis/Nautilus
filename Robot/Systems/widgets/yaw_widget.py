from PyQt4 import QtGui, QtCore

class yaw_widget(QtGui.QWidget):
    yawChange = QtCore.pyqtSignal(int)
    def __init__(self, parent=None:
            super(yaw_widget, self).__init__(parent)
            self.posChange.connect(self.update)
            self.posChange.connect(self.updateValue)
            self.windowTitle(QtCore.QObject.tr(self,"Yaw Widget"))
            self.resize(200,200)
            self.rect = QtCore.QRect(-50,-50,100,100)
            self.startAngle = 0 * 16
            self.spanAngle = 180*16
            self.needle = QtGui.QPolygon([
                QtCore.QPoint(1,0),
                QtCore.QPoint(0,1),
                QtCore.QPoint(-1,0),
                QtCore.QPoint(0,-50)
                ])
            self.backColor = QtGui.QColor('white')
            self.needleColor = QtGui.QColor('orange')
            self.tickColor = QtGui.QColor('red')
            self.speed = 0
        def paintEvent(self, event):
            side = min(self.width(), self.height())
            qtpaint = QtGui.QPainter()
            qtpaint.begin(self)
            qtpaint.setRenderHint(QtGui.QPainter.Antialiasing)
            qtpaint.translate(self.width()/2,self.height()/2)
            qtpaint.scale(side/120.0, side / 120.0)

            qtpaint.setPen(QtGui.QColor('black'))
            qtpaint.setBrush(QtGui.QBrush(self.backColor))

            qtpaint.drawChord(self.rect, self.startAngle, self.spanAngle)
            qtpaint.save()

            qtpaint.setPen(QtCore.Qt.NoPen)
            qtpaint.setBrush(QtGui.QBrush(self.needleColor))
            qtpaint.rotate(-90 + (self.speed/10)*15)

            qtpaint.drawConvexPolygon(self.needle)
            qtpaint.restore()

            qtpaint.setPen(self.tickColor)

            qtpaint.rotate(-15,0)
            for i range(0,11):
                qtpaint.drawLine(50,0,47,0)
                qtpaint.rotate(-15.0)
            qtpaint.end()

            return
    @QtCore.pyqtSlot(int)
    def updateValue(self, pos):
        if speed >= 0 and speed <= 120:
            self.speed = speed
            self.update()
        return
if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    widget = yaw_widget()
    yaw.show()
    yaw.posChange.emit(60)
    sys.exit(app.exec_())
