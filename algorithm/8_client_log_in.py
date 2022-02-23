#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/10/22

#寄件用户登录系统

import MySQLdb
import sys

telephone = "17765994676"
code = "123456"

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
    cur.execute(log_in, [telephone,code])
    name = cur.fetchone()
    if name[0] != 0:
        print("Hello! %s"%name)
except:
    print("Your telephone or code is wrong")
    print("Please try again!")
    sys.exit(1)
finally:
    cur.close()
    conn.commit()
    conn.close()