#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import struct

class MyHTMLParser(HTMLParser):
    strtime=[]
    strtittle = []
    strlocal=[]


    def __init__(self):
        HTMLParser.__init__(self)
        self.in_h3 = False
        self.in_time = False
    def handle_starttag(self, tag, attrs):
        print ('<%s>' % tag)
        if tag == 'h3':
            for attr in attrs:
                if attr[0] == 'class'and attr[1]=='event-title':
                    self.in_h3 = True
                    break
                else:
                    pass
        elif tag == 'time':
            for attr in attrs:
                if attr[0]=='datetime':
                    self.in_time=True
                    break

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print data
        if self.in_h3==True and self.lasttag =='a':
            print data
            print type(data)
            self.in_h3=False
            self.strtittle.append('tittle:'+data)
        elif self.in_time == True and self.lasttag == 'time':
             print data
             # self.strtime.append('time'+data.decode('utf-8'))
             self.strtime.append('time:' + struct.unpack('>H',data))

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

if __name__=='__main__':
    parser = MyHTMLParser()
    parser.feed(open('python.html').read())
    print parser.strtittle
    print parser.strtime
