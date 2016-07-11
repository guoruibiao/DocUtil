# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/7/11'
#    __Desc__ = 测试index文件的生成情况

from main import ParserTool

if __name__ == "__main__":
    ls = ParserTool.Parser().get_all_source_file('public')
    index_file = open(r'./../themes/index.html', 'rb')
    a_href = ''
    for item in ls:
        # item = item.strip('.md')+'.html'
        a_href += "<a href='./../public/%s'" % (item) + ">%s" % (item) + "</a>"+"<br/>"
        print a_href
    index_data = index_file.read()
    index_file.close()
    result = index_data%(a_href)
    index = open(r'./../public/index.html','wb')
    index.write(result)
    index.close()
    print result

