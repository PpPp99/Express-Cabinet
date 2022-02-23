#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/11/1

# 客户开辟使用新cabinet寄件

import random
import sys
import MySQLdb


def v_code():
    ret = ""
    for i in range(6):
        num = random.randint(0, 9)
        Letter = chr(random.randint(65, 90))
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
    attribution_change = "update home.machine set attribution='pending' where size = %s and attribution='empty' order by id limit 1 "
    pickupcode_add = "update home.machine set pickupcode = %s where pickupcode = '0' and size = %s and attribution='pending' order by id limit 1 "
    cur = conn.cursor()
    cur.execute(attribution_change, [l])
    print("attribution changed")
    cur.execute(pickupcode_add, [password, l])
    print("pickupcode added")

    #交易金额
    deduct_money = "update home.client set balance = balance + %i where telephone = %s"
    cur.execute(deduct_money, [20,telephone])
    print("attribution changed")

    cur.close()
    conn.commit()
    conn.close()
except MySQLdb.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)
