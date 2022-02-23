#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/11/1

#清空id对应的cabinet信息

import sys
import MySQLdb

id = '32'

conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='home',
    )
find_id = "update home.machine set attribution='empty' , pickupcode='0' where id = %s"
cur = conn.cursor()
try:
    cur.execute(find_id, [id])
except:
    print("Empty failed")
    sys.exit(1)
finally:
    cur.close()
    conn.commit()
    conn.close()