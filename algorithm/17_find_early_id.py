#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/11/13
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
find_id = "select id from home.machine where size = %s and attribution='to_be_taken' order by UpdateTime desc limit 1"
cur = conn.cursor()
try:
    cur.execute(find_id, [m])
    id_line = cur.fetchone()
    id = id_line[0]
    print(id)
    cur.close()
    conn.commit()
    conn.close()
except:
    print("find failed")
    sys.exit(1)