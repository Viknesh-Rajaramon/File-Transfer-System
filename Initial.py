# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Initial.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from sender import Ui_SenderWindow
from receiver import Ui_RecvWindow
import sys 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 711, 131))
        font = QtGui.QFont()
        font.setFamily("Noto Serif CJK SC")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 491, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Serif CJK SC")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 220, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 220, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.send_pop)
        self.pushButton_2.clicked.connect(self.clickRecv)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Computer Networks Project"))
        self.label_2.setText(_translate("MainWindow", "File Transfer Application"))
        self.pushButton.setText(_translate("MainWindow", "Sender"))
        self.pushButton_2.setText(_translate("MainWindow", "Receiver"))
        
    def clickRecv(self):
        msg = QMessageBox.question(None, "File Transfer", "Are you sure you want to receive a file?", QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:
            self.RecvWindow = QtWidgets.QMainWindow()
            self.ui = Ui_RecvWindow()
            self.ui.setupUi(self.RecvWindow)
            self.RecvWindow.show()
            print("Receiver open")

    def send_pop(self):
        msg = QMessageBox.question(None, "File Transfer", "Are you sure you want to send a file?", QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:
            self.SenderWindow = QtWidgets.QMainWindow()
            self.ui = Ui_SenderWindow()
            self.ui.setupUi(self.SenderWindow)
            self.SenderWindow.show()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())