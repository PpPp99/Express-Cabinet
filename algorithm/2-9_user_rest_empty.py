#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/10/22

#返回寄存柜内剩余空柜子的数量

import sys
import MySQLdb

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
find_empty = "select count(*) from home.machine where attribution='empty' and size=%s"
cur = conn.cursor()
try:
    cur.execute(find_empty, [s])
    count_line = cur.fetchone()
    count = count_line[0]
    if count > 0:
        print(count)
    else:
        print('0')
except:
    print("Check failed")
    sys.exit(1)
finally:
    cur.close()
    conn.commit()
    conn.close()