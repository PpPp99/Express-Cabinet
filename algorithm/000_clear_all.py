#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/11/11
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

    clear_machine = "update home.machine set attribution='empty' , pickupcode='0', open_close='close' where id >= 1 and id <= 40"
    clear_client = "delete from home.client"
    clear_courier = "delete from home.courier"
    clear_sender = "delete from home.sender"
    clear_receiver = "delete from home.receiver"
    clear_express = "delete from home.express"
    reset_change = "update home.client set balance=200 where balance > 0"

    cur = conn.cursor()
    cur.execute(clear_machine)
#    cur.execute(clear_client)
#    cur.execute(clear_courier)
    cur.execute(clear_sender)
    cur.execute(clear_receiver)
    cur.execute(clear_express)
    cur.execute(reset_change)
    cur.close()
    conn.commit()
    conn.close()
    print("clear all")
except MySQLdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

