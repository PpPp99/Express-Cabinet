#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/11/1

#快递员清空id对应的cabinet信息

import sys
import MySQLdb

#size=""

conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='home',
        )
        find_pending = "select id from home.machine where find_in_set(pending, attribution) > 0 order by id limit 1"
        open_cabinet = "update home.machine set open_close='open' where id = %s"
        receive_money = "update home.client set balance = balance + %i where telephone = %s"
        clear_pending = "update home.machine set attribution='empty' and pickupcode='0' where id = %s"
        cur = conn.cursor()
        try:
            cur.execute(find_pending)
            id_line = cur.fetchone()
            id = id_line[0]
            print(id)
            cur.execute(open_cabinet, [id])

            # 等待120s,开始清空

            cur.execute(clear_pending, [id])
            print("cabinet has been clear")

            #收钱
            global t1
            cur.execute(receive_money, [20, t1])
            print("attribution changed")
        except:
            print("Empty failed")
            sys.exit(1)
        finally:
            cur.close()
            conn.commit()
            conn.close()