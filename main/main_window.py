# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1200, 800)
        Main.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setGeometry(QtCore.QRect(240, 520, 720, 160))
        self.pushButton_send.setStyleSheet("QPushButton{\n"
"   border-radius: 50px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 30pt \"Algerian\";\n"
"}\n"
"")
        self.pushButton_send.setCheckable(False)
        self.pushButton_send.setAutoRepeatInterval(100)
        self.pushButton_send.setObjectName("pushButton_send")
        self.pushButton_receive = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_receive.setGeometry(QtCore.QRect(240, 300, 720, 160))
        self.pushButton_receive.setStyleSheet("QPushButton{\n"
"   border-radius: 50px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 30pt \"Algerian\";\n"
"}\n"
"")
        self.pushButton_receive.setCheckable(False)
        self.pushButton_receive.setObjectName("pushButton_receive")
        self.pushButton_courier = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_courier.setEnabled(True)
        self.pushButton_courier.setGeometry(QtCore.QRect(240, 90, 720, 160))
        self.pushButton_courier.setStyleSheet("QPushButton{\n"
"   border-radius: 50px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 30pt \"Algerian\";\n"
"}\n"
"")
        self.pushButton_courier.setCheckable(False)
        self.pushButton_courier.setObjectName("pushButton_courier")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        self.pushButton_receive.clicked.connect(Main.turn_win)
        self.pushButton_send.clicked.connect(Main.turn_send_win)
        self.pushButton_courier.clicked.connect(Main.turn_courier_win)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.pushButton_send.setText(_translate("Main", "client send express"))
        self.pushButton_receive.setText(_translate("Main", "client receive express"))
        self.pushButton_courier.setText(_translate("Main", "courier"))
import images_rc
