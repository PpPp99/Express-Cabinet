#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/10/23

#用户接收/快递员接收后关闭cabinet，系统后续处理删除快递单

import sys
import MySQLdb

#接受id
id = ""
#if  # 收到关门指令:
    try:
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        find_sender= "select sender_telephone from home.express where id=%s"
        find_receiver= "select receiver_telephone from home.express where id=%s"

        cur = conn.cursor()
        cur.execute(find_sender,[id])
        sender_telephone_line = cur.fetchone()
        sender_telephone = sender_telephone_line[0]
        cur.execute(find_receiver, [id])
        receiver_telephone_line = cur.fetchone()
        receiver_telephone = receiver_telephone_line[0]

        delete_sender = "delete from home.sender where telephone=%s order by create_time"
        delete_receiver = "delete from home.receiver where telephone=%s order by create_time"
        delete_express = "delete from home.express where id=%s"
        cur.execute(delete_sender, [sender_telephone])
        cur.execute(delete_receiver, [receiver_telephone])
        cur.execute(delete_express, [id])

        #120s count finished

        clear_machine = "update home.machine set attribution='empty' and pickupcode='0' where id = %s"
        cur.execute(clear_machine, [id])
        print("cabinet reset")
    except MySQLdb.Error as e:
        print("Delete failed%d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)