import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QTimer, Qt

num = 0


class my_num(QWidget):
    def __init__(self):
        super(my_num, self).__init__()
        self.InitUi()

    def InitUi(self):
        self.resize(600, 400)
        self.setWindowTitle('demo')
        self.btn_1 = QPushButton('累加', self)
        self.btn_1.setGeometry(60, 120, 150, 100)
        self.btn_1.clicked.connect(self.m_add)
        self.label = QLabel("<h1>0</h1>", self)  # 设置Label的字体大小，通过html的格式设置
        self.label.setGeometry(300, 120, 300, 100)
        self.label.setAlignment(Qt.AlignCenter)
        self.mt = QTimer(self)

    def my_timer(self):
        if self.btn_1.clicked:
            self.mt.singleShot(500, self.m_add)

    def m_add(self):
        global num
        num += 1
        print('num = {}'.format(num))
        self.label.setText("<h1>{}</h1>".format(num))
        self.my_timer()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = my_num()
    w.show()
    sys.exit(app.exec_())
