# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'put_window1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_put_window_one(object):
    def setupUi(self, put_window_one):
        put_window_one.setObjectName("put_window_one")
        put_window_one.resize(1200, 800)
        put_window_one.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(put_window_one)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 60, 531, 101))
        self.label_7.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 560, 320, 60))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(255, 196, 197);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 320, 60))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 440, 320, 60))
        self.label_3.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 320, 320, 60))
        self.label_2.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 440, 320, 60))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
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
        self.label.setGeometry(QtCore.QRect(570, 200, 301, 60))
        self.label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.big_rem_lab = QtWidgets.QLabel(self.centralwidget)
        self.big_rem_lab.setGeometry(QtCore.QRect(900, 200, 50, 60))
        self.big_rem_lab.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.big_rem_lab.setObjectName("big_rem_lab")
        self.med_rem_lab = QtWidgets.QLabel(self.centralwidget)
        self.med_rem_lab.setGeometry(QtCore.QRect(900, 320, 70, 60))
        self.med_rem_lab.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.med_rem_lab.setObjectName("med_rem_lab")
        self.small_rem_lab = QtWidgets.QLabel(self.centralwidget)
        self.small_rem_lab.setGeometry(QtCore.QRect(900, 440, 70, 60))
        self.small_rem_lab.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.small_rem_lab.setObjectName("small_rem_lab")
        put_window_one.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(put_window_one)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        put_window_one.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(put_window_one)
        self.statusbar.setObjectName("statusbar")
        put_window_one.setStatusBar(self.statusbar)

        self.retranslateUi(put_window_one)
        self.pushButton.clicked.connect(put_window_one.turn_put_win2big)
        self.pushButton_2.clicked.connect(put_window_one.turn_put_win2med)
        self.pushButton_3.clicked.connect(put_window_one.turn_put_win2small)
        self.pushButton_4.clicked.connect(put_window_one.turn_courier_win2)
        QtCore.QMetaObject.connectSlotsByName(put_window_one)

    def retranslateUi(self, put_window_one):
        _translate = QtCore.QCoreApplication.translate
        put_window_one.setWindowTitle(_translate("put_window_one", "MainWindow"))
        self.label_7.setText(_translate("put_window_one", "<html><head/><body><p><span style=\" font-size:36pt;\">Choose the box size：</span></p></body></html>"))
        self.pushButton_4.setText(_translate("put_window_one", " cancel"))
        self.pushButton.setText(_translate("put_window_one", "Use Large Box"))
        self.label_3.setText(_translate("put_window_one", "The remaining："))
        self.label_2.setText(_translate("put_window_one", "The remaining："))
        self.pushButton_3.setText(_translate("put_window_one", "Use Small Box"))
        self.pushButton_2.setText(_translate("put_window_one", "Use Medium Box"))
        self.label.setText(_translate("put_window_one", "The remaining："))
        self.big_rem_lab.setText(_translate("put_window_one", "0"))
        self.med_rem_lab.setText(_translate("put_window_one", "0"))
        self.small_rem_lab.setText(_translate("put_window_one", "0"))
import images_rc
