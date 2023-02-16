import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class DrawingWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setGeometry(0, 0, 500, 100)

        self.drawing = False
        self.brushSize = 12
        self.previousPoint = QPoint()
        self.drawingWindow = QWidget()

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        