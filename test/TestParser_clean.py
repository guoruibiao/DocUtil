# coding:utf-8
import sys
import os
import os

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/7/11'
#    __Desc__ = 测试实现public下所有生成文件的清理工作

if __name__ == "__main__":
    path = r'../public/'
    ls = os.listdir(path)
    for item in ls:
        print item, " has been removed!"
        os.remove(path + str(item))
