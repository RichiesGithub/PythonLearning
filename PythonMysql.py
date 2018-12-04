#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "lq910816", "PythonDB", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor()
#创建表EMPLOYEE
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# #关闭数据库连接

sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchmany(3)
   print results
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"
db.close()

