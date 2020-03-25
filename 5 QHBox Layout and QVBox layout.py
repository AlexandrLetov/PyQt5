from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQT5 5 QHBox Layout and QVBox layout"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.iconName = "images/icon.jpg"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_layout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.group_box)
        self.setLayout(vbox) 

        self.show()

    def create_layout(self):
        self.group_box = QGroupBox("What is your favorite sport?")
        hbox_layout = QHBoxLayout()

        button = QPushButton("One", self)
        button.setIcon(QtGui.QIcon("images/icon.jpg"))
        button.setMinimumHeight(40)
        hbox_layout.addWidget(button)

        button1 = QPushButton("Two", self)
        button1.setIcon(QtGui.QIcon("images/icon.jpg"))
        button1.setMinimumHeight(40)
        hbox_layout.addWidget(button1)

        button2 = QPushButton("Three", self)
        button2.setIcon(QtGui.QIcon("images/icon.jpg"))
        button2.setMinimumHeight(40)
        hbox_layout.addWidget(button2)

        self.group_box.setLayout(hbox_layout)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
