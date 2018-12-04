#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

from wsgiref.simple_server import make_server
from HelloWSGI import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('',8099,application)
print "Serving HTTP on port 8000..."
httpd.serve_forever()