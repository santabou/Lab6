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
        
    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.drawing = True
            self.previousPoint = event.pos()

    def mouseMoveEvent(self, e):
        if (e.buttons() and Qt.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.black, self.brushSize))

            painter.drawLine(self.previousPoint, e.pos())

            self.previousPoint = e.pos()
            self.update()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False
    
    def clear(self):
       self.image.fill(Qt.white)
       self.update()

class SimplePaintProgram(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Paint Program")
        self.setGeometry(0,0,500,300)

        layout = QVBoxLayout()
        self.drawingWindow = DrawingWindow()

        self.label = QLabel()
        self.label.setText("Drag the mouse to draw")
        self.label.setAlignment(Qt.AlignCenter)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.drawingWindow.clear)
        self.clear_button.setGeometry(10, 130, 340, 40)

        layout.addWidget(self.drawingWindow)
        layout.addWidget(self.label)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

        self.show()


def main():
    app = QApplication(sys.argv)
    
    w = SimplePaintProgram()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())