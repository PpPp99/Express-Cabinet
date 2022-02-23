# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_win4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sendfourwin(object):
    def setupUi(self, sendfourwin):
        sendfourwin.setObjectName("sendfourwin")
        sendfourwin.resize(1200, 800)
        sendfourwin.setStyleSheet("QWidget#centralwidget {\n"
"border-image: url(:/register/背景1.jpg)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(sendfourwin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 160, 500, 320))
        self.label.setStyleSheet("font: 40pt \"Baskerville Old Face\";")
        self.label.setObjectName("label")
        self.id_lab = QtWidgets.QLabel(self.centralwidget)
        self.id_lab.setGeometry(QtCore.QRect(500, 330, 71, 51))
        self.id_lab.setStyleSheet("font: 36pt \"Baskerville Old Face\";")
        self.id_lab.setObjectName("id_lab")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 490, 331, 71))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   border-radius: 25px;\n"
"   background-color:rgb(222, 254, 255);\n"
"   border:5px solid rgb(0, 0, 0);\n"
"   font: 30pt \"Baskerville Old Face\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        sendfourwin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sendfourwin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        sendfourwin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sendfourwin)
        self.statusbar.setObjectName("statusbar")
        sendfourwin.setStatusBar(self.statusbar)

        self.retranslateUi(sendfourwin)
        self.pushButton.clicked.connect(sendfourwin.turn_send_win5)
        QtCore.QMetaObject.connectSlotsByName(sendfourwin)

    def retranslateUi(self, sendfourwin):
        _translate = QtCore.QCoreApplication.translate
        sendfourwin.setWindowTitle(_translate("sendfourwin", "MainWindow"))
        self.label.setText(_translate("sendfourwin", "<html><head/><body><p><span style=\" font-size:36pt;\">The box is open!</span></p><p><span style=\" font-size:36pt;\">id is:</span><span style=\" font-size:36pt; text-decoration: underline;\">____</span></p></body></html>"))
        self.id_lab.setText(_translate("sendfourwin", "00"))
        self.pushButton.setText(_translate("sendfourwin", "Close the box"))
import images_rc
