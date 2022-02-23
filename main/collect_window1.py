# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collect_window1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_collect_win_one(object):
    def setupUi(self, collect_win_one):
        collect_win_one.setObjectName("collect_win_one")
        collect_win_one.resize(1200, 800)
        collect_win_one.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(collect_win_one)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 70, 831, 71))
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
        self.label_3.setGeometry(QtCore.QRect(540, 440, 320, 60))
        self.label_3.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 320, 320, 60))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 440, 320, 60))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 20pt \"Showcard Gothic\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 200, 281, 60))
        self.label.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.big_box_lab = QtWidgets.QLabel(self.centralwidget)
        self.big_box_lab.setGeometry(QtCore.QRect(870, 200, 70, 60))
        self.big_box_lab.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.big_box_lab.setObjectName("big_box_lab")
        self.med_box_lab = QtWidgets.QLabel(self.centralwidget)
        self.med_box_lab.setGeometry(QtCore.QRect(870, 320, 70, 60))
        self.med_box_lab.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.med_box_lab.setObjectName("med_box_lab")
        self.small_box_lab = QtWidgets.QLabel(self.centralwidget)
        self.small_box_lab.setGeometry(QtCore.QRect(870, 440, 70, 60))
        self.small_box_lab.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.small_box_lab.setObjectName("small_box_lab")
        collect_win_one.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(collect_win_one)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        collect_win_one.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(collect_win_one)
        self.statusbar.setObjectName("statusbar")
        collect_win_one.setStatusBar(self.statusbar)

        self.retranslateUi(collect_win_one)
        self.pushButton_4.clicked.connect(collect_win_one.turn_courier_win2)
        self.pushButton.clicked.connect(collect_win_one.collect_big)
        self.pushButton_3.clicked.connect(collect_win_one.collect_small)
        self.pushButton_2.clicked.connect(collect_win_one.collect_med)
        QtCore.QMetaObject.connectSlotsByName(collect_win_one)

    def retranslateUi(self, collect_win_one):
        _translate = QtCore.QCoreApplication.translate
        collect_win_one.setWindowTitle(_translate("collect_win_one", "MainWindow"))
        self.label_7.setText(_translate("collect_win_one", "<html><head/><body><p><span style=\" font-size:36pt;\">Things that need to be delivered：</span></p></body></html>"))
        self.pushButton_4.setText(_translate("collect_win_one", "cancel"))
        self.pushButton.setText(_translate("collect_win_one", "The big size"))
        self.label_3.setText(_translate("collect_win_one", "The remaining："))
        self.label_2.setText(_translate("collect_win_one", "The remaining："))
        self.pushButton_2.setText(_translate("collect_win_one", "The Medium size"))
        self.pushButton_3.setText(_translate("collect_win_one", "The Small size"))
        self.label.setText(_translate("collect_win_one", "The remaining："))
        self.big_box_lab.setText(_translate("collect_win_one", "0"))
        self.med_box_lab.setText(_translate("collect_win_one", "0"))
        self.small_box_lab.setText(_translate("collect_win_one", "0"))
import images_rc
