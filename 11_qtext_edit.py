import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.text2 = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.text2)
        layout.addWidget(self.clr_btn)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 TextEdit')

        self.show()

app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())