import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from Simple_drawing_window1 import *
from Simple_drawing_window2 import *
from Simple_drawing_window3 import *

def one():
    app = QApplication(sys.argv)
    w = Simple_drawing_window_1()
    w.show
    return app.exec()


def two():
    app= QApplication(sys.argv)
    w = Simple_drawing_window_2()
    w.show
    return app.exec()


def three():
    app = QApplication(sys.argv)
    w = Simple_drawing_window_3()
    w.show
    return app.exec()

def main():
    one()
    two()
    three()
    
if __name__ == '__main__':
    sys.exit(main())