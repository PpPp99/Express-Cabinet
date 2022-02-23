#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/11/12

import sys
import MySQLdb

n = 'Yui'

conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='home',
    )
cur = conn.cursor()
find = "select telephone from home.client where name = %s"
pay_money = "update home.client set balance = balance - %s where telephone = %s"
#   global value
cur.execute(find,[n])
t_line = cur.fetchone()
t = t_line[0]
print(t)
value = 10
int_value = int(value)
cur.execute(pay_money, [value, t])

cur.close()
conn.commit()
conn.close()
