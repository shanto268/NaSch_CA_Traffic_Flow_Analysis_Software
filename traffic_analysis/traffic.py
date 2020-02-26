# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class Traffic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Traffic Analysis Software"
        self.top = 200
        self.left = 500
        self.width = 600
        self.height = 400
        self.UIComponents()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def UIComponents(self):
        button = QPushButton("Submit", self)
        button.setGeometry(QRect(100, 100, 100, 50))
        button.setIcon(QtGui.QIcon("home.png"))
        button.setToolTip("Click Me")
        button.clicked.connect(self.ClickMe)

    def ClickMe(Self):
        print("Hello World")


if __name__ == "__main__":
    app = QApplication([])
    window = Traffic()
    window.show()
    sys.exit(app.exec_())
