# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_traffic.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GUI_traffic(object):
    def setupUi(self, GUI_traffic):
        GUI_traffic.setObjectName("GUI_traffic")
        GUI_traffic.resize(488, 445)
        self.centralwidget = QtWidgets.QWidget(GUI_traffic)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(370, 0, 111, 381))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 90, 91, 21))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 120, 91, 21))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 150, 91, 21))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 180, 91, 21))
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        GUI_traffic.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GUI_traffic)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        GUI_traffic.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(GUI_traffic)
        QtCore.QMetaObject.connectSlotsByName(GUI_traffic)

    def retranslateUi(self, GUI_traffic):
        _translate = QtCore.QCoreApplication.translate
        GUI_traffic.setWindowTitle(_translate("GUI_traffic", "MainWindow"))
        self.groupBox.setTitle(_translate("GUI_traffic", "Inputs"))
        self.menuFile.setTitle(_translate("GUI_traffic", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI_traffic = QtWidgets.QMainWindow()
    ui = Ui_GUI_traffic()
    ui.setupUi(GUI_traffic)
    GUI_traffic.show()
    sys.exit(app.exec_())
