#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import datetime
import urllib2
import xlwt
import socket
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
# def QuickSort(myList,start,end):
#     #判断low是否小于high,如果为false,直接返回
#     if start < end:
#         i,j = start,end
#         #设置基准数
#         base = myList[i]
#
#         while i < j:
#             #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
#             while (i < j) and (myList[j] >= base):
#                 j = j - 1
#
#             #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
#             myList[i] = myList[j]
#
#             #同样的方式比较前半区
#             while (i < j) and (myList[i] <= base):
#                 i = i + 1
#             myList[j] = myList[i]
#         #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
#         myList[i] = base
#
#         #递归前后半区
#         QuickSort(myList, start, i - 1)
#         QuickSort(myList, j + 1, end)
#     return myList
#
#
# myList =[34,6,3,88,23,61,90,34,26,63,42]
# print("Quick Sort: ")
# QuickSort(myList,0,len(myList)-1)
# print(myList)

#计算n阶矩阵对角线的和
# Lists = [[3,3,3,3] for i in range(4)]
# print Lists
# num = 0
# sum1=0
# for i in range(len(Lists)):
#     if i <=len(Lists)-1:
#         num = Lists[i][i]+Lists[i][len(Lists)-i-1]
#     sum1 +=num
# print sum1

# f = open(r"test.txt","w+")
# # 注：w+ truncates the file - 因此文件无论存在与否，结果一致
# f.write('hello')
# f.flush()
# print '+++++++++++++++++',f.read(),'+++++++++++++++++++'
# f.seek(0)
# print f.read()
# f.close()
import urllib2
# import re

# from distutils.filelist import find

# page = urllib2.urlopen('http://movie.douban.com/top250?format=text')
# contents = page.read()
# # print(contents)
# soup = BeautifulSoup(contents, "html.parser")
# print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")
# for tag in soup.find_all('div', class_='info'):
#     # print tag
#     m_name = tag.find('span', class_='title').get_text()
#     m_rating_score = float(tag.find('span', class_='rating_num').get_text())
#     m_people = tag.find('div', class_="star")
#     m_span = m_people.findAll('span')
#     m_peoplecount = m_span[3].contents[0]
#     m_url = tag.find('a').get('href')
#     print(m_name + "        " + str(m_rating_score) + "           " + m_peoplecount + "    " + m_url)

# driver = webdriver.Chrome()
# def login():
#     driver.get("https://auth.alipay.com/login/index.htm?loginScene=7&amp;goto=https%3A%2F%2Fauth.alipay.com%2Flogin%2Ftaobao_trust_login.htm%3Ftarget%3Dhttps%253A%252F%252Flogin.taobao.com%252Fmember%252Falipay_sign_dispatcher.jhtml%253Ftg%253Dhttps%25253A%25252F%25252Fwww.taobao.com%25252F&amp;params=VFBMX3JlZGlyZWN0X3VybD1odHRwcyUzQSUyRiUyRnd3dy50YW9iYW8uY29tJTJG")
#     input()
#     time.sleep(5)
#     # 点击购物车里全选按钮
#     if driver.find_element_by_id("J_SelectAll1"):
#         driver.find_element_by_id("J_SelectAll1").click()
#     # time.sleep(3)
#     now = datetime.datetime.now()
#     print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
#
# def input():
#     time.sleep(3)
#     time.sleep(3)
#     driver.get("https://cart.taobao.com/cart.htm")
#     time.sleep(2)
#
#
# def buy(buytime):
#     while True:
#         now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         if now == buytime:
#             try:
#                 # 点击结算按钮
#                 if driver.find_element_by_id("J_Go"):
#                     driver.find_element_by_id("J_Go").click()
#                 driver.find_element_by_link_text('提交订单').click()
#             except:
#                 time.sleep(1)
#         print(now)
#         time.sleep(1)
# if __name__ == "__main__":
#     # 中文账号记得decode编码
#     login()
#     # buy('2018-01-30 13:35:00')

# workbook = xlwt.Workbook()
# sheet1 = workbook.add_sheet('test', cell_overwrite_ok=True)
# # 生成sheet：test，如下图1：
# data = { \
#     "1": [u"张三", 150, 120, 100], \
#     "2": ["wang", 90, 99, 95], \
#     "3": ["wu", 60, 66, 68] \
#     }
# num = [a for a in data]
# ldata = []
# num.sort()
# for x in num:
#     t = [int(x)]
#     for a in data[x]:
#         t.append(a)
#
#     ldata.append(t)
#     print ldata
# for i, p in enumerate(ldata):
#     for j, q in enumerate(p):
#         sheet1.write(i, j, q)
#     workbook.save('C:\\test.xls')

# import string,random
# def get_clice(num):
#     res =[]
#     tmp = list(string.lowercase)
#     for i in range(num):
#         res.append(''.join(random.sample(tmp,random.randint(3,7))))
#     return res
# print get_clice(20)

# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 12345
# client.connect((host,port))
# str = client.recv(1024)
# print str
# # client.close()

# 定义一个MyParser继承自HTMLParser
# class MyParser(HTMLParser):
#     re = []  # 放置结果
#     flg = 0  # 标志，用以标记是否找到我们需要的标签
#
#     def handle_starttag(self, tag, attrs):
#         if tag == 'h3':  # 目标标签
#             for attr in attrs:
#                 if attr[0] == 'class' and attr[1] == 'tb-main-title':  # 目标标签具有的属性
#                     self.flg = 1  # 符合条件则将标志设置为1
#                     break
#         else:
#             pass
#
#     def handle_data(self, data):
#         if self.flg == 1:
#             self.re.append(data.strip())  # 如果标志为我们需要的标志，则将数据添加到列表中
#             self.flg = 0  # 重置标志，进行下次迭代
#         else:
#             pass
#
#
# my = MyParser()
# my.feed(open('xiaomin.html').read())

# import xml.sax
#
#
# class MovieHandler(xml.sax.ContentHandler):
#     def __init__(self):
#         self.CurrentData = ""
#         self.type = ""
#         self.format = ""
#         self.year = ""
#         self.rating = ""
#         self.stars = ""
#         self.description = ""
#
#     # 元素开始事件处理
#     def startElement(self, tag, attributes):
#         self.CurrentData = tag
#         if tag == "movie":
#             print "*****Movie*****"
#             title = attributes["title"]
#             print "Title:", title
#
#     # 元素结束事件处理
#     def endElement(self, tag):
#         if self.CurrentData == "type":
#             print "Type:", self.Type
#         elif self.CurrentData == "format":
#             print "Format:", self.Format
#         elif self.CurrentData == "year":
#             print "Year:", self.Fear
#         elif self.CurrentData == "rating":
#             print "Rating:", self.Rating
#         elif self.CurrentData == "stars":
#             print "Stars:", self.Stars
#         elif self.CurrentData == "description":
#             print "Description:", self.Description
#         self.CurrentData = ""
#
#     # 内容事件处理
#     def characters(self, content):
#         if self.CurrentData == "type":
#             self.Type = content
#         elif self.CurrentData == "format":
#             self.Format = content
#         elif self.CurrentData == "year":
#             self.Year = content
#         elif self.CurrentData == "rating":
#             self.Rating = content
#         elif self.CurrentData == "stars":
#             self.Stars = content
#         elif self.CurrentData == "description":
#             self.Description = content
#
#
# if (__name__ == "__main__"):
#     # 创建一个 XMLReader
#     parser = xml.sax.make_parser()
#     # turn off namepsaces
#     parser.setFeature(xml.sax.handler.feature_namespaces, 0)
#
#     # 重写 ContextHandler
#     Handler = MovieHandler()
#     parser.setContentHandler(Handler)
#
#     parser.parse("movies.xml")
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b  # 使用 yield
#         # print b
#         a, b = b, a + b
#         n = n + 1
#
#
# for n in fab(5):
#     print n


# def addlist(alist):
#     for i in alist:
#         yield i + 1
# alist = [1, 4, 6, 9]
# for x in addlist(alist):
#     print(x)

# def h():
#     print('study yield')
#     yield 5
#     print('go on!')
#
# h()
# def fun():
#     for i in range(20):
#         x=yield i
#         print('good',x)
#
# if __name__ == '__main__':
#     a=fun()
#     a.next()
#     x=a.send(5)
#     print(x)

# def s():
#     print('study yield')
#     m = yield 5
#     print(m)
#     d = yield 16
#     print('go on!')
#
#
# c = s()
# s_d1 = next(c)  # 相当于send(None)
# s_d2 = c.send('Fighting!')  # (yield 5)表达式被赋予了'Fighting!'
# print('My Birth Day:', s_d1, '.', s_d2)

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
url = 'https://ip.cn/'

## 下面的网站是用来获取代理ip的API
ip_url = 'http://proxy.w2n1ck.com:9090/random'
ip = {'http': 'http://' + requests.get(ip_url).text}
print(ip)
response = requests.get(url, headers=headers, proxies=ip, timeout=10).text
html = etree.HTML(response)
## 提取页面显示的ip
res = html.xpath('//*[@id="result"]/div/p[1]/code/text()')
print(res)



