#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'
from multiprocessing import Process
import os
#Python 多进程

def run_proc(name):
    print 'Run child process:%s,%s '%(name,os.getpid())

if __name__ == '__main__':
    print 'Parent process:%s'%os.getpid()
    p = Process(target=run_proc,args=('test',))
    print os.getpid()
    print 'Process will start'
    p.start()
    p.join()
    print 'Process end'
