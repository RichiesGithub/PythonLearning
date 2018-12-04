#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import time
import calendar
start = time.clock()
time1 = time.time()
print time.localtime()
print time1
#从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。

localtime = time.localtime(time.time())
print '本地时间为：',localtime
#你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
localtime = time.asctime(time.localtime(time.time()))
print localtime
#格式化时间我们可以使用 time 模块的 strftime 方法来格式化日期，：
#将时间转化为yyyy-mm-dd hh:mm:ss

print time.strftime('%Y-%m-%d %H:%M:%S %a %A %b %B')

end = time.clock()
print end - start
print time.gmtime()
print time.localtime()

print time.timezone/3600
print str(time.tzname)

print calendar.calendar(2018,w=1,l=1,c=1,m=12)
print calendar.firstweekday()
#判断是否为闰年
print calendar.isleap(2018)
print calendar.leapdays(2008,2018)
print calendar.month(2018,10,w=1,l=1)
print calendar.monthcalendar(2018,9)
print calendar.monthrange(2018,8)
calendar.prcal(2018,w=2,l=1,c=6)#等同于calendar.calendar
calendar.prmonth(2018,9,w=2,l=1)
print calendar.weekday(2018,10,01)

