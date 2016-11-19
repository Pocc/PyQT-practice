import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton('Push Me')
    l = QtWidgets.QLabel('Look at Me')

    # Push box automatically formats widgets that you add to it so you don't have to use move(x,y)
    h_box = QtWidgets.QHBoxLayout()  # HBox makes it so that line always stays in the middle vertically
    h_box.addStretch()  # Will fill up as much space horizontally (to the left) as it can
    h_box.addWidget(l)
    h_box.addStretch()  # Will fill up as much space vertically (to the right) as it can

    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)  # VBox extends button to both sides of window
    v_box.addLayout(h_box)  # button b is above the HBox from previous paragraph

    w.setLayout(v_box)  # Call the push box layout for w

    w.setWindowTitle('PYQt5 lesson 4')
    w.show()
    sys.exit(app.exec_())

window()

