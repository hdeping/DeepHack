#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
 
"""

============================

    @author       : Deping Huang
    @mail address : xiaohengdao@gmail.com
    @date         : 2019-06-25 02:16:47
    @project      : png to html
    @version      : 0.1
    @source file  : GetHtml.py

============================
"""

import os

class GetHtml():
    """docstring for GetHtml"""
    def __init__(self):
        super(GetHtml, self).__init__()
        self.filename = "index.html"
        self.names = None

    def getNames(self):
        self.names = os.popen("ls *png")
        self.names = self.names.read()
        self.names = self.names.split("\n")
        self.names.pop()
    def getHtml(self):
        self.getNames()
        print(self.names)

        fp = open(self.filename,"w")

        for i,line in enumerate(self.names):
            print(i,line)
            fp.write('<div>%s</div>\n'%(line))
            fp.write('<img src="%s"></img>\n'%(line))
        fp.close()
        print("%s was written"%(self.filename))
                                                                
        

html = GetHtml()
html.getHtml()
        