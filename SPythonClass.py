#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

class Pri:
    def prt(self):
        print self
        print self.__class__
T = Pri()
T.prt()

#Python对象的销毁， 垃圾回收

class Point:
    def __init__(self,x=0,y=1):
        self.x = x
        self.y = x
    def  __del__(self):
        className = self.__class__.__name__
        print
#Python同样支持运算符重载，实例如下：
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1+v2

L1 = (2,10)
L2 = (5,-2)
print L1+L2

class A:
   def foo(self):
      print('called A.foo()')
class B(A):
   pass
class C(A):
   def foo(self):
      print('called C.foo()')
class D(B, C):
   pass

if __name__ == '__main__':
   d = D()
   d.foo()


shoplist = ['apple','mango','carrot','banana']
mylist = shoplist # 简单的赋值 只是引用变量名
#普通引用只是名称的绑定，而只有完整切片才是真正意义上的复制。所以我们在简单引用后一定要考虑是否可以更改，因为操作可能影响到源对象。
del shoplist[0]
del mylist[0]

print 'shoplist 列表：',shoplist
print 'mylist 列表：',mylist

