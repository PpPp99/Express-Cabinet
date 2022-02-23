import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Take_delivery import *
from error_message2 import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        #这里的setupUi()是几个意思？
        self.main_ui.setupUi(self)


class MyDialog(QDialog,Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    child = MyDialog()
    btn = win.main_ui.pushButton
    btn.clicked.connect(child.show)
    win.show()
    sys.exit(app.exec())