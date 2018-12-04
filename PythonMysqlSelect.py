#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

import MySQLdb
#插入多条数据
db = MySQLdb.Connect("localhost", "root", "lq910816", "PythonDB", charset='utf8')
cursor = db.cursor()
sql  = 'SELECT COUNT(*) FROM EMPLOYEE'
cursor.execute(sql)
print cursor.fetchone()
db.close()
