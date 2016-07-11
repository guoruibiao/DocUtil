# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/7/11'
#    __Desc__ = 一个协助命令行工作方式的工具类

import ParserTool
import os

class DocUtil:

    def __init__(self):
        self.parser = ParserTool.Parser()


    def generate(self):
        self.parser.parseAll()
        self.indexFile()

    def clean(self):
        path = r'../public/'
        ls = os.listdir(path)
        for item in ls:
            print item, " has been removed!"
            os.remove(path + str(item))

    def indexFile(self):
        ls = ParserTool.Parser().get_all_source_file('public')
        index_file = open(r'./../themes/index.html', 'rb')
        a_href = ''
        for item in ls:
            # item = item.strip('.md')+'.html'
            a_href += "<div class='panel panel-default'><div class='panel-heading'><li><a href='./../public/%s'" % (item) + ">%s" % (item) + "</a>" + "</li></div></div>"
            print a_href
        index_data = index_file.read()
        index_file.close()
        result = index_data % (a_href)
        index = open(r'./../public/index.html', 'wb')
        index.write(result)
        index.close()
