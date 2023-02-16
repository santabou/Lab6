import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window_3(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple GitHub Drawing")
        self.rabbit= QPixmap("pic3.png")

    def paintEvent(self,e):
        p=QPainter()
        p.begin(self)

        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()
