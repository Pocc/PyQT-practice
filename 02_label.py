import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)  # Create a label for window w
    l2 = QtWidgets.QLabel(w)
    l1.setText("Hello World")  # Set the text for window w
    l2.setPixmap(QtGui.QPixmap('rsc/globe.png'))  # Set the pixmap to globe.png using QtGui
    w.setWindowTitle('PYQt5 lesson 2')
    w.setGeometry(200, 100, 300, 400)  # Window geometry (startX, startY, widthX, widthY)
    l1.move(120, 40)  # move label over 130px and 20px down
    l2.move(20, 100)  # move the globe image down to the center of the screen
    w.show()
    sys.exit(app.exec_())

window()