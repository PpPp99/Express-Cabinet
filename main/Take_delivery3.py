# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Take_delivery3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_take_delivery_three(object):
    def setupUi(self, take_delivery_three):
        take_delivery_three.setObjectName("take_delivery_three")
        take_delivery_three.resize(1200, 800)
        take_delivery_three.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(take_delivery_three)
        self.centralwidget.setObjectName("centralwidget")
        self.time_le = QtWidgets.QLabel(self.centralwidget)
        self.time_le.setGeometry(QtCore.QRect(830, 160, 71, 61))
        self.time_le.setStyleSheet("font: 24pt \"Baskerville Old Face\";")
        self.time_le.setObjectName("time_le")
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
        self.label_2.setGeometry(QtCore.QRect(215, 138, 901, 221))
        self.label_2.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_2.setObjectName("label_2")
        take_delivery_three.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(take_delivery_three)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        take_delivery_three.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(take_delivery_three)
        self.statusbar.setObjectName("statusbar")
        take_delivery_three.setStatusBar(self.statusbar)

        self.retranslateUi(take_delivery_three)
        self.pushButton.clicked.connect(take_delivery_three.return_put_win1)
        self.pushButton_2.clicked.connect(take_delivery_three.reopen_box)
        self.pushButton_3.clicked.connect(take_delivery_three.return_mainwindow)
        QtCore.QMetaObject.connectSlotsByName(take_delivery_three)

    def retranslateUi(self, take_delivery_three):
        _translate = QtCore.QCoreApplication.translate
        take_delivery_three.setWindowTitle(_translate("take_delivery_three", "MainWindow"))
        self.time_le.setText(_translate("take_delivery_three", "<html><head/><body><p><span style=\" color:#000000;\">120</span></p></body></html>"))
        self.pushButton.setText(_translate("take_delivery_three", "Continue to Receive"))
        self.pushButton_2.setText(_translate("take_delivery_three", "Reopen the Box"))
        self.pushButton_3.setText(_translate("take_delivery_three", "Renturn the Mainwindow"))
        self.label_2.setText(_translate("take_delivery_three", "<html><head/><body><p><span style=\" font-size:24pt;\">System will return to main screen after ___s</span></p><p><span style=\" font-size:24pt;\">If you incorrectly close the box without take the express</span></p><p><span style=\" font-size:24pt;\">you can reopen the box in 2 minutes</span></p></body></html>"))
import images_rc
