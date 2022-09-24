import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import time
import socket
import tqdm
import os
import argparse
import threading


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024

class File(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Select File'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.fileName = ''
        self.host = []
        self.initUI()
        self.close()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.openFileNameDialog()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            print(self.fileName)


    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    def client(self, filename):
        port=5001

        # creating thread 
        t1 = threading.Thread(target=self.send_file, args=(filename,self.host[0],port)) 
        t2 = threading.Thread(target=self.send_file, args=(filename,self.host[1],port)) 
        t3 = threading.Thread(target=self.send_file, args=(filename,self.host[2],port)) 

        # starting thread 1 
        t1.start() 
        # starting thread 2 
        t2.start() 
        # starting thread 3 
        t3.start() 
    
        # wait until thread 1 is completely executed 
        t1.join() 
        # wait until thread 2 is completely executed 
        t2.join() 
        # wait until thread 2 is completely executed 
        t3.join() 
    
        # both threads completely executed 
        print("Done!") 
   

class Ui_SenderWindow(File):
    def __init__(self):
        super().__init__()
        print("Inside sender window function\n\n\n\n")
        print(self.fileName)

    def send_file(self, filename, host, port):
        value = 0
        filesize = os.path.getsize(filename)
        s = socket.socket()
        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print("[+] Connected.")
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "rb") as f:
            for _ in progress:
                bytes_read = f.read(BUFFER_SIZE)
                value = value + 1024
                self.progressBar.setProperty("value", value/filesize*100)

                
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                progress.update(len(bytes_read))
        s.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 120, 431, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(self.fileName)
        self.fileSelect = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.fileSelect.setGeometry(QtCore.QRect(590, 110, 174, 41))
        self.fileSelect.setObjectName("fileSelect")
        self.fileSelect.clicked.connect(self.fileClick)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 170, 431, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(80, 370, 671, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 611, 91))
        font = QtGui.QFont()
        font.setFamily("Noto Serif CJK SC")
        font.setPointSize(36)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 210, 431, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 250, 431, 23))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 300, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 170, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 210, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 250, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.transferClick)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fileSelect.setText(_translate("MainWindow", "Select File"))
        self.label.setText(_translate("MainWindow", "File Transfer Client"))
        self.pushButton.setText(_translate("MainWindow", "Start Transfer"))
        self.label_2.setText(_translate("MainWindow", "Enter Receiver 1 IP :"))
        self.label_3.setText(_translate("MainWindow", "Enter Receiver 2 IP :"))
        self.label_4.setText(_translate("MainWindow", "Enter Receiver 3 IP :"))

    def fileClick(self):
        self._new_window = File()
    
    def transferClick(self):
        self.host.append(self.lineEdit_2.text())
        self.host.append(self.lineEdit_3.text())
        self.host.append(self.lineEdit_4.text())
        print(self.host)
        super().client(self.fileName)

    def ipClick(self, no):
        print("inside ip host")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_SenderWindow()
    sys.exit(app.exec_())