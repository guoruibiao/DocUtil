# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/7/11'
#    __Desc__ =  用于命令行下完成操作的入口

import ParserTool,Utils
from optparse import OptionParser


def main():
    USAGE = \
        """
        '-c','--clean'    'Clean all the html files in folder public'
        '-g','--generate'   'Generate html files by using folder source!'
        """
    opt = OptionParser(usage=USAGE)
    opt.add_option('-c', '--clean', dest='clean', type='string', help='Clean all the old html files in folder public')
    opt.add_option('-g', '--generate', dest='generate', type='string',
                   help='Generate html files by using folder source!')
    (options, args) = opt.parse_args()
    clean = options.clean
    generate = options.generate

    # 实例化操作对象
    docutil = Utils.DocUtil()
    if clean == 'clean':
        docutil.clean()
        exit(0)
    if generate == 'generate':
        docutil.generate()
        exit(0)

if __name__ == "__main__":
    main()
