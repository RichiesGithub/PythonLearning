#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
from string import maketrans
import re
#Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。
str='rICHIEieieieiIEIEieIE'
print str.capitalize()
print str.center(20)
print str.upper()
print str.lower()
print str.count('ie',0,len(str))
print str.count('ie',0,12)

str2 = '123456Richie'
print str2.isalnum()

#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
str = '-'
print str.join(['1','b','c'])
#字典支队key值进行连接
seq = {'hello':'nihao','good':2,'boy':3,'doiido':4}
print str.join(seq)
#返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
print str2.ljust(20)
print str2.rjust(20)
#Python lstrip() 方法用于截掉字符串左边的空格或指定字符。
#截掉 string 左边的空格(默认)，可以指定字符串，字符串可以是一个字符，或者多个字符，匹配时不是按照整个字符串匹配的，而是一个个匹配的。
L1 = '     string'
L2 = 'string     '
print L1.lstrip()
print L2.rstrip()

L3 = '####Richie######'
print L1.lstrip('R')
print L1.lstrip('s')
print L3.lstrip('#')
print L3.lstrip('##')
print L3.lstrip('###')
print L3.lstrip('#####')
print L3.lstrip('#R')
print L3.lstrip('#i')
print L3.lstrip('l')

#Python maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
#注：两个字符串的长度必须相同，为一一对应的关系。
intab  = 'aeiou'
outtab = '12345'
translate =maketrans(intab,outtab)
str = "this is string example....wow!!!";
print str.translate(translate)
# 4.
# # 对translate方法的简单封装, 使用起来更加方便
# frm: intab
# to: outtab
# delete: 指定删除字符
# keep: 指定保留字符
# delete和keep有重叠时，delete优先
'''
def my_translator(frm = b'', to = b'', delete = b'', keep = None):

    if len(to) == 1:
        to = to * len(frm) #如果to只有一个字符,将字符的数量跟frm相等,这样才能一一对应

    #构建一个映射表
    trans = bytes.maketrans(frm, to)

    if keep is not None: #如果有保留字
        allchars = bytes.maketrans(b'', b'')  # 获取空映射表的所有字符
        keep = keep.translate(allchars, delete)  # 从keep中去除delete中包含的字符，即keep与delete有重合时，优先考虑delete
        delete = allchars.translate(allchars, keep)  # delete为从全体字符中除去keep，即不在keep的都删掉


    # 闭包
    def my_translate(s):
        return s.translate(trans, delete)

    return my_translate


# 测试my_tranlator

# 只保留数字
digits_only = my_translator(keep = b'0123456789')
print(digits_only(b'http://www.csdn.net/wirelessqa 520520'))  #b'520520'

# 删除所有数字
no_digits = my_translator(delete = b'0123456789')
print(no_digits(b'http://www.csdn.net/wirelessqa 520520'))  #b'http://www.csdn.net/wirelessqa '

# 用*替换数字
digits_to_hash = my_translator(frm = b'0123456789', to = b'*')
print(digits_to_hash(b'http://www.csdn.net/wirelessqa 520520')) #b'http://www.csdn.net/wirelessqa ******'

# delete与keep有重合时的情况
trans = my_translator(delete = b'20', keep = b'0123456789')
print(trans(b'http://www.csdn.net/wirelessqa 520520'))  # b'55'
'''

# partition() 方法用来根据指定的分隔符将字符串进行分割。
# 如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
Str = 'fhdjshfkldhjghiurethfjksdhufdgfjkfhldjrhjsalkjsdhfhurhfk'
print Str.partition('l')
print Str.partition('z')

#Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
STR = 'This is Richie form Nokia EAI Solution team , he is a Coder, this is the first time he touching Python '
print STR.replace('is','was')
print STR.replace('is','was',3)

#Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
str3 = 'this is Richie speaking'
print str3.split()
print str3.split(' ',1)
# split re 模块
a='Beautiful, is; better*than\nugly'
x= re.split(',|; |\*|\n',a)
print(x)
#Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
str1 = 'ab c\n\nde fg\rkl\r\n'
print str1.splitlines()
print str1.splitlines(True)
