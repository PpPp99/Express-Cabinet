# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_input.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registered_win(object):
    def setupUi(self, registered_win):
        registered_win.setObjectName("registered_win")
        registered_win.resize(1200, 800)
        registered_win.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(registered_win)
        self.centralwidget.setObjectName("centralwidget")
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 380, 200, 50))
        self.label_3.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_3.setObjectName("label_3")
        self.balance_le = QtWidgets.QLineEdit(self.centralwidget)
        self.balance_le.setEnabled(False)
        self.balance_le.setGeometry(QtCore.QRect(530, 380, 71, 51))
        self.balance_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.balance_le.setObjectName("balance_le")
        self.address_le = QtWidgets.QLineEdit(self.centralwidget)
        self.address_le.setGeometry(QtCore.QRect(530, 300, 401, 51))
        self.address_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.address_le.setObjectName("address_le")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 300, 200, 51))
        self.label_2.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 220, 200, 50))
        self.label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.name_le = QtWidgets.QLineEdit(self.centralwidget)
        self.name_le.setGeometry(QtCore.QRect(530, 220, 401, 51))
        self.name_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.name_le.setObjectName("name_le")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 140, 200, 50))
        self.label_5.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_5.setObjectName("label_5")
        self.telephone_le = QtWidgets.QLineEdit(self.centralwidget)
        self.telephone_le.setGeometry(QtCore.QRect(530, 140, 401, 50))
        self.telephone_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.telephone_le.setObjectName("telephone_le")
        self.password_le = QtWidgets.QLineEdit(self.centralwidget)
        self.password_le.setGeometry(QtCore.QRect(530, 460, 401, 51))
        self.password_le.setStyleSheet("QLineEdit{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 255, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.password_le.setObjectName("password_le")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 460, 200, 50))
        self.label_4.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_4.setObjectName("label_4")
        registered_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(registered_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        registered_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(registered_win)
        self.statusbar.setObjectName("statusbar")
        registered_win.setStatusBar(self.statusbar)

        self.retranslateUi(registered_win)
        self.pushButton.clicked.connect(registered_win.registered)
        self.pushButton_2.clicked.connect(registered_win.return_send1)
        QtCore.QMetaObject.connectSlotsByName(registered_win)

    def retranslateUi(self, registered_win):
        _translate = QtCore.QCoreApplication.translate
        registered_win.setWindowTitle(_translate("registered_win", "MainWindow"))
        self.pushButton.setText(_translate("registered_win", "determine"))
        self.pushButton_2.setText(_translate("registered_win", "cancel"))
        self.label_3.setText(_translate("registered_win", "<html><head/><body><p>Balance：</p></body></html>"))
        self.balance_le.setText(_translate("registered_win", "100"))
        self.label_2.setText(_translate("registered_win", "<html><head/><body><p>Address：</p></body></html>"))
        self.label.setText(_translate("registered_win", "<html><head/><body><p>Name:</p></body></html>"))
        self.label_5.setText(_translate("registered_win", "<html><head/><body><p>Telephone:</p></body></html>"))
        self.telephone_le.setWhatsThis(_translate("registered_win", "<html><head/><body><p>QLineEdit{</p><p>   border-radius: 25px;</p><p>   background-color:rgb(255, 255, 255);</p><p>   border:5px solid rgb(0, 0, 0);</p><p>   font: 20pt &quot;Showcard Gothic&quot;;</p><p>}</p></body></html>"))
        self.label_4.setText(_translate("registered_win", "<html><head/><body><p>Password：</p></body></html>"))
import images_rc
