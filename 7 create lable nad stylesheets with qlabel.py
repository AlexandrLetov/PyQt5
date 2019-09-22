from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Signal_and_slots"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.icon_name = "images/icon.jpg"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        label = QLabel("This is label")
        vbox.addWidget(label)

        label2 = QLabel("Second label")
        label2.setFont(QtGui.QFont("Sanserif ", 20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
