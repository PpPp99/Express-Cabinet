#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/10/21

#输入验证码匹配柜子，正确后返回id

import sys
import MySQLdb

input_pickupcode = "123123"

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
    cur.execute(get_pickupcode, [input_pickupcode])
    id_line = cur.fetchone()
    id = id_line[0]
    print(id)
    if id > 0:
        print("pickup！code！ Best Match!")
    cur.execute(open_cabinet, [id])
    print("cabinet is open")
except:
    print("Match failed")
    sys.exit(1)
finally:
    cur.close()
    conn.commit()
    conn.close()
