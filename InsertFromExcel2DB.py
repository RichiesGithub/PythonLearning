#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

import xlrd
import MySQLdb
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")

#打开excel
def openExcel():
    try:
        book = xlrd.open_workbook("C:\\test.xls")
    except Exception,e:
        print("open failed!")
        print e
    try:
        sheet = book.sheet_by_name("test")
        return sheet
    except Exception,e:
        print("loading sheet failed!")
        print e

def insertData2DB():
    db = MySQLdb.Connect("localhost", "root", "lq910816", "PythonDB", charset='utf8')
    cursor = db.cursor()
    source = openExcel()
    rnum= source.nrows
    DBlist=[]
    for i in range(0,rnum):
        rowdata = source.row_values(i)
        DBvalue = (rowdata[0],rowdata[1],rowdata[2],rowdata[3],rowdata[4])
        DBlist.append(DBvalue)
    try:
        sql = 'INSERT INTO EMPLOYEE VALUES (%s,%s,%s,%s,%s)'
        cursor.executemany(sql,DBlist)
        db.commit()
    except Exception,e:
        print e
        db.rollback()
    db.close()

if __name__ == '__main__':
    start = time.clock()
    insertData2DB()
    end = time.clock()
    print 'time useage:',end-start