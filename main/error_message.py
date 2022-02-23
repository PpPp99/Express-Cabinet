# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_message.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error_landing(object):
    def setupUi(self, Error_landing):
        Error_landing.setObjectName("Error_landing")
        Error_landing.resize(500, 320)
        Error_landing.setStyleSheet("QDialog#Error_landing {\n"
"border-image:url(:/register/按键1.jpg)\n"
"}\n"
"")
        self.pushButton = QtWidgets.QPushButton(Error_landing)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 181, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 196, 197);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Error_landing)
        self.label.setGeometry(QtCore.QRect(-50, 70, 591, 101))
        self.label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")

        self.retranslateUi(Error_landing)
        self.pushButton.clicked.connect(Error_landing.close)
        QtCore.QMetaObject.connectSlotsByName(Error_landing)

    def retranslateUi(self, Error_landing):
        _translate = QtCore.QCoreApplication.translate
        Error_landing.setWindowTitle(_translate("Error_landing", "Dialog"))
        self.pushButton.setText(_translate("Error_landing", "confirm"))
        self.label.setText(_translate("Error_landing", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Your Telephone or Password is wrong!</span></p></body></html>"))
import images_rc
