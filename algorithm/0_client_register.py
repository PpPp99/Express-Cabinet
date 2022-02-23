
#用户注册新账户

import sys
import MySQLdb
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from Register_interface import Ui_MainWindow

class Win(QMainWindow, Ui_MainWindow):
    register_account_pwd_signal = pyqtSignal(str, str, str, str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)

    def registered(self):
        print("registered")
        telephone = self.telephone_le.text()
        name = self.name_le.text()
        address = self.address_le.text()
        balance = self.balance_le.text()
        password = self.password_le.text()
        self.register_account_pwd_signal.emit(telephone, name, address, balance, password)


def intodb(t, n, a, b, p):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='home',
    )
    cur = conn.cursor()
    cur.execute("insert into client values(%s,%s,%s,%s,%s)", (t, n, a, b, p))
    cur.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = Win()
    the_mainwindow.register_account_pwd_signal.connect(lambda t, n, a, b, p: intodb(t, n, a, b, p))
    the_mainwindow.show()
try:
    sys.exit(app.exec_())
except Exception as e:
    print(e)
finally:
    print(123)
