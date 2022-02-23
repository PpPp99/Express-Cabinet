import random
import sys
import MySQLdb
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Take_delivery3 import *
from Take_delivery2 import *
from Take_delivery import *
from main_window import *
from error_message3 import *
from error_message2 import *
from error_message import *
from send_win1 import *
from send_win2 import *
from send_win3 import *
from send_win4 import *
from send_win5 import *
from courier_win1 import *
from courier_win2 import *
from put_window1 import *
from put_window2 import *
from put_window3 import *
from put_window4 import *
from User_input import *
from collect_window1 import *
from collect_window2 import *
from collect_window3 import *

id = 0
num = 120
big_num = 10
med_num = 10
small_num = 20
t1 = 0
n1 = 0
c1 = 0
value = 0

# Take_delivery2界面 显示行列
class endWindow(QMainWindow, Ui_End_win):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.Output_id()

    def Output_id(self):
        global id
        self.id_lab.setText(format(id))

    def close_box(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        find_id = "update home.machine set open_close='close' where id = %s"
        cur = conn.cursor()
        try:
            global id
            cur.execute(find_id, [id])
        except:
            print("Check failed")
        finally:
            cur.close()
            conn.commit()
            conn.close()

    WindowList = []

    def turn_delivery3(self):
        self.close_box()
        the_window = delivery_three_win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# Take_delivery3界面 结束
class delivery_three_win(QMainWindow, Ui_take_delivery_three):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.mt = QTimer(self)
        self.m_sub()

    WinList = []

    def return_mainwindow(self):
        global num
        num = -100
        self.clear_express()
        self.clear_box_data()
        the_window = FirstMainWindow()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def clear_express(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            # find telephone
            find_sender = "select sender_telephone from home.express where id = %s"
            find_receiver = "select receiver_telephone from home.express where id = %s"
            cur = conn.cursor()
            global id
            cur.execute(find_sender, [id])
            sender_tele = cur.fetchone()
            t1 = sender_tele[0]
            cur.execute(find_receiver, [id])
            receiver_tele = cur.fetchone()
            t2 = receiver_tele[0]
            # delete line in two side tables
            delete_sender = "delete from home.sender where telephone = %s order by time"
            delete_receiver = "delete from home.receiver where telephone = %s order by time"
            delete_express = "delete from home.express where id = %s"
            cur.execute(delete_sender, [t1])
            print("sender deleted")
            cur.execute(delete_receiver, [t2])
            print("receiver deleted")
            cur.execute(delete_express, [id])
            print("express deleted")
            cur.close()
            conn.commit()
            conn.close()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def clear_box_data(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        find_id = "update home.machine set attribution='empty' , pickupcode='0' where id = %s"
        cur = conn.cursor()
        try:
            global id
            cur.execute(find_id, [id])
        except:
            print("Empty failed")
        finally:
            cur.close()
            conn.commit()
            conn.close()

    def m_sub(self):
        global num
        num -= 1
        print('num = {}'.format(num))
        if num > 0:
            self.time_le.setText(format(num))
            self.the_world()
        elif num <= -100:
            num = 120
        else:

            self.return_mainwindow()
            num = 120

    WindowList = []

    def return_put_win1(self):
        global num
        num = -100
        self.clear_express()
        self.clear_box_data()
        the_window = SecondWindow()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    WindowtheList = []

    def reopen_box(self):
        global num
        num = -100
        global id
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        find_id = "update home.machine set open_close='open' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(find_id, [id])
        except:
            print("Check failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()
        the_window = endWindow()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def the_world(self):
        self.mt.singleShot(1000, self.m_sub)


# error_message2界面 报错
class MyDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)

class MyDialog2(QDialog, Ui_Error_landing):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Error_landing()
        self.child.setupUi(self)

class MyDialog3(QDialog, Ui_Error_overflow):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Error_overflow()
        self.child.setupUi(self)


# Take_delivery界面 输入快递code
class SecondWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)

    def Turn_dialog(self):
        self.Ui_dialog = MyDialog()
        self.Ui_dialog.show()

    WinList = []

    def Turn_end(self):
        the_window = endWindow()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def textchange(self):
        code = self.code_le.text()
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        get_pickupcode = "select id from home.machine where find_in_set(%s, pickupcode) > 0 and attribution='to_be_taken'"
        open_cabinet = "update home.machine set open_close='open' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(get_pickupcode, [code])
            id_line = cur.fetchone()
            global id
            id = id_line[0]
            print(id)
            if id > 0:
                print("pickup！code！ Best Match!")
            cur.execute(open_cabinet, [id])
            print("cabinet is open")
            self.Turn_end()
        except:
            print("Match failed")
            self.Turn_dialog()
        finally:
            cur.close()
            conn.commit()
            conn.close()


    WindowList = []

    def Retur_main(self):
        the_window = FirstMainWindow()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# main_window界面
class FirstMainWindow(QMainWindow, Ui_Main):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)

    windowList = []

    def turn_win(self):
        the_window = SecondWindow()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    twowindowList = []

    def turn_send_win(self):
        the_swindow = send_FirstWin()
        self.twowindowList.append(the_swindow)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_swindow.show()

    threewindowList = []

    def turn_courier_win(self):
        the_twindow = courier_one_win()
        self.threewindowList.append(the_twindow)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_twindow.show()


# send_win1界面 登陆界面
class send_FirstWin(QMainWindow, Ui_send_Firstwin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)

    def Turn_dialog(self):
        self.Ui_dialog = MyDialog2()
        self.Ui_dialog.show()

    WinList = []

    def Turn_send_three(self):
        the_window = send_two_Win()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    WintwoList = []

    def turn_registered(self):
        the_window = registered_window()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def Turn_send2(self):
        print("open the new window.")
        telephone = self.User_name_le.text()
        code = self.send_passage_le.text()
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        log_in = "select name from home.client where find_in_set(%s, telephone) > 0 and find_in_set(%s, code)> 0"
        cur = conn.cursor()
        try:
            cur.execute(log_in, [telephone, code])
            name = cur.fetchone()
            if name[0] != 0:
                print("Hello! %s" % name)
            get_sender_address = "select address from home.client where find_in_set(%s, telephone) > 0 and find_in_set(%s, code)> 0"
            global n1
            n1 = name
            cur.execute(get_sender_address, [telephone, code])
            a1_line = cur.fetchone()
            a1 = a1_line[0]
            input_sender = "insert into home.sender (telephone,name,address) values(%s,%s,%s)"
            cur.execute(input_sender, [telephone, n1, a1])
            global t1
            t1 = telephone
            print("sender added")
            self.Turn_send_three()
        except:
            self.Turn_dialog()
        finally:
            cur.close()
            conn.commit()
            conn.close()

    WindowList = []

    def Retur_main(self):
        the_window = FirstMainWindow()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# send_win2界面 选择箱子
def v_code():
    ret = ""
    for i in range(6):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))#ASCII表示数字
        Letter = chr(random.randint(65, 90))  # 取大写字母
        s = str(random.choice([num, Letter]))
        ret += s
    return ret

class send_two_Win(QMainWindow, Ui_send_windowtwo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.sql_number_data()

    def detemain_box_number(self):
        global big_num ,med_num,small_num
        print(big_num,med_num,small_num)
        if big_num>0:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
        if med_num>0:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
        if small_num>0:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)

    #显示剩余箱子
    def sql_number_data(self):
        global big_num
        global med_num
        global small_num
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        s = "Small"
        m = "Medium"
        l = "Large"
        find_empty = "select count(*) from home.machine where attribution='empty' and size=%s"
        cur = conn.cursor()
        try:
            cur.execute(find_empty, [l])
            l_count_line = cur.fetchone()
            big_num = l_count_line[0]
            cur.execute(find_empty, [m])
            m_count_line = cur.fetchone()
            med_num = m_count_line[0]
            cur.execute(find_empty, [s])
            s_count_line = cur.fetchone()
            small_num = s_count_line[0]
            self.Big_re_label.setText(format(big_num))
            self.med_re_label.setText(format(med_num))
            self.small_re_label.setText(format(small_num))
            self.detemain_box_number()

        except:
            print("Check failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()

    WindowList = []

    def turn_sendwin3(self):
        the_window = send_three_win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def delete_sender(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            # find telephone
            global t1
            cur = conn.cursor()
            try:
                # delete line in two side tables
                delete_sender = "delete from home.sender where telephone = %s order by time desc limit 1"
                cur.execute(delete_sender, [t1])
                print("sender deleted")
                cur.close()
                conn.commit()
                conn.close()
            except:
                print("Express delete error")
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def take_big_box(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            password = v_code()
            print("password: %s" % password)
            s = "Small"
            m = "Medium"
            l = "Large"
            attribution_change = "update home.machine set attribution='pending' where size = %s and attribution='empty' order by id limit 1 "
            pickupcode_add = "update home.machine set pickupcode = %s where pickupcode = '0' and size = %s and attribution='pending' order by id limit 1 "
            find_id = "select id from home.machine where size = %s and attribution='pending' order by UpdateTime desc limit 1"
            cur = conn.cursor()
            cur.execute(attribution_change, [l])
            print("attribution changed")
            cur.execute(pickupcode_add, [password, l])
            print("pickupcode added")
            cur.execute(find_id, [l])
            id_line = cur.fetchone()
            global id
            id = id_line[0]
            print(id)
            global value
            value = 20
            find_all = "select count(*) from home.machine where size=%s"
            find_rest = "select count(*) from home.machine where attribution='empty' and size=%s"
            cur.execute(find_all, [l])
            all_line = cur.fetchone()
            all = all_line[0]
            cur.execute(find_rest, [l])
            count_line = cur.fetchone()
            count = count_line[0]
            if count / all > 0.2:
                print("enough")
            else:
                find_early_id = "select id from home.machine where pickupcode <> '0' order by UpdateTime limit 1"
                find_early = "select receiver_telephone from home.express where id = %s"
                cur.execute(find_early_id)
                e_id_line = cur.fetchone()
                eid = e_id_line[0]
                cur.execute(find_early, [eid])
                tele_line = cur.fetchone()
                tele = tele_line[0]
                print("Rest space of size '", l, "' in express machine is less than 20%")
                print("Remind message has been sent to telephone number:", tele)


            cur.close()
            conn.commit()
            conn.close()
            self.turn_sendwin3()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def take_med_box(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            password = v_code()
            print("password: %s" % password)
            s = "Small"
            m = "Medium"
            l = "Large"
            attribution_change = "update home.machine set attribution='pending' where size = %s and attribution='empty' order by id limit 1 "
            pickupcode_add = "update home.machine set pickupcode = %s where pickupcode = '0' and size = %s and attribution='pending' order by id limit 1 "
            find_id = "select id from home.machine where size = %s and attribution='pending' order by UpdateTime desc limit 1"
            cur = conn.cursor()
            cur.execute(attribution_change, [m])
            print("attribution changed")
            cur.execute(pickupcode_add, [password, m])
            print("pickupcode added")
            cur.execute(find_id, [m])
            id_line = cur.fetchone()
            global id
            id = id_line[0]
            print(id)
            global value
            value = 15
            find_all = "select count(*) from home.machine where size=%s"
            find_rest = "select count(*) from home.machine where attribution='empty' and size=%s"
            cur.execute(find_all, [m])
            all_line = cur.fetchone()
            all = all_line[0]
            cur.execute(find_rest, [m])
            count_line = cur.fetchone()
            count = count_line[0]
            if count / all > 0.2:
                print("enough")
            else:
                find_early_id = "select id from home.machine where pickupcode <> '0' order by UpdateTime limit 1"
                find_early = "select receiver_telephone from home.express where id = %s"
                cur.execute(find_early_id)
                e_id_line = cur.fetchone()
                eid = e_id_line[0]
                cur.execute(find_early, [eid])
                tele_line = cur.fetchone()
                tele = tele_line[0]
                print("Rest space of size '", m, "' in express machine is less than 20%")
                print("Remind message has been sent to telephone number:", tele)

            cur.close()
            conn.commit()
            conn.close()
            self.turn_sendwin3()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def take_small_box(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            password = v_code()
            print("password: %s" % password)
            s = "Small"
            m = "Medium"
            l = "Large"
            attribution_change = "update home.machine set attribution='pending' where size = %s and attribution='empty' order by id limit 1 "
            pickupcode_add = "update home.machine set pickupcode = %s where pickupcode = '0' and size = %s and attribution='pending' order by id limit 1 "
            find_id = "select id from home.machine where size = %s and attribution='pending' order by UpdateTime desc limit 1"
            cur = conn.cursor()
            cur.execute(attribution_change, [s])
            print("attribution changed")
            cur.execute(pickupcode_add, [password, s])
            print("pickupcode added")
            cur.execute(find_id, [s])
            id_line = cur.fetchone()
            global id
            id = id_line[0]
            print(id)
            global value
            value = 10

            find_all = "select count(*) from home.machine where size=%s"
            find_rest = "select count(*) from home.machine where attribution='empty' and size=%s"
            cur.execute(find_all, [l])
            all_line = cur.fetchone()
            all = all_line[0]
            cur.execute(find_rest, [l])
            count_line = cur.fetchone()
            count = count_line[0]
            if count / all > 0.2:
                print("enough")
            else:
                find_early_id = "select id from home.machine where pickupcode <> '0' order by UpdateTime limit 1"
                find_early = "select receiver_telephone from home.express where id = %s"
                cur.execute(find_early_id)
                e_id_line = cur.fetchone()
                eid = e_id_line[0]
                cur.execute(find_early, [eid])
                tele_line = cur.fetchone()
                tele = tele_line[0]
                print("Rest space of size '", s, "' in express machine is less than 20%")
                print("Remind message has been sent to telephone number:", tele)


            cur.close()
            conn.commit()
            conn.close()
            self.turn_sendwin3()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    WinList = []

    def turn_sendwin1(self):
        self.delete_sender()
        the_window = send_FirstWin()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# send_win3界面
class send_three_win(QMainWindow, Ui_sendthreewin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)

    def Turn_dialog(self):
        self.Ui_dialog = MyDialog3()
        self.Ui_dialog.show()

    WinList = []

    def Turn_end(self):
        the_windows = send_four_win()
        self.WinList.append(the_windows)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_windows.show()

    def turn_to_win4(self):
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            if n1 != 0:
                print("Welcome to express system! %s"% n1)
                t2 = self.Rec_tele_le.text()  # 输入寄给谁
                n2 = self.Rec_name_le.text()
                a2 = self.Rec_address_le.text()
                if len(t2) <=11 and len(n2)<=10 and len(a2)<=100:
                    # 打开指定箱子
                    global id  # 放入物品，返回坐标
                    open_box = "update home.machine set open_close = 'open' where id = %s"
                    input_receiver = "insert into home.receiver (telephone,name,address) values(%s,%s,%s)"
                    input_express = "insert into home.express (sender_telephone,receiver_telephone,id) values(%s,%s,%s)"
                    global t1
                    cur = conn.cursor()
                    cur.execute(input_receiver, [t2, n2, a2])
                    print("receiver added")
                    cur.execute(input_express, [t1, t2, id])
                    print("express added")
                    cur.execute(open_box, [id])
                    print("cabinet open")
                    #判断容量

                    cur.close()
                    conn.commit()
                    conn.close()
                    self.Turn_end()
                else:
                    self.Turn_dialog()
            else:
               print("Express enter error")
               sys.exit(1)  # 需要循环结构



    def delete_box(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        global id
        find_id = "update home.machine set attribution='empty' , pickupcode='0' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(find_id, [id])
        except:
            print("Empty failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()

    WindowList = []

    def turn_to_win2(self):
        self.delete_box()
        #        print("第二个send界面打开")
        the_window = send_two_Win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# send_win4界面
class send_four_win(QMainWindow, Ui_sendfourwin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.Output_id()

    def Output_id(self):
        global id
        self.id_lab.setText(format(id))

    def close_box(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        global id
        find_id = "update home.machine set open_close='close' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(find_id, [id])
        except:
            print("Check failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()

    WindowList = []

    def turn_send_win5(self):
        self.close_box()
        the_window = send_five_Win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# send_win5界面
class send_five_Win(QMainWindow, Ui_sendfivewin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.mt = QTimer(self)
        self.m_sub()

    def money(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        cur = conn.cursor()
        pay_money = "update home.client set balance = balance - %s where telephone = %s"
        global value
        cur.execute(pay_money, [value, t1])
        print("money paid")
        cur.close()
        conn.commit()
        conn.close()

    WinList = []

    def return_mainwindow(self):
        global num
        num = -100
        self.money()
        the_window = FirstMainWindow()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def m_sub(self):
        global num
        num -= 1
        print('num = {}'.format(num))
        if num > 0:
            self.time_le.setText(format(num))
            self.The_world()
        elif num < -100:
            num = 120
        else:
            self.return_mainwindow()
            num = 120

    def reinput_user(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        cur = conn.cursor()
        get_sender_address = "select address from home.client where find_in_set(%s, telephone) > 0"
        global n1,t1
        cur.execute(get_sender_address, [t1])
        a1_line = cur.fetchone()
        a1 = a1_line[0]
        input_sender = "insert into home.sender (telephone,name,address) values(%s,%s,%s)"
        cur.execute(input_sender, [t1, n1, a1])
        print("sender added")
        cur.close()
        conn.commit()
        conn.close()

    WindowList = []

    def turn_send_win1(self):
        global num
        num = -100
        self.money()
        self.reinput_user()
        the_window = send_two_Win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    WindowtheList = []

    def reopen_box(self):
        global num
        num = -100
        global id
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        find_id = "update home.machine set open_close='open' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(find_id, [id])
        except:
            print("Check failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()
        the_window = send_four_win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def The_world(self):
        self.mt.singleShot(1000, self.m_sub)


# cuorier_win1界面
class courier_one_win(QMainWindow, Ui_courier_win_one):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)

    def Turn_dialog(self):
        self.Ui_dialog = MyDialog2()
        self.Ui_dialog.show()

    WinList = []

    def sure_passage(self):
        the_window = courier_two_win()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def turn_courier_win1(self):
        telephone = self.courier_name_le.text()
        code = self.courier_passage_le.text()
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        log_in = "select name from home.courier where find_in_set(%s, telephone) > 0 and find_in_set(%s, code)> 0"
        cur = conn.cursor()
        try:
            cur.execute(log_in, [telephone, code])
            name = cur.fetchone()
            if name[0] != 0:
                print("Hello! %s" % name)
            get_sender_company = "select company from home.courier where find_in_set(%s, telephone) > 0 and find_in_set(%s, code)> 0"
            global n1
            global c1
            n1 = name
            cur.execute(get_sender_company, [telephone, code])
            c1_line = cur.fetchone()
            c1 = c1_line[0]
            global t1
            t1 = telephone

            self.sure_passage()
        except:
            self.Turn_dialog()
        finally:
            cur.close()
            conn.commit()
            conn.close()

    def turn_registered_win(self):
        print("open registered window")

    WindowList = []

    def turn_main_win(self):
        the_window = FirstMainWindow()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# courier_win2界面
class courier_two_win(QMainWindow, Ui_courier_win_two):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)

    def insert_courier(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        cur = conn.cursor()
        global t1, n1, c1
        input_sender = "insert into home.sender (telephone,name,address) values(%s,%s,%s)"
        cur.execute(input_sender, [t1, n1, c1])
        print(t1, n1, c1)
        print("sender added")
        cur.close()
        conn.commit()
        conn.close()

    WindowList = []

    def Put_window(self):
        self.insert_courier()
        print("open put window")
        the_window = courier_put_one_win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    win = []

    def courier_window(self):
        the_window = courier_one_win()
        self.win.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    WinList = []

    def Collect_window(self):
        print("open put window")
        the_window = courier_collect_one_win()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# put_window1界面 选择箱子
class courier_put_one_win(QMainWindow, Ui_put_window_one):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.sql_number_data()

    def detemain_box_number(self):
        global big_num ,med_num,small_num
        print(big_num,med_num,small_num)
        if big_num>0:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
        if med_num>0:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
        if small_num>0:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)

    WindowList = []

    def turn_put_win2(self):
        the_window = courier_put_two_win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def delete_sender(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            # find telephone
            global t1
            cur = conn.cursor()
            try:
                # delete line in two side tables
                delete_sender = "delete from home.sender where telephone = %s order by time desc limit 1"
                cur.execute(delete_sender, [t1])
                print("sender deleted")
                cur.close()
                conn.commit()
                conn.close()
            except:
                print("Express delete error")
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def sql_number_data(self):
        global big_num
        global med_num
        global small_num
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        s = "Small"
        m = "Medium"
        l = "Large"
        find_empty = "select count(*) from home.machine where attribution='empty' and size=%s"
        cur = conn.cursor()
        try:
            cur.execute(find_empty, [l])
            l_count_line = cur.fetchone()
            big_num = l_count_line[0]
            cur.execute(find_empty, [m])
            m_count_line = cur.fetchone()
            med_num = m_count_line[0]
            cur.execute(find_empty, [s])
            s_count_line = cur.fetchone()
            small_num = s_count_line[0]
            self.big_rem_lab.setText(format(big_num))
            self.med_rem_lab.setText(format(med_num))
            self.small_rem_lab.setText(format(small_num))
            self.detemain_box_number()
        except:
            print("Check failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()

    def turn_put_win2big(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            password = v_code()
            print("password: %s" % password)
            s = "Small"
            m = "Medium"
            l = "Large"
            attribution_change = "update home.machine set attribution='to_be_taken' where size = %s and attribution='empty' order by id limit 1 "
            pickupcode_add = "update home.machine set pickupcode = %s where pickupcode = '0' and size = %s and attribution='to_be_taken' order by id limit 1 "
            find_id = "select id from home.machine where size = %s and attribution='to_be_taken' order by UpdateTime desc limit 1"
            cur = conn.cursor()
            cur.execute(attribution_change, [l])
            print("attribution changed")
            cur.execute(pickupcode_add, [password, l])
            print("pickupcode added")
            cur.execute(find_id, [l])
            id_line = cur.fetchone()
            global id
            id = id_line[0]
            print(id)

            find_all = "select count(*) from home.machine where size=%s"
            find_rest = "select count(*) from home.machine where attribution='empty' and size=%s"
            cur.execute(find_all, [l])
            all_line = cur.fetchone()
            all = all_line[0]
            cur.execute(find_rest, [l])
            count_line = cur.fetchone()
            count = count_line[0]
            if count / all > 0.2:
                print("enough")
            else:
                find_early_id = "select id from home.machine where pickupcode <> '0' order by UpdateTime limit 1"
                find_early = "select receiver_telephone from home.express where id = %s"
                cur.execute(find_early_id)
                e_id_line = cur.fetchone()
                eid = e_id_line[0]
                cur.execute(find_early, [eid])
                tele_line = cur.fetchone()
                tele = tele_line[0]
                print("Rest space of size '", l, "' in express machine is less than 20%")
                print("Remind message has been sent to telephone number:", tele)

            cur.close()
            conn.commit()
            conn.close()
            self.turn_put_win2()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def turn_put_win2med(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            password = v_code()
            print("password: %s" % password)
            s = "Small"
            m = "Medium"
            l = "Large"
            attribution_change = "update home.machine set attribution='to_be_taken' where size = %s and attribution='empty' order by id limit 1 "
            pickupcode_add = "update home.machine set pickupcode = %s where pickupcode = '0' and size = %s and attribution='to_be_taken' order by id limit 1 "
            find_id = "select id from home.machine where size = %s and attribution='to_be_taken' order by UpdateTime desc limit 1"
            cur = conn.cursor()
            cur.execute(attribution_change, [m])
            print("attribution changed")
            cur.execute(pickupcode_add, [password, m])
            print("pickupcode added")
            cur.execute(find_id, [m])
            id_line = cur.fetchone()
            global id
            id = id_line[0]
            print(id)

            find_all = "select count(*) from home.machine where size=%s"
            find_rest = "select count(*) from home.machine where attribution='empty' and size=%s"
            cur.execute(find_all, [m])
            all_line = cur.fetchone()
            all = all_line[0]
            cur.execute(find_rest, [m])
            count_line = cur.fetchone()
            count = count_line[0]
            if count / all > 0.2:
                print("enough")
            else:
                find_early_id = "select id from home.machine where pickupcode <> '0' order by UpdateTime limit 1"
                find_early = "select receiver_telephone from home.express where id = %s"
                cur.execute(find_early_id)
                e_id_line = cur.fetchone()
                eid = e_id_line[0]
                cur.execute(find_early, [eid])
                tele_line = cur.fetchone()
                tele = tele_line[0]
                print("Rest space of size '", m, "' in express machine is less than 20%")
                print("Remind message has been sent to telephone number:", tele)

            cur.close()
            conn.commit()
            conn.close()
            self.turn_put_win2()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def turn_put_win2small(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            password = v_code()
            print("password: %s" % password)
            s = "Small"
            m = "Medium"
            l = "Large"
            attribution_change = "update home.machine set attribution='to_be_taken' where size = %s and attribution='empty' order by id limit 1 "
            pickupcode_add = "update home.machine set pickupcode = %s where pickupcode = '0' and size = %s and attribution='to_be_taken' order by id limit 1 "
            find_id = "select id from home.machine where size = %s and attribution='to_be_taken' order by UpdateTime desc limit 1"
            cur = conn.cursor()
            cur.execute(attribution_change, [s])
            print("attribution changed")
            cur.execute(pickupcode_add, [password, s])
            print("pickupcode added")
            cur.execute(find_id, [s])
            id_line = cur.fetchone()
            global id
            id = id_line[0]
            print(id)

            find_all = "select count(*) from home.machine where size=%s"
            find_rest = "select count(*) from home.machine where attribution='empty' and size=%s"
            cur.execute(find_all, [s])
            all_line = cur.fetchone()
            all = all_line[0]
            cur.execute(find_rest, [s])
            count_line = cur.fetchone()
            count = count_line[0]
            if count / all > 0.2:
                print("enough")
            else:
                find_early_id = "select id from home.machine where pickupcode <> '0' order by UpdateTime limit 1"
                find_early = "select receiver_telephone from home.express where id = %s"
                cur.execute(find_early_id)
                e_id_line = cur.fetchone()
                eid = e_id_line[0]
                cur.execute(find_early, [eid])
                tele_line = cur.fetchone()
                tele = tele_line[0]
                print("Rest space of size '", s, "' in express machine is less than 20%")
                print("Remind message has been sent to telephone number:", tele)

            cur.close()
            conn.commit()
            conn.close()
            self.turn_put_win2()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    WinList = []

    def turn_courier_win2(self):
        self.delete_sender()
        the_window = courier_two_win()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# put_window2界面 输入信息
class courier_put_two_win(QMainWindow, Ui_put_win_two):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)

    def Turn_dialog(self):
        self.Ui_dialog = MyDialog3()
        self.Ui_dialog.show()

    def delete_box(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        global id
        find_id = "update home.machine set attribution='empty' , pickupcode='0' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(find_id, [id])
        except:
            print("Empty failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()

    WinList = []

    def turn_put_win1(self):
        self.delete_box()
        the_window = courier_put_one_win()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    WindowList = []

    def turn_put_win3(self):
        self.data_change()

    def turn_put_last_win(self):
        the_window = courier_put_three_win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def data_change(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            try:
                if n1 != 0:
                    print("Thank you for your hard work! %s"%n1)
                    n2 = self.Rec_name_le.text()
                    t2 = self.Rec_telephone_le.text()
                    a2 = self.Rec_name_le.text()
                    if len(t2) <= 11 and len(n2) <= 10 and len(a2) <= 100:
                        global id
                        input_receiver = "insert into home.receiver (telephone,name,address) values(%s,%s,%s)"
                        input_express = "insert into home.express (sender_telephone,receiver_telephone,id) values(%s,%s,%s)"
                        open_box = "update home.machine set open_close = 'open' where id = %s"
                        global t1
                        cur = conn.cursor()
                        cur.execute(input_receiver, [t2, n2, a2])
                        print("receiver added")
                        cur.execute(input_express, [t1, t2, id])
                        print("express added")
                        cur.execute(open_box, [id])
                        print("cabinet open")
                        # 存放完毕后直接提醒用户
                        get_client_tele = "select receiver_telephone from home.express where id = %s"
                        cur.execute(get_client_tele, [id])
                        receiver_tele = cur.fetchone()
                        goal = receiver_tele[0]
                        get_pickupcode = "select pickupcode from home.machine where id = %s"
                        cur.execute(get_pickupcode, [id])
                        pickupcode_line = cur.fetchone()
                        pickupcode = pickupcode_line[0]
                        print("System has send a pickupcode '", pickupcode,"' to", goal)
                        cur.close()
                        conn.commit()
                        conn.close()
                        self.turn_put_last_win()
                    else:
                        self.Turn_dialog()
            except:
                print("Express enter error")
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))


# put_window3界面
class courier_put_three_win(QMainWindow, Ui_put_win_three):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.Output_id()

    def close_box(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        global id
        find_id = "update home.machine set open_close='close' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(find_id, [id])
        except:
            print("Check failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()

    def Output_id(self):
        global id
        self.id_lab.setText(format(id))

    WindowList = []

    def turn_put_win4(self):
        self.close_box()
        the_window = courier_put_four_win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# put_window4界面
class courier_put_four_win(QMainWindow, Ui_put_win_four):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.mt = QTimer(self)
        self.m_sub()

    WinList = []

    def return_mainwindow(self):
        global num
        num = -100
        the_window = FirstMainWindow()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def m_sub(self):
        global num
        num -= 1
        print('num = {}'.format(num))
        if num > 0:
            self.time_le.setText(format(num))
            self.The_world()
        elif num < -100:
            num = 120
        else:
            self.return_mainwindow()
            num = 120


    def reinput_user(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        cur = conn.cursor()
        get_sender_address = "select company from home.courier where find_in_set(%s, telephone) > 0"
        global n1,t1
        cur.execute(get_sender_address, [t1])
        c1_line = cur.fetchone()
        c1 = c1_line[0]
        input_sender = "insert into home.sender (telephone,name,address) values(%s,%s,%s)"
        cur.execute(input_sender, [t1, n1, c1])
        print("sender added")
        cur.close()
        conn.commit()
        conn.close()

    WindowList = []

    def return_put_win1(self):
        global num
        num = -100
        self.reinput_user()
        the_window = courier_put_one_win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    WindowtheList = []

    def reopen_box(self):
        global num
        num = -100
        global id
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        find_id = "update home.machine set open_close='open' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(find_id, [id])
        except:
            print("Check failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()
        the_window = courier_put_three_win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def The_world(self):
        self.mt.singleShot(1000, self.m_sub)


# User_input界面 注册界面
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


class registered_window(QMainWindow, Ui_registered_win):
    #    register_account_pwd_signal = pyqtSignal(str, str, str, str, str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)

    WinList = []

    def return_send_FirstWin(self):
        the_window = send_FirstWin()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def return_send1(self):
        self.return_send_FirstWin()

    def registered(self):
        print("registered")
        telephone = self.telephone_le.text()
        name = self.name_le.text()
        address = self.address_le.text()
        balance = self.balance_le.text()
        password = self.password_le.text()
        print(telephone, name, address, balance, password)
        intodb(telephone, name, address, balance, password)
        #        self.register_account_pwd_signal.emit(telephone, name, address, balance, password)
        self.return_send_FirstWin()


# collect_window1界面:选择箱子
class courier_collect_one_win(QMainWindow, Ui_collect_win_one):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.box_number_be_sent()

    def detemain_box_number(self):
        global big_num ,med_num,small_num
        print(big_num,med_num,small_num)
        if big_num>0:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
        if med_num>0:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
        if small_num>0:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)

    WinList = []

    def turn_collect_win2(self):
        the_window = courier_collect_two_win()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def box_number_be_sent(self):
        global big_num
        global med_num
        global small_num
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        s = "Small"
        m = "Medium"
        l = "Large"
        find_pending = "select count(*) from home.machine where attribution='pending' and size=%s"
        cur = conn.cursor()
        try:
            cur.execute(find_pending, [l])
            l_count_line = cur.fetchone()
            big_num = l_count_line[0]
            cur.execute(find_pending, [m])
            m_count_line = cur.fetchone()
            med_num = m_count_line[0]
            cur.execute(find_pending, [s])
            s_count_line = cur.fetchone()
            small_num = s_count_line[0]
            self.big_box_lab.setText(format(big_num))
            self.med_box_lab.setText(format(med_num))
            self.small_box_lab.setText(format(small_num))
            self.detemain_box_number()
        except:
            print("Check failed")
        finally:
            cur.close()
            conn.commit()
            conn.close()

    def collect_big(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            s = "Small"
            m = "Medium"
            l = "Large"
            find_pending = "select id from home.machine where size = %s and find_in_set('pending', attribution) > 0 order by id limit 1"
            open_cabinet = "update home.machine set open_close='open' where id = %s"

            cur = conn.cursor()
            cur.execute(find_pending, [l])
            id_line = cur.fetchone()
            global id
            id = id_line[0]
            print(id)

            cur.execute(open_cabinet, [id])
            print("cabinet open")
            #金额
            global value
            value = 20

            cur.close()
            conn.commit()
            conn.close()
            self.turn_collect_win2()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def collect_med(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            s = "Small"
            m = "Medium"
            l = "Large"
            find_pending = "select id from home.machine where size = %s and find_in_set('pending', attribution) > 0 order by id limit 1"
            open_cabinet = "update home.machine set open_close='open' where id = %s"
            cur = conn.cursor()
            cur.execute(find_pending, [m])
            id_line = cur.fetchone()
            global id
            id = id_line[0]
            print(id)

            cur.execute(open_cabinet, [id])
            print("cabinet open")

            # 金额
            global value
            value = 15

            cur.close()
            conn.commit()
            conn.close()
            self.turn_collect_win2()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def collect_small(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            s = "Small"
            m = "Medium"
            l = "Large"
            find_pending = "select id from home.machine where size = %s and find_in_set('pending', attribution) > 0 order by id limit 1"
            open_cabinet = "update home.machine set open_close='open' where id = %s"

            cur = conn.cursor()
            cur.execute(find_pending, [s])
            id_line = cur.fetchone()
            global id
            id = id_line[0]
            print(id)

            cur.execute(open_cabinet, [id])
            print("cabinet open")

            # 金额
            global value
            value = 10

            cur.close()
            conn.commit()
            conn.close()
            self.turn_collect_win2()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    Win_List = []

    def turn_courier_win2(self):
        the_window = courier_two_win()
        self.Win_List.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# collect_window2界面:
class courier_collect_two_win(QMainWindow, Ui_collect_win_two):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.Output_id()
        self.output_information()

    def output_information(self):
        global id
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            # find telephone
            find_sender = "select sender_telephone from home.express where id = %s"
            find_receiver = "select receiver_telephone from home.express where id = %s"
            cur = conn.cursor()
            cur.execute(find_sender, [id])
            sender_tele = cur.fetchone()
            t1 = sender_tele[0]
            cur.execute(find_receiver, [id])
            receiver_tele = cur.fetchone()
            t2 = receiver_tele[0]

            try:
                # delete line in two side tables
                find_sender_name = "select name from home.sender where telephone = %s order by time"
                find_sender_address = "select address from home.sender where telephone = %s order by time"
                find_receiver_name = "select name from home.receiver where telephone = %s order by time"
                find_receiver_address = "select address from home.receiver where telephone = %s order by time"
                cur.execute(find_sender_name, [t1])
                sender_name = cur.fetchone()
                n1 = sender_name[0]
                print("sender name found")
                cur.execute(find_sender_address, [t1])
                sender_address = cur.fetchone()
                a1 = sender_address[0]
                print("sender address found")

                cur.execute(find_receiver_name, [t2])
                receiver_name = cur.fetchone()
                n2 = receiver_name[0]
                print("receiver name found")
                cur.execute(find_receiver_address, [t2])
                receiver_address = cur.fetchone()
                a2 = receiver_address[0]
                print("receiver address found")

                cur.close()
                conn.commit()
                conn.close()
            except:
                print("Express find error")
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
        self.send_address_lab.setText(format(a1))
        self.send_name_lab.setText(format(n1))
        self.send_telephone_lab.setText(format(t1))
        self.rec_address_lab.setText(format(a2))
        self.rec_name_lab.setText(format(n2))
        self.rec_telephone_lab.setText(format(t2))

    def Output_id(self):
        global id
        self.id_label.setText(format(id))

    def close_box(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        global id
        find_id = "update home.machine set open_close='close' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(find_id, [id])
        except:
            print("Check failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()

    WinList = []

    def turn_collect_win3(self):
        self.close_box()
        the_window = courier_collect_three_win()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


# collect_window3界面: 倒计时
class courier_collect_three_win(QMainWindow, Ui_collect_win_three):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类
        self.setupUi(self)
        self.mt = QTimer(self)
        self.m_sub()

    WinList = []

    def turn_collect_win1(self):
        global num
        num = -100
        self.money()
        self.clear_box_data()
        self.clear_express()
        the_window = courier_collect_one_win()
        self.WinList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def money(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            cur = conn.cursor()
            global t1
            print(t1)
            pay_money = "update home.courier set balance = balance + %s where telephone = %s"
            global value
            cur.execute(pay_money, [value, t1])
            cur.close()
            conn.commit()
            conn.close()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def clear_express(self):
        try:
            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='home',
            )
            # find telephone
            find_sender = "select sender_telephone from home.express where id = %s"
            find_receiver = "select receiver_telephone from home.express where id = %s"
            cur = conn.cursor()
            global id
            cur.execute(find_sender, [id])
            sender_tele = cur.fetchone()
            t1 = sender_tele[0]
            cur.execute(find_receiver, [id])
            receiver_tele = cur.fetchone()
            t2 = receiver_tele[0]
            # delete line in two side tables
            delete_sender = "delete from home.sender where telephone = %s order by time"
            delete_receiver = "delete from home.receiver where telephone = %s order by time"
            delete_express = "delete from home.express where id = %s"
            cur.execute(delete_sender, [t1])
            print("sender deleted")
            cur.execute(delete_receiver, [t2])
            print("receiver deleted")
            cur.execute(delete_express, [id])
            print("express deleted")
            cur.close()
            conn.commit()
            conn.close()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def clear_box_data(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        find_id = "update home.machine set attribution='empty' , pickupcode='0' where id = %s"
        cur = conn.cursor()
        try:
            global id
            cur.execute(find_id, [id])
        except:
            print("Empty failed")
        finally:
            cur.close()
            conn.commit()
            conn.close()

    WindowList = []

    def return_mainwindow(self):
        global num
        num = -100
        self.money()
        self.clear_box_data()
        self.clear_express()
        the_window = FirstMainWindow()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def m_sub(self):
        global num
        num -= 1
        print('num = {}'.format(num))
        if num > 0:
            self.time_le.setText(format(num))
            self.The_world()
        elif num < -100:
            num = 120
        else:
            self.return_mainwindow()
            num = 120

    WindowtheList = []

    def reopen_box(self):
        global num
        num = -100
        global id
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        find_id = "update home.machine set open_close='open' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(find_id, [id])
        except:
            print("Check failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()
        the_window = courier_collect_two_win()
        self.WindowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()

    def The_world(self):
        self.mt.singleShot(1000, self.m_sub)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = FirstMainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())
