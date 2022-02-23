# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_win5.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sendfivewin(object):
    def setupUi(self, sendfivewin):
        sendfivewin.setObjectName("sendfivewin")
        sendfivewin.resize(1200, 800)
        sendfivewin.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(sendfivewin)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 620, 531, 71))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 25pt \"Baskerville Old Face\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 430, 531, 71))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 250, 205);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 25pt \"Baskerville Old Face\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.time_le = QtWidgets.QLabel(self.centralwidget)
        self.time_le.setGeometry(QtCore.QRect(830, 160, 71, 61))
        self.time_le.setStyleSheet("font: 24pt \"Baskerville Old Face\";")
        self.time_le.setObjectName("time_le")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(15, 620, 531, 71))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 196, 197);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 25pt \"Baskerville Old Face\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(215, 138, 911, 221))
        self.label_2.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_2.setObjectName("label_2")
        sendfivewin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sendfivewin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        sendfivewin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sendfivewin)
        self.statusbar.setObjectName("statusbar")
        sendfivewin.setStatusBar(self.statusbar)

        self.retranslateUi(sendfivewin)
        self.pushButton.clicked.connect(sendfivewin.turn_send_win1)
        self.pushButton_3.clicked.connect(sendfivewin.return_mainwindow)
        self.pushButton_2.clicked.connect(sendfivewin.reopen_box)
        QtCore.QMetaObject.connectSlotsByName(sendfivewin)

    def retranslateUi(self, sendfivewin):
        _translate = QtCore.QCoreApplication.translate
        sendfivewin.setWindowTitle(_translate("sendfivewin", "MainWindow"))
        self.pushButton.setText(_translate("sendfivewin", "Continue to send"))
        self.pushButton_2.setText(_translate("sendfivewin", "reopen the box"))
        self.time_le.setText(_translate("sendfivewin", "<html><head/><body><p><span style=\" color:#000000;\">120</span></p></body></html>"))
        self.pushButton_3.setText(_translate("sendfivewin", "renturn the mainwindow"))
        self.label_2.setText(_translate("sendfivewin", "<html><head/><body><p><span style=\" font-size:24pt;\">System will return to main screen after ___s</span></p><p><span style=\" font-size:24pt;\">If you incorrectly close the box without take the express</span></p><p><span style=\" font-size:24pt;\">you can reopen the box in 2 minutes</span></p></body></html>"))
import images_rc
