# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'put_window2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_put_win_two(object):
    def setupUi(self, put_win_two):
        put_win_two.setObjectName("put_win_two")
        put_win_two.resize(1200, 800)
        put_win_two.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(put_win_two)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 50, 791, 131))
        self.label_3.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.label_3.setObjectName("label_3")
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
        self.label_2.setGeometry(QtCore.QRect(220, 210, 311, 51))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 320, 371, 51))
        self.label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.Rec_address_le = QtWidgets.QLineEdit(self.centralwidget)
        self.Rec_address_le.setGeometry(QtCore.QRect(680, 430, 361, 51))
        self.Rec_address_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.Rec_address_le.setObjectName("Rec_address_le")
        self.Rec_telephone_le = QtWidgets.QLineEdit(self.centralwidget)
        self.Rec_telephone_le.setGeometry(QtCore.QRect(680, 320, 361, 51))
        self.Rec_telephone_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.Rec_telephone_le.setObjectName("Rec_telephone_le")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 430, 351, 51))
        self.label_4.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_4.setObjectName("label_4")
        put_win_two.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(put_win_two)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        put_win_two.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(put_win_two)
        self.statusbar.setObjectName("statusbar")
        put_win_two.setStatusBar(self.statusbar)

        self.retranslateUi(put_win_two)
        self.pushButton.clicked.connect(put_win_two.turn_put_win3)
        self.pushButton_2.clicked.connect(put_win_two.turn_put_win1)
        QtCore.QMetaObject.connectSlotsByName(put_win_two)

    def retranslateUi(self, put_win_two):
        _translate = QtCore.QCoreApplication.translate
        put_win_two.setWindowTitle(_translate("put_win_two", "MainWindow"))
        self.label_3.setText(_translate("put_win_two", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Enter recipient information：</span></p></body></html>"))
        self.pushButton.setText(_translate("put_win_two", "confirm"))
        self.pushButton_2.setText(_translate("put_win_two", "cancel"))
        self.label_2.setText(_translate("put_win_two", "Receiver\'s Name:"))
        self.label.setText(_translate("put_win_two", "Receiver\'s Telephone:"))
        self.label_4.setText(_translate("put_win_two", "Receiver\'s Address:"))
import images_rc
