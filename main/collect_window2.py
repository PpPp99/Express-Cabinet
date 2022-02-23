# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collect_window2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_collect_win_two(object):
    def setupUi(self, collect_win_two):
        collect_win_two.setObjectName("collect_win_two")
        collect_win_two.resize(1200, 800)
        collect_win_two.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(collect_win_two)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 70, 241, 71))
        self.label.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(510, 80, 81, 51))
        self.id_label.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.id_label.setObjectName("id_label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 160, 371, 41))
        self.label_6.setStyleSheet("font: 25pt \"Baskerville Old Face\";")
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 390, 191, 31))
        self.label_3.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 300, 141, 31))
        self.label_4.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 220, 211, 41))
        self.label_8.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(420, 260, 101, 31))
        self.label_9.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 430, 91, 31))
        self.label_10.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(619, 260, 161, 31))
        self.label_11.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(619, 430, 171, 31))
        self.label_12.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(420, 470, 121, 31))
        self.label_13.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 560, 331, 71))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 30pt \"Baskerville Old Face\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.send_name_lab = QtWidgets.QLabel(self.centralwidget)
        self.send_name_lab.setGeometry(QtCore.QRect(520, 260, 91, 31))
        self.send_name_lab.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.send_name_lab.setObjectName("send_name_lab")
        self.send_telephone_lab = QtWidgets.QLabel(self.centralwidget)
        self.send_telephone_lab.setGeometry(QtCore.QRect(779, 260, 101, 31))
        self.send_telephone_lab.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.send_telephone_lab.setObjectName("send_telephone_lab")
        self.send_address_lab = QtWidgets.QLabel(self.centralwidget)
        self.send_address_lab.setGeometry(QtCore.QRect(550, 300, 251, 31))
        self.send_address_lab.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.send_address_lab.setObjectName("send_address_lab")
        self.rec_name_lab = QtWidgets.QLabel(self.centralwidget)
        self.rec_name_lab.setGeometry(QtCore.QRect(520, 430, 91, 31))
        self.rec_name_lab.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.rec_name_lab.setObjectName("rec_name_lab")
        self.rec_telephone_lab = QtWidgets.QLabel(self.centralwidget)
        self.rec_telephone_lab.setGeometry(QtCore.QRect(779, 430, 141, 31))
        self.rec_telephone_lab.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.rec_telephone_lab.setObjectName("rec_telephone_lab")
        self.rec_address_lab = QtWidgets.QLabel(self.centralwidget)
        self.rec_address_lab.setGeometry(QtCore.QRect(550, 470, 251, 31))
        self.rec_address_lab.setStyleSheet("font: 20pt \"Baskerville Old Face\";")
        self.rec_address_lab.setObjectName("rec_address_lab")
        collect_win_two.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(collect_win_two)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        collect_win_two.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(collect_win_two)
        self.statusbar.setObjectName("statusbar")
        collect_win_two.setStatusBar(self.statusbar)

        self.retranslateUi(collect_win_two)
        self.pushButton.clicked.connect(collect_win_two.turn_collect_win3)
        QtCore.QMetaObject.connectSlotsByName(collect_win_two)

    def retranslateUi(self, collect_win_two):
        _translate = QtCore.QCoreApplication.translate
        collect_win_two.setWindowTitle(_translate("collect_win_two", "MainWindow"))
        self.label.setText(_translate("collect_win_two", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">id:____</span></p></body></html>"))
        self.id_label.setWhatsThis(_translate("collect_win_two", "<html><head/><body><p>0</p></body></html>"))
        self.id_label.setText(_translate("collect_win_two", "00"))
        self.label_6.setText(_translate("collect_win_two", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Delivery information:</span></p></body></html>"))
        self.label_3.setText(_translate("collect_win_two", "<html><head/><body><p>The recipient:</p></body></html>"))
        self.label_4.setText(_translate("collect_win_two", "Address:"))
        self.label_8.setText(_translate("collect_win_two", "<html><head/><body><p>The sender:</p></body></html>"))
        self.label_9.setText(_translate("collect_win_two", "Name:"))
        self.label_10.setText(_translate("collect_win_two", "Name:"))
        self.label_11.setText(_translate("collect_win_two", "Telephone:"))
        self.label_12.setText(_translate("collect_win_two", "Telephone:"))
        self.label_13.setText(_translate("collect_win_two", "Address:"))
        self.pushButton.setText(_translate("collect_win_two", "close the box"))
        self.send_name_lab.setText(_translate("collect_win_two", "Ning"))
        self.send_telephone_lab.setText(_translate("collect_win_two", "654321"))
        self.send_address_lab.setText(_translate("collect_win_two", "IG"))
        self.rec_name_lab.setText(_translate("collect_win_two", "Tian"))
        self.rec_telephone_lab.setText(_translate("collect_win_two", "123456"))
        self.rec_address_lab.setText(_translate("collect_win_two", "FPX"))
import images_rc
