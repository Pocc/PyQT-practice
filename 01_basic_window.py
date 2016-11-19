import sys
from PyQt5 import QtWidgets

def window():
    # Set app to an instance of a QT application with the current file (01_basic_window.py) with full file path
    app = QtWidgets.QApplication(sys.argv)

    # Create a variable 'w' to hold a QtWidget
    w = QtWidgets.QWidget()

    # Set the window title
    w.setWindowTitle('PYQt5 lesson 1')

    # Show the window
    w.show()

    # Exit the application
    sys.exit(app.exec_())

window()

