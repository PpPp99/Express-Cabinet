# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_win3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sendthreewin(object):
    def setupUi(self, sendthreewin):
        sendthreewin.setObjectName("sendthreewin")
        sendthreewin.resize(1200, 800)
        sendthreewin.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(sendthreewin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 50, 791, 131))
        self.label.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 600, 320, 80))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 600, 320, 80))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 196, 197);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 210, 351, 51))
        self.label_2.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_2.setObjectName("label_2")
        self.Rec_name_le = QtWidgets.QLineEdit(self.centralwidget)
        self.Rec_name_le.setGeometry(QtCore.QRect(680, 210, 361, 51))
        self.Rec_name_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.Rec_name_le.setObjectName("Rec_name_le")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 320, 431, 51))
        self.label_3.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_3.setObjectName("label_3")
        self.Rec_tele_le = QtWidgets.QLineEdit(self.centralwidget)
        self.Rec_tele_le.setGeometry(QtCore.QRect(680, 320, 361, 51))
        self.Rec_tele_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.Rec_tele_le.setObjectName("Rec_tele_le")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 430, 391, 51))
        self.label_4.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_4.setObjectName("label_4")
        self.Rec_address_le = QtWidgets.QLineEdit(self.centralwidget)
        self.Rec_address_le.setGeometry(QtCore.QRect(680, 430, 361, 51))
        self.Rec_address_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.Rec_address_le.setObjectName("Rec_address_le")
        sendthreewin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sendthreewin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        sendthreewin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sendthreewin)
        self.statusbar.setObjectName("statusbar")
        sendthreewin.setStatusBar(self.statusbar)

        self.retranslateUi(sendthreewin)
        self.pushButton.clicked.connect(sendthreewin.turn_to_win4)
        self.pushButton_2.clicked.connect(sendthreewin.turn_to_win2)
        QtCore.QMetaObject.connectSlotsByName(sendthreewin)

    def retranslateUi(self, sendthreewin):
        _translate = QtCore.QCoreApplication.translate
        sendthreewin.setWindowTitle(_translate("sendthreewin", "MainWindow"))
        self.label.setText(_translate("sendthreewin", "Enter recipient information："))
        self.pushButton.setText(_translate("sendthreewin", "Continue"))
        self.pushButton_2.setText(_translate("sendthreewin", "cancel"))
        self.label_2.setText(_translate("sendthreewin", "Name of Recipient:"))
        self.label_3.setText(_translate("sendthreewin", "Telephone of Recopient:"))
        self.label_4.setText(_translate("sendthreewin", "Address of Recipient:"))
import images_rc
