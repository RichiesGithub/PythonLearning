#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

import xml.sax

class MoviesHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ''
        self.Type=''
        self.Formate = ''
        self.Year = ''
        self.Rating = ''
        self.Stars = ''
        self.Description = ''

    def startElement(self, tag, attrs):
        self.CurrentData = tag
        if tag == 'movie':
            print "*****Movie*****"
            title = attrs['title']
            print 'Title:',title
    def endElement(self, tag):
        if tag == 'type':
            print 'Type:',self.Type
        elif tag == 'formate':
            print 'Formate:',self.Formate
        elif self.CurrentData == 'year':
            print 'Year:',self.Year
        elif self.CurrentData == 'rating':
            print 'Rating:',self.Rating
        elif self.CurrentData == 'stars':
            print 'Stars:',self.Stars
        elif self.CurrentData == 'description':
            print 'Description:',self.Description
        self.CurrentData = ''

    def characters(self, content):
        if self.CurrentData == 'type':
            self.Type == content
        elif self.CurrentData == 'formate':
            self.Formate == content
        elif self.CurrentData == 'year':
            self.Year == content
        elif self.CurrentData == 'rating':
            self.Rating == content
        elif self.CurrentData == 'stars':
            self.Stars == content
        elif self.CurrentData == 'description':
            self.Description == content

if __name__ == '__main__':
    # 创建一个 XMLReader
    parsed = xml.sax.make_parser()
    # turn off namepsaces
    parsed.setFeature(xml.sax.handler.feature_namespaces, 0)

    #重写contextHandler
    Handler = MoviesHandler()
    parsed.setContentHandler(Handler)
    parsed.parse('movies.xml')

