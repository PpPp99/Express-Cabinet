import sys
from PyQt5.Qt import *
from User_input import Ui_MainWindow


class Win(QMainWindow,Ui_MainWindow):

    register_account_pwd_signal = pyqtSignal(str,str,str,str,str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  #调用父类
        self.setupUi(self)


    def registered(self):
        print("registered")
        telephone = self.telephone_le.text()
        name = self.name_le.text()
        address = self.address_le.text()
        balance = self.balance_le.text()
        password = self.password_le.text()
        print(telephone,name,address,balance,password)
        self.register_account_pwd_signal.emit(telephone,name,address,balance,password)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = Win()
    the_mainwindow.register_account_pwd_signal.connect(lambda t,n,a,b,p:print(t,n,a,b,p))
    the_mainwindow.show()
    sys.exit(app.exec_())