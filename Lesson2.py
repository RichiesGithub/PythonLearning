#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import json
import copy
#python 变量
'''python 有五种标准数据类型， Numbers，String，List,Tuple,Dictionary
'''
#----------------------------------------------------------------------------
# Number
'''
Python支持四种不同的数字类型：

int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）
'''
#复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。

#----------------------------------------------------------------------------
#String
s ='Richie'
print s[1:4]

# *是重复操作
print s[1:4]*2*3
#------------------------------------------------------------------------------
#List
List=[1,2,3,'Richie']
List2=[0,9,8,'Ann']
# +是合并操作
print List+List2
print List * 2
#-----------------------------------------------------------------------------
#tuple(元组)
#元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。（指的是元祖中的值不可以改变， 但可以最元组进行操作）
tuple = (1,2,3,4,'Richie')
tuple2 = (0,9,8,7,'Ann')
print tuple*2
print tuple[2]
#----------------------------------------------------------------------------
# Dictionary
#dictionary 相当于JAVA中的MAP ， 通过键值对来存取数据，dictionary是无序集合
dict = {}
dict['one'] = "Richie"
dict[2] = "Ann"
print dict
print dict.keys()
print dict.values()
#print dict *2 不可用
#print dict + dict 不可用+合并
#dict 创建方法
y={}#创建空dict
print y
'''

??????????????????????????????
#1.传入关键字
y(a=1,b=2,c=3)
print y
#映射函数创建dict
'''
#zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
#如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
'''
dict1={}
print dict1(zip(['a','b','c'],[1,2,3]))
'''

y="Richie"
print list(y)

#eval 执行一个字符串表达式 eg：
x=3
print eval('3*x')
h='danchaofan'
print set(h)
i='qwerty'
print frozenset(i)

#python 逻辑运算符
x,y = 10,20
print x and y#如果 x 为 False，x and y 返回 x，否则它返回 y 的计算值。
print x or y#如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。
print not(x)#如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。

x=0
print x and y#???????????????????
print x or y
print not(x)
x=-1
print x and y
print x or y
print not(x)

#Python 成员运算符
L1= 'Richie'
print 'i' in L1
L2 = ['Ann','Richie']
print L1 in L2
L3=['Ann','Richie','DAN',['Ann','Richie']]
print L2 in L3


a = 20
b = 20

if (a is b):
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if (a is not b):
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"
#python 为了节省内存， 在定义变量时候， 在脚本中， 如果值相同，那么久指定为同意地址， 在控制台输出的话， 定义在同一行中， 默认对象地址相同， 如果不同行中， 如果值-5<=x<=256, 那么地址相同， 否则地址不同。
a=1000
b=1000
print a is b
a=100000000000000
b=100000000000000
print a is b

a=-1
b=-1
print a is b

a='Richieqwertyuiopasdfghjklzxcvbnm'
b='Richieqwertyuiopasdfghjklzxcvbnm'
print a is b

#格式化函数
print "My name is %s and weight is %d kg!" % ('Zara', 21)
#python 2.6 后， 增加了str.formate()方法来格式化字符串
print '{}{}'.format('Hello','World')#按顺序输出
print '{1}{0}'.format('Hello','World')#按指定位置输出
print '{1}{0}{1}'.format('Hello','World')#设置制定位置

#也可以设置参数来格式化字符串
print '网站名：{name},地址{url}'.format(name='菜鸟教程',url='www.baidu.com')
#通过字典设置字符串参数
site={'name':'菜鸟教程','link':'www.baidu.com'}
print '网站名：{name},地址：{link}'.format(**site)
#通过列表索引甚至字符串参数
List=['菜鸟教程','www.baidu.com']
print '网站名:{0[0]},link:{0[1]}'.format(List)

print("%6.3f" % 2.3)


L3=[1,2,3,4,5,2,3,123,5,6,2,4,6,7,3,6,7,]
aList = [123, 'xyz', 'zara', 'abc', 123];
print L3.count(3)
L3.extend(aList[:3])
print L3
print L3.index(3)


list_2d = [ [1for i in range(5)] for i in range(5)]
print list_2d

ListChinese=["你","我","他"]
print ListChinese#不能正常显示汉字
#解决方案 1

print str(ListChinese).decode("string_escape")

#解决方案2  用Json
print json.dumps(ListChinese,encoding='UTF-8',ensure_ascii=False)


dict={1:2,2:3,3:4}
print dict
dict = {'Name': 'Zara', 'Age': 7};
print dict
print '这是一个字典：%s'%str(dict)

#copy and deepcopy
#引用属于浅拷贝，D1,D2之相同一对象
D1={'num1':1,'num2':2,'num3':[4,5,6]}
D2=D1
print D2,D1
D1['num1']=100
print D1,D2

#浅拷贝copy只作用于dict的二级目录，一级目录指向不同的对象， 二级目录指向相同的对象。
D3={'num1':1,'num2':2,'num3':[4,5,6]}
D4=D3.copy()
D3['num1']=100
D3['num3'][0]=200
print 'D3=%s'%str(D3)
print 'D4=%s'%str(D4)
D3['num3']=300
print 'D3=%s'%str(D3)
print 'D4=%s'%str(D4)

#深拷贝， 对象完全独立
D5={'num1':1,'num2':2,'num3':[4,5,6]}
D6=copy.deepcopy(D5)
D5['num1']=100
D5['num3'][0]=200
print 'D5=%s'%str(D5)
print 'D6=%s'%str(D6)

#字典cmp()的比较规则
#1，比较长短， 短的比长的小
D7={'Name': 'e', 'Age': 30, 'Addr':'hust'}
D8={'Name': 'e', 'Age': 30}
print cmp(D7,D8)
#长度相同，比较不同的最小Key值
D7={'Name': 'e', 'Age': 30, 'Addr':'hust'}
D8={'Name': 'e', 'Age': 30, 'Adds':'hust'}
print cmp(D7,D8)
#Key值都相同，比较Value不等的Key中的最小value
D7={'Name': 'a', 'Age': 22, 'Addr':'hust'}
D8={'Name': 'e', 'Age': 30, 'Addr':'husts'}
print cmp(D7,D8)

print type(D8)

#Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
L={}
L1 = ('Richie', 'Ann', 'Dan')
L = L.fromkeys(L1)
L = L.fromkeys(L1,(10,20,30))
print str(L)
#Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
dict = {'Name': 'Zara', 'Age': 27}

print "Value : %s" %  dict.get('Age')
print "Value : %s" %  dict.get('Sex', "Richie")

#Pyhton dict 中setdefault()跟 get相反， 如果值不存在字典中， 将值添加到dict中。
dict = {'Name': 'Zara', 'Age': 27}
print '1.%s'%dict.setdefault('Name')
print '2.%s'%dict.setdefault('sex')
print '3.%s'%dict.setdefault('Ann','女')
print str(dict).decode("string_escape")
# print str(dict)
print json.dumps(str(dict),encoding='UTF-8',ensure_ascii=False)

print dict.has_key('Name')
#可用于遍历dict
print dict.items()
for k,v in dict.items():
    print k,v
#dict.update把字典dict2的键/值对更新到dict里
dict2 = {'Name1': 'Zara', 'Age1': 27}
dict.update(dict2)
print str(dict)
#Python 字典 pop() 方法删除字典给定键 key 及对应的值，返回值为被删除的值。key 值必须给出。 否则，返回 default 值。
dict2.pop('Name1')
print str(dict2)
dict2['name2']='Richie'
print str(dict2)
















