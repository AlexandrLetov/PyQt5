from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Signal_and_slots"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        # self.setWinowIcon(QtGui.QIcon("home.png")) # I just don't have any icon now
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.UiComponents()

        self.show()

    def UiComponents(self):
        button = QPushButton("Click Me", self)
        button.setGeometry(QRect(100, 100, 111, 50))
        button.setIcon(QtGui.QIcon("images/icon.jpg"))
        button.clicked.connect(self.Click_Me)


    def Click_Me(self):
        sys.exit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())