#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import time
import calendar
import os

fo = open("foo.txt", "w+")
# fo1 = open('fo1.txt','a')
# print '对象ID 是：',id(fo)
# print "文件名: ", fo.name
# print "是否已关闭 : ", fo.closed
# print "访问模式 : ", fo.mode
# print "末尾是否强制加空格 : ", fo.softspace
fo.write('www.baidu.com,www,google.com,www.hp.com,www.csdn.com,www.ibm.com')
fo.flush()
# fo.seek(-11,1)
print fo.read()
print fo.tell()
fo.close()
# fo1.close()
#rename and remove
# os.rename('fo1.txt','fo2.txt')
# time.sleep(5)
# os.remove('fo2.txt')
#在当前目录下创建目录
# os.mkdir('test')
# os.chdir('/Lessons')
#删除一个目录
#os.rmdir('xxx')
#获取当前目录
print os.getcwd()
print os.path.dirname(__file__)
print os.path.abspath(os.path.dirname(__file__))

#获取上级目录
print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print os.path.abspath(os.path.dirname(os.getcwd()))
print os.path.abspath(os.path.join(os.getcwd(), ".."))
#获取上上级目录
print os.path.abspath(os.path.join(os.getcwd(), "../.."))
print os.path.abspath(os.path.join('C:\Users\qli25\PycharmProjects','..'))












# foo = open('foo.txt','w+')
# print '对象ID 是：',id(foo)
# print foo.softspace
# foo.write('www.baidu.com www.google.com\nwww.sina.com\n')
# str = foo.read().decode('utf-8')
# print str

try:
    fh = open("testfile")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()

try:
    fh = open("testfile")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print "关闭文件"
        fh.close()
except IOError:
    print "Error: 没有找到文件或读取文件失败"

def try_exception(num):
    try:
        int(num)
    except ValueError,arg:
        print arg,"is not a number"
    else:
        print "this is a number inputs"

try_exception(2)

