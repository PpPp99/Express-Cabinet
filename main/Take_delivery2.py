# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Take_delivery2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_End_win(object):
    def setupUi(self, End_win):
        End_win.setObjectName("End_win")
        End_win.resize(1200, 800)
        End_win.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(End_win)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 490, 331, 71))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 30pt \"Baskerville Old Face\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 160, 500, 320))
        self.label.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.id_lab = QtWidgets.QLabel(self.centralwidget)
        self.id_lab.setGeometry(QtCore.QRect(550, 310, 191, 71))
        self.id_lab.setStyleSheet("font: 36pt \"Baskerville Old Face\";")
        self.id_lab.setObjectName("id_lab")
        End_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(End_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        End_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(End_win)
        self.statusbar.setObjectName("statusbar")
        End_win.setStatusBar(self.statusbar)

        self.retranslateUi(End_win)
        self.pushButton.clicked.connect(End_win.turn_delivery3)
        QtCore.QMetaObject.connectSlotsByName(End_win)

    def retranslateUi(self, End_win):
        _translate = QtCore.QCoreApplication.translate
        End_win.setWindowTitle(_translate("End_win", "MainWindow"))
        self.pushButton.setText(_translate("End_win", "close the box"))
        self.label.setText(_translate("End_win", "<html><head/><body><p><span style=\" font-size:36pt;\">The box is open !</span></p><p><span style=\" font-size:36pt;\">Id is : </span><span style=\" font-size:36pt; text-decoration: underline;\">____</span></p></body></html>"))
        self.id_lab.setText(_translate("End_win", "0"))
import images_rc
