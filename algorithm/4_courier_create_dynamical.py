#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/10/

#由寄件快递员创建express，sender，receiver数据库的新快递单

import sys
import MySQLdb

try:
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='home',
    )
    t1 = ""
    input_code = ""

    get_sender_name = "select name from home.courier where find_in_set(%s, telephone) > 0 and find_in_set(%s, code)> 0"
    get_sender_address = "select company from home.courier where find_in_set(%s, telephone) > 0 and find_in_set(%s, code)> 0"
    cur = conn.cursor()
    cur.execute(get_sender_name,[t1,input_code])
    n1_line = cur.fetchone()
    n1 = n1_line[0]
    cur.execute(get_sender_address,[t1,input_code])
    c1_line = cur.fetchone()
    c1 = c1_line[0]
    try:
        if n1 != 0:
            print("Thank you for your hard work! %s" % name)
            t2 = ""#输入寄给谁
            n2 = ""
            a2 = ""
#打开指定箱子
            id = ""#放入物品，返回坐标

            input_sender = "insert into home.sender (telephone,name,address) values(%s,%s,%s)"
            input_receiver = "insert into home.receiver (telephone,name,address) values(%s,%s,%s)"
            input_express = "insert into home.express (sender_telephone,receiver_telephone,id) values(%s,%s,%s)"

            cur.execute(input_sender, [t1, n1, c1])
            print("sender added")
            cur.execute(input_receiver, [t2, n2, a2])
            print("receiver added")
            cur.execute(input_express, [t1, t2, id])
            print("express added")

            #存放完毕后直接提醒用户
            get_client_tele = "select receiver_telephone from home.express where id = %s"
            cur = conn.cursor()
            cur.execute(get_client_tele, [id])
            receiver_tele = cur.fetchone()
            goal = receiver_tele[0]
            print("System has send a message to", goal)
            cur.close()
            conn.commit()
            conn.close()
    except:
        print("Express enter error")
        sys.exit(1)#需要循环结构
except MySQLdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

