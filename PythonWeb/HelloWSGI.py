#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

def application(environ,start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello World!</h1>'
