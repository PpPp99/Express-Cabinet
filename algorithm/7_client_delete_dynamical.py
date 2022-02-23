#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/11/1

#删除express、sender和receiver的动态数据

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
    #find telephone
    find_sender = "select sender_telephone from home.express where id = %s"
    find_receiver = "select receiver_telephone from home.express where id = %s"
    cur = conn.cursor()
    cur.execute(find_sender,[id])
    sender_tele = cur.fetchone()
    t1 = sender_tele[0]
    cur.execute(find_receiver,[id])
    receiver_tele = cur.fetchone()
    t2 = receiver_tele[0]

    try:
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
    except:
        print("Express delete error")
except MySQLdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

