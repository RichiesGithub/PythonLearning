#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import socket
import time

#获取新浪主页
#创建一个socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.settimeout(100)
# #创建一个连接
# client.connect(('www.baidu.com',80))
# client.send('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
# recvList = []
# while True:
#     data = client.recv(1024)
#     if data:
#         recvList.append(data)
#     else:
#         break
# str = ''.join(recvList)
# print 'Successfully'
# print str
# print 'Successfully'
# client.close()
# header, html = str.split('\r\n\r\n', 1)
# print header
# print html
# with open('sina.html','wb') as file:
#     file.write(html)
host = socket.gethostname()
port = 9889
client.connect((host,port))
str = client.recv(1024)
print str
time.sleep(2)
for data in ['Richie','Ann']:
    client.send(data)
    print client.recv(1024)
client.send('exit')
client.close()


