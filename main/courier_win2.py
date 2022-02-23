# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'courier_win2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_courier_win_two(object):
    def setupUi(self, courier_win_two):
        courier_win_two.setObjectName("courier_win_two")
        courier_win_two.resize(1200, 800)
        courier_win_two.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(courier_win_two)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(236, 190, 741, 111))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 50px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Algerian\";\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 380, 741, 111))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"   border-radius: 50px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Algerian\";\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 600, 320, 80))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 196, 197);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        courier_win_two.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(courier_win_two)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        courier_win_two.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(courier_win_two)
        self.statusbar.setObjectName("statusbar")
        courier_win_two.setStatusBar(self.statusbar)

        self.retranslateUi(courier_win_two)
        self.pushButton.clicked.connect(courier_win_two.Put_window)
        self.pushButton_2.clicked.connect(courier_win_two.Collect_window)
        self.pushButton_3.clicked.connect(courier_win_two.courier_window)
        QtCore.QMetaObject.connectSlotsByName(courier_win_two)

    def retranslateUi(self, courier_win_two):
        _translate = QtCore.QCoreApplication.translate
        courier_win_two.setWindowTitle(_translate("courier_win_two", "MainWindow"))
        self.pushButton.setText(_translate("courier_win_two", "Put the client\'s express into the cabinet"))
        self.pushButton_2.setText(_translate("courier_win_two", "Receive pending express from client"))
        self.pushButton_3.setText(_translate("courier_win_two", "cancel"))
import images_rc
