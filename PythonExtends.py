#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

#在python中继承中的一些特点：
# 1、如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。
#eg:
class Father(object):
    def __init__(self,name):
        self.name = name
        print 'Name:',name
    def getName(self):
        return 'Father:'+self.name
class Son(Father):
    def getName(self):
        return 'Son: '+self.name

#如果重写了__init__ 时，实例化子类，就不会调用父类已经定义的 __init__，语法格式如下：
class Son2(Father):
    def __init__(self,name):
        print 'Son2小儿子:' + name
        self.name = name
    def getName(self):
        return 'Son2:'+self.name
#如果重写了__init__ 时，要继承父类的构造方法，可以使用 super 关键字：
class Son3(Father):
    def __init__(self,name):
        super(Son3,self).__init__(name)
        print 'hi'
        self.name = name
    def getName(self):
        return 'Son3:'+self.name
#还有一种经典写法
class Son4(Father):
    def __init__(self,name):
        Father.__init__(self,name)
        print 'hi'
        self.name = name
    def getName(self):
        return 'Son4:'+self.name

if __name__ == '__main__':
    son = Son('Dan')
    print son.getName()
    son2 = Son2('Dan2')
    print son2.getName()
    son3 = Son3('Dan3')
    print son3.getName()
    son4 = Son3('Dan3')
    print son4.getName()
print issubclass(Son3,Father)

# 2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
# 3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。

