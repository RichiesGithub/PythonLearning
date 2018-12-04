#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import xlwt
import random
import string
#自动生成10000条数据并插入到Excel
workbook  = xlwt.Workbook()
Sheet1  = workbook.add_sheet('test',cell_overwrite_ok=True)
#自动生成数据， 数据库格式：(fNAME,lNAME,AGE,SEX,INCOME)

list=[]#生成dataInsert的list
dataInsert = []
num=0
while num<=10000:
    #在26个字母中随机生成三位字母的组合
    Fname = string.join(random.sample(string.lowercase, 3)).replace(" ","")
    # 在26个字母中随机生成三位字母的组合
    Lname = string.join(random.sample(string.lowercase, 3)).replace(" ","")
    age = random.randint(28,40)
    #在F与M中随机选择
    sex = random.choice('FM')
    income = random.randint(1000,6001)
    list = [Fname,Lname,age,sex,income]
    num+=1
    dataInsert.append(list)
for rnum,rvalues in enumerate(dataInsert):
    for cnum,value in enumerate(rvalues):
        Sheet1.write(rnum,cnum,value)
    workbook.save('C:\\test.xls')






