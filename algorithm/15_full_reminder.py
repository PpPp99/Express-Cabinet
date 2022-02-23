#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/11/12
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

find_all = "select count(*) from home.machine where size=%s"
find_rest = "select count(*) from home.machine where attribution='empty' and size=%s"
cur = conn.cursor()
try:
    cur.execute(find_all, [l])
    all_line = cur.fetchone()
    all = all_line[0]
    cur.execute(find_rest, [l])
    count_line = cur.fetchone()
    count = count_line[0]
    print(count)
    if count/all > 0.2:
        print("enough")
    else:
        find_early_id = "select id from home.machine where pickupcode <> '0' order by UpdateTime limit 1"
        find_early = "select receiver_telephone from home.express where id = %s"
        cur.execute(find_early_id)
        e_id_line = cur.fetchone()
        eid = e_id_line[0]
        cur.execute(find_early,[eid])
        tele_line = cur.fetchone()
        tele = tele_line[0]
        print("Rest space of size '", l, "' in express machine is less than 20%")
        print("Remind message has been sent to telephone number:", tele)
    cur.close()
    conn.commit()
    conn.close()
except:
    print("find failed")
    sys.exit(1)