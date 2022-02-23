#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/10/1
# coding=utf-8

#快递员寄件时开辟cabinet并附加取件码

import random
import sys
import MySQLdb

def v_code():
    ret = ""
    for i in range(6):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))#ASCII表示数字
        Letter = chr(random.randint(65, 90))  # 取大写字母
        s = str(random.choice([num, Letter]))
        ret += s
    return ret

password = v_code()
print("password: %s" % password)
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
    attribution_change = "update home.machine set attribution='to_be_taken' where size = %s and attribution='empty' order by id limit 1 "
    pickupcode_add = "update home.machine set pickupcode = %s, open_close = 'open' where pickupcode = '0' and size = %s and attribution='to_be_taken' order by id limit 1 "
    cur = conn.cursor()
    cur.execute(attribution_change, [l])
    print("attribution changed")
    cur.execute(pickupcode_add, [password,l])
    print("pickupcode added")

    cur.close()
    conn.commit()
    conn.close()
except MySQLdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)