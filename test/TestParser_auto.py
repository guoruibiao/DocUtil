# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/7/11'
#    __Desc__ = 测试直接生成全部文件的方式

from main import ParserTool

if __name__ == "__main__":
    p = ParserTool.Parser()
    p.parseAll()
