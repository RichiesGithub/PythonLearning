#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import math
def ChangeInt(a):
    a = 10
    print a
a=8
ChangeInt(a)
print a


def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print "函数内 : ", total
    print locals()
    print globals()
    return;


# 调用sum函数
total = sum(10, 20);

Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    global Money

    Money = Money + 1


print Money
AddMoney()
print Money

print dir(math)
print globals()