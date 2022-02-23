# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'put_window3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_put_win_three(object):
    def setupUi(self, put_win_three):
        put_win_three.setObjectName("put_win_three")
        put_win_three.resize(1200, 800)
        put_win_three.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(put_win_three)
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
        self.id_lab = QtWidgets.QLabel(self.centralwidget)
        self.id_lab.setGeometry(QtCore.QRect(515, 330, 71, 51))
        self.id_lab.setStyleSheet("font: 36pt \"Baskerville Old Face\";")
        self.id_lab.setObjectName("id_lab")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 165, 500, 320))
        self.label.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        put_win_three.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(put_win_three)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        put_win_three.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(put_win_three)
        self.statusbar.setObjectName("statusbar")
        put_win_three.setStatusBar(self.statusbar)

        self.retranslateUi(put_win_three)
        self.pushButton.clicked.connect(put_win_three.turn_put_win4)
        QtCore.QMetaObject.connectSlotsByName(put_win_three)

    def retranslateUi(self, put_win_three):
        _translate = QtCore.QCoreApplication.translate
        put_win_three.setWindowTitle(_translate("put_win_three", "MainWindow"))
        self.pushButton.setText(_translate("put_win_three", "Close the box"))
        self.id_lab.setText(_translate("put_win_three", "<html><head/><body><p>0</p></body></html>"))
        self.label.setText(_translate("put_win_three", "<html><head/><body><p><span style=\" font-size:36pt;\">The box is open!</span></p><p><span style=\" font-size:36pt;\">id is:</span><span style=\" font-size:36pt; text-decoration: underline;\">____</span></p></body></html>"))
import images_rc
