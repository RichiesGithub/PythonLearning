#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

from xml.dom.minidom import parse
import xml.dom.minidom

#使用dom 解析器打开xml文档
DOMTree = parse('movies.xml')
collections  = DOMTree.documentElement
movies = collections.getElementsByTagName('movie')
for movie in movies:
    print "*****Movie*****"
    if movie.hasAttribute('title'):
        print 'title:',movie.getAttribute('title')
    type = movie.getElementsByTagName('type')[0]
    print 'type:',type.childNodes[0].data
    format = movie.getElementsByTagName('format')[0]
    print "Format: %s" % format.childNodes[0].data
    rating = movie.getElementsByTagName('rating')[0]
    print "Rating: %s" % rating.childNodes[0].data
    description = movie.getElementsByTagName('description')[0]
    print "Description: %s" % description.childNodes[0].data
