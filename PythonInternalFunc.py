#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

# input 和 raw_input , input() 和 raw_input() 这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。而对于 input() ，
# 它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError

# print 'please enter:',input()
# print 'please enter raw:', raw_input()

#python staticmethod 返回函数的静态方法。
class C(object):
    @staticmethod
    def f():
        print 'staticmethod静态方法不需要实例化调用'
#不实例化直接调用
C.f()
#实例化调用
obje = C()
obje.f()