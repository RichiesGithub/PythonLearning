#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import re
from selenium import webdriver
#re.match, re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

print re.match('www','www.baidu.com').span()
print re.match('com','www.baidu.com')

#re.search 扫描整个字符串并返回第一个成功的匹配。
print re.match('www','www.baidu.com').span()
print re.match('com','www.baidu.com')