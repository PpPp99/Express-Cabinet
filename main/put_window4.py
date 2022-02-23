# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'put_window4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_put_win_four(object):
    def setupUi(self, put_win_four):
        put_win_four.setObjectName("put_win_four")
        put_win_four.resize(1200, 800)
        put_win_four.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(put_win_four)
        self.centralwidget.setObjectName("centralwidget")
        self.time_le = QtWidgets.QLabel(self.centralwidget)
        self.time_le.setGeometry(QtCore.QRect(830, 160, 71, 61))
        self.time_le.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.time_le.setObjectName("time_le")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 620, 531, 71))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 25pt \"Baskerville Old Face\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 430, 531, 71))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 250, 205);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 25pt \"Baskerville Old Face\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(15, 620, 531, 71))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 196, 197);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 25pt \"Baskerville Old Face\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(215, 140, 911, 221))
        self.label_2.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_2.setObjectName("label_2")
        put_win_four.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(put_win_four)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        put_win_four.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(put_win_four)
        self.statusbar.setObjectName("statusbar")
        put_win_four.setStatusBar(self.statusbar)

        self.retranslateUi(put_win_four)
        self.pushButton.clicked.connect(put_win_four.return_put_win1)
        self.pushButton_2.clicked.connect(put_win_four.reopen_box)
        self.pushButton_3.clicked.connect(put_win_four.return_mainwindow)
        QtCore.QMetaObject.connectSlotsByName(put_win_four)

    def retranslateUi(self, put_win_four):
        _translate = QtCore.QCoreApplication.translate
        put_win_four.setWindowTitle(_translate("put_win_four", "MainWindow"))
        self.time_le.setText(_translate("put_win_four", "<html><head/><body><p><span style=\" color:#000000;\">120</span></p></body></html>"))
        self.pushButton.setText(_translate("put_win_four", "Continue to send"))
        self.pushButton_2.setText(_translate("put_win_four", "reopen the box"))
        self.pushButton_3.setText(_translate("put_win_four", "renturn the mainwindow"))
        self.label_2.setText(_translate("put_win_four", "<html><head/><body><p><span style=\" font-size:24pt;\">System will return to main screen after ___s</span></p><p><span style=\" font-size:24pt;\">If you incorrectly close the box without take the express</span></p><p><span style=\" font-size:24pt;\">you can reopen the box in 2 minutes</span></p></body></html>"))
import images_rc
