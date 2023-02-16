import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from Simple_drawing_window1 import *
from Simple_drawing_window2 import *
from Simple_drawing_window3 import *

def main():
    app = QApplication(sys.argv)
    w1 = Simple_drawing_window_1()
    w1.show()
    w2 = Simple_drawing_window_2()
    w2.show()
    w3 = Simple_drawing_window_3()
    w3.show()
    return app.exec()
    
if __name__ == '__main__':
    sys.exit(main())