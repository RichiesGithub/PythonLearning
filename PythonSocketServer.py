#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
import socket
import threading

server = socket.socket()
host = socket.gethostname()
port = 9889
server.bind((host,port))
server.listen(5)
def tcplink(c,addr):
    c.send('Welcome!')
    while True:
        order = c.recv(1024)
        if order == 'exit' or not order:
            break
        else:
            c.send('Welcome:%s!'%order)
    c.close()
    print 'Connection form %s:%s has been closed'%addr






while True:
    c,addr = server.accept()
    print '连接地址：',addr
    t = threading.Thread(target =tcplink,args=(c,addr))
    t.start()





