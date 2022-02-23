# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'courier_win1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_courier_win_one(object):
    def setupUi(self, courier_win_one):
        courier_win_one.setObjectName("courier_win_one")
        courier_win_one.resize(1200, 809)
        courier_win_one.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(courier_win_one)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(484, 110, 421, 71))
        self.label_3.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 600, 320, 80))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 196, 197);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 251, 210, 51))
        self.label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.courier_name_le = QtWidgets.QLineEdit(self.centralwidget)
        self.courier_name_le.setGeometry(QtCore.QRect(510, 260, 391, 51))
        self.courier_name_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.courier_name_le.setObjectName("courier_name_le")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 371, 191, 51))
        self.label_2.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_2.setObjectName("label_2")
        self.courier_passage_le = QtWidgets.QLineEdit(self.centralwidget)
        self.courier_passage_le.setGeometry(QtCore.QRect(509, 370, 391, 51))
        self.courier_passage_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.courier_passage_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.courier_passage_le.setObjectName("courier_passage_le")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 600, 320, 80))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        courier_win_one.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(courier_win_one)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        courier_win_one.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(courier_win_one)
        self.statusbar.setObjectName("statusbar")
        courier_win_one.setStatusBar(self.statusbar)

        self.retranslateUi(courier_win_one)
        self.pushButton.clicked.connect(courier_win_one.turn_courier_win1)
        self.pushButton_2.clicked.connect(courier_win_one.turn_main_win)
        QtCore.QMetaObject.connectSlotsByName(courier_win_one)

    def retranslateUi(self, courier_win_one):
        _translate = QtCore.QCoreApplication.translate
        courier_win_one.setWindowTitle(_translate("courier_win_one", "MainWindow"))
        self.label_3.setText(_translate("courier_win_one", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Courier landing：</span></p></body></html>"))
        self.pushButton_2.setText(_translate("courier_win_one", "cancel"))
        self.label.setText(_translate("courier_win_one", "Telephone:"))
        self.label_2.setText(_translate("courier_win_one", "Password："))
        self.pushButton.setText(_translate("courier_win_one", "login"))
import images_rc
