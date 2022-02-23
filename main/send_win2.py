# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_win2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_send_windowtwo(object):
    def setupUi(self, send_windowtwo):
        send_windowtwo.setObjectName("send_windowtwo")
        send_windowtwo.resize(1200, 800)
        send_windowtwo.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(send_windowtwo)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 60, 531, 101))
        self.label_7.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.label_7.setObjectName("label_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 570, 320, 60))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 196, 197);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(880, 440, 181, 60))
        self.label_6.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 320, 60))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 320, 271, 60))
        self.label_2.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 320, 320, 60))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 200, 271, 60))
        self.label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.Big_re_label = QtWidgets.QLabel(self.centralwidget)
        self.Big_re_label.setGeometry(QtCore.QRect(770, 200, 71, 60))
        self.Big_re_label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.Big_re_label.setObjectName("Big_re_label")
        self.med_re_label = QtWidgets.QLabel(self.centralwidget)
        self.med_re_label.setGeometry(QtCore.QRect(770, 320, 61, 60))
        self.med_re_label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.med_re_label.setObjectName("med_re_label")
        self.small_re_label = QtWidgets.QLabel(self.centralwidget)
        self.small_re_label.setGeometry(QtCore.QRect(770, 440, 51, 60))
        self.small_re_label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.small_re_label.setObjectName("small_re_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 440, 271, 60))
        self.label_3.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 440, 320, 60))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(880, 320, 171, 60))
        self.label_5.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(880, 200, 211, 60))
        self.label_4.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_4.setObjectName("label_4")
        send_windowtwo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(send_windowtwo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        send_windowtwo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(send_windowtwo)
        self.statusbar.setObjectName("statusbar")
        send_windowtwo.setStatusBar(self.statusbar)

        self.retranslateUi(send_windowtwo)
        self.pushButton_2.clicked.connect(send_windowtwo.take_med_box)
        self.pushButton_3.clicked.connect(send_windowtwo.take_small_box)
        self.pushButton.clicked.connect(send_windowtwo.take_big_box)
        self.pushButton_5.clicked.connect(send_windowtwo.turn_sendwin1)
        QtCore.QMetaObject.connectSlotsByName(send_windowtwo)

    def retranslateUi(self, send_windowtwo):
        _translate = QtCore.QCoreApplication.translate
        send_windowtwo.setWindowTitle(_translate("send_windowtwo", "MainWindow"))
        self.label_7.setText(_translate("send_windowtwo", "<html><head/><body><p><span style=\" font-size:36pt;\">Choose the box size：</span></p></body></html>"))
        self.pushButton_5.setText(_translate("send_windowtwo", " cancel"))
        self.label_6.setText(_translate("send_windowtwo", "price: 10"))
        self.pushButton.setText(_translate("send_windowtwo", "Use Large Box"))
        self.label_2.setText(_translate("send_windowtwo", "The remaining："))
        self.pushButton_2.setText(_translate("send_windowtwo", "Use Medium Box"))
        self.label.setText(_translate("send_windowtwo", "The remaining："))
        self.Big_re_label.setText(_translate("send_windowtwo", "10"))
        self.med_re_label.setText(_translate("send_windowtwo", "10"))
        self.small_re_label.setText(_translate("send_windowtwo", "20"))
        self.label_3.setText(_translate("send_windowtwo", "The remaining："))
        self.pushButton_3.setText(_translate("send_windowtwo", "Use Small Box"))
        self.label_5.setText(_translate("send_windowtwo", "price: 15"))
        self.label_4.setText(_translate("send_windowtwo", "price: 20"))
import images_rc
