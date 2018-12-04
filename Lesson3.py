#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

import random

# Python 条件语句
#简单的条件判断语句组
var = 100
if (var == 100):print 'Successfully'

a = [1,2,3]
b = a if len(a) != 0 else ""
print(b)

i=1
while i<10:
    i+=1;
    if i%2==0:
        continue
    print i
i=1
while 1:
    print i
    i+=1
    if i>10:
        break
'''
var = 1
while var==1:
    num = raw_input("name:")
    print 'you enter'+num
'''
#循环使用else，判断语句为fause时候执行else
var = 1
while var<5:
    var+=1
    print var
else:
    print 'more than 5'
#石头剪刀布


while 1:
    cump = int(random.randint(1, 3))
    if cump == 1:
        cumphand = '石头'
    elif cump == 2:
        cumphand = '剪刀'
    elif cump == 3:
        cumphand = '布'
    print cumphand
    manhand = raw_input('Please enter your choose:')
    handlist=['石头','剪刀','布','end']
    if manhand not in handlist:
        print 'wrong input'
    elif manhand == handlist[3]:
        print '退出......'
        break
    elif manhand == cumphand:
        print '平手，请继续'
       # continue
    elif (manhand==handlist[0] and cump == 2) or (manhand ==handlist[1] and cump == 3) or (manhand == handlist[2] and cump == 1):
        print '电脑：'+cumphand
        print '玩家：'+manhand
        print 'you win !!!'
    elif (manhand==handlist[0] and cump == 3) or (manhand ==handlist[1] and cump == 1) or (manhand == handlist[2] and cump == 2):
        print '电脑：'+cumphand
        print '玩家：'+manhand
        print 'you lose!'

#九九乘法表
i = 1
while i:
    j = 1
    while j:
        print j, "*", i, " = ", i * j, '  ',
        if i == j:
            break

        j += 1
        if j >= 10:
            break

    print "\n"
    i += 1
    if i >= 10:
        break

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果 :', fruits[index]

print "Good bye!"

# for... else ： else 会在for循环正常结束后执行， 正常结束是指for循环不是因break终端而结束。
#eg：判断质数

num = int(raw_input("Please enter a number:"))
for i in range(2,num):
    if num % i == 0:
        j = num/i
        print "%d不是一个质数，可以分解为%d * %d" %(num,i,j)
    break
else:
    print "%d 是一个质数"%(num)

#使用内置的enumerate进行遍历
'''for index, item in enumerate(sequence):
    process(index, item)'''
str = "Richie"
for i,j in enumerate(str):
    print i,j

#*字塔
i=1
#j=1
while i<=9:
   if i<=5:
      print ("*"*i)

   elif i<=9 :
      j=i-2*(i-5)
      print("*"*j)
   i+=1
else :
   print("")
'''
numList = [13,23,25,66,73,98,89,16]
Len = len(numList)
for i in range(Len):
    for j in range(Len-i):
        if numList[i]<'''
'''
array = [9,2,7,4,5,6,3,8,1,10]
L = len(array)
for i in range(L):
    for j in range(L-i):
        if array[L-j-1]<array[L-j-2]:
            array[L-j-1],array[L-j-2]=array[L-j-2],array[L-j-1]
for i in range(L):
    print array[i]
    '''








































