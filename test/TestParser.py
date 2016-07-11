# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#    __author__ = '郭 璞'
#    __date__ = '2016/7/11'
#    __Desc__ =  测试Parser的生成测试用例

from core import ParserTool

if __name__ =="__main__":
    # ParserTool.parse(None,'Test.md')
    p = ParserTool.Parser()
    p.parse(style='style.css',infile='Test.md')
