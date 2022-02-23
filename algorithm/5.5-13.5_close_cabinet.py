#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Gao Renjie time:2019/11/5

#指令关闭cabinet

import sys
import MySQLdb

#id = ""

conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='home',
    )

find_id = "update home.machine set open_close='close' where id = %s"
cur = conn.cursor()
try:
    cur.execute(find_id, [id])
except:
    print("Check failed")
    sys.exit(1)
finally:
    cur.close()
    conn.commit()
    conn.close()