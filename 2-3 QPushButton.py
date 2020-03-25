from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "PyQt5 Push Button"
        left = 500
        top = 200
        width = 300
        height = 250
        # iconName = "home.png" # Don't have icon

        self.setWindowTitle(title)
        # self.setWindowIcon(QtGui.QtGui.QIcon(iconName)
        self.setGeometry(left, top, width, height)
        self.UiComponents()

        self.show()

    def UiComponents(self):
        button = QPushButton("Click Me", self)
        button.setGeometry(QRect(100, 100, 111, 50))
        button.setIcon(QtGui.QIcon("images/icon.jpg"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setToolTip("<h2>This is click me button<h2>") # We can use HTML tags.


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
