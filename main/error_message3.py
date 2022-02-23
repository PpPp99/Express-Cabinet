# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_message3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error_overflow(object):
    def setupUi(self, Error_overflow):
        Error_overflow.setObjectName("Error_overflow")
        Error_overflow.resize(500, 320)
        Error_overflow.setStyleSheet("QDialog#Error_overflow {\n"
"border-image:url(:/register/按键1.jpg)\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Error_overflow)
        self.label.setGeometry(QtCore.QRect(-40, 70, 591, 101))
        self.label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Error_overflow)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 181, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 196, 197);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Error_overflow)
        self.pushButton.clicked.connect(Error_overflow.close)
        QtCore.QMetaObject.connectSlotsByName(Error_overflow)

    def retranslateUi(self, Error_overflow):
        _translate = QtCore.QCoreApplication.translate
        Error_overflow.setWindowTitle(_translate("Error_overflow", "Dialog"))
        self.label.setText(_translate("Error_overflow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Error! overflow!!!</span></p></body></html>"))
        self.pushButton.setText(_translate("Error_overflow", "confirm"))
import images_rc
