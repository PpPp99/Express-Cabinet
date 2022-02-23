# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_win1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_send_Firstwin(object):
    def setupUi(self, send_Firstwin):
        send_Firstwin.setObjectName("send_Firstwin")
        send_Firstwin.resize(1200, 800)
        send_Firstwin.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(send_Firstwin)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 100, 361, 71))
        self.label_3.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 450, 731, 51))
        self.label_4.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 600, 320, 70))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 250, 205);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 600, 320, 70))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 196, 197);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 600, 320, 70))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.send_passage_le = QtWidgets.QLineEdit(self.centralwidget)
        self.send_passage_le.setGeometry(QtCore.QRect(530, 320, 381, 51))
        self.send_passage_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.send_passage_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.send_passage_le.setObjectName("send_passage_le")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 330, 201, 31))
        self.label_2.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_2.setObjectName("label_2")
        self.User_name_le = QtWidgets.QLineEdit(self.centralwidget)
        self.User_name_le.setGeometry(QtCore.QRect(530, 220, 381, 51))
        self.User_name_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.User_name_le.setObjectName("User_name_le")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 220, 211, 41))
        self.label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        send_Firstwin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(send_Firstwin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        send_Firstwin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(send_Firstwin)
        self.statusbar.setObjectName("statusbar")
        send_Firstwin.setStatusBar(self.statusbar)

        self.retranslateUi(send_Firstwin)
        self.pushButton.clicked.connect(send_Firstwin.Turn_send2)
        self.pushButton_2.clicked.connect(send_Firstwin.Retur_main)
        self.pushButton_3.clicked.connect(send_Firstwin.turn_registered)
        QtCore.QMetaObject.connectSlotsByName(send_Firstwin)

    def retranslateUi(self, send_Firstwin):
        _translate = QtCore.QCoreApplication.translate
        send_Firstwin.setWindowTitle(_translate("send_Firstwin", "MainWindow"))
        self.label_3.setText(_translate("send_Firstwin", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">User landing：</span></p></body></html>"))
        self.label_4.setText(_translate("send_Firstwin", "If not registered，Click the register button"))
        self.pushButton_3.setText(_translate("send_Firstwin", "register"))
        self.pushButton_2.setText(_translate("send_Firstwin", "cancel"))
        self.pushButton.setText(_translate("send_Firstwin", "login"))
        self.label_2.setText(_translate("send_Firstwin", "Password  ："))
        self.label.setText(_translate("send_Firstwin", "Telephone："))
import images_rc
