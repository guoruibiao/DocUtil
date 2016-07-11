# coding:utf-8

#    __author__ = '郭 璞'
#    __date__ = '2016/7/11'
#    __Desc__ = 用于markdown转换成html的工具类

from markdown import markdown
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')


class Parser:
    def __init__(self):
        self.style = None
        self.infile = None
        print "Ready to init Parser tool!"

    def parse(self, style=None, infile=None):
        title = infile.strip('.md')
        style_file = open(r'./../themes/' + str(style), 'rb')
        style = style_file.read()
        style_file.close()
        head = """
            <html><head><meta charset='utf-8'><title>%s</title><meta name="viewport" content="width=device-width, initial-scale=1">
            <style>%s</style>
            <link rel="stylesheet" href="http://apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css">
            <script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
            <script src="http://apps.bdimg.com/libs/bootstrap/3.3.0/js/bootstrap.min.js"></script></head><body><div class='container'><div class="row-fluid">
            <div class="span12">
             """ % (title, style)

        content_file = open(r'./../source/' + str(infile), 'rb')
        content = content_file.read()
        content_file.close()
        content = markdown(content)

        temp_data = head + content

        tail = """
            <div class="span-12">
            <!-- 添加评论功能-->
            <div id="uyan_frame"></div>
            <script type="text/javascript" id="UYScript" src="http://v1.uyan.cc/js/iframe.js?UYUserId=0" async="">
            </script>
            </div>
             </div></div></div><script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
             <script src="http://apps.bdimg.com/libs/bootstrap/3.2.0/js/bootstrap.min.js"></script></body></html>
             """
        result = temp_data + tail
        outputfile = open(r'./../public/' + str(title) + ".html", 'wb')
        outputfile.write(result)
        outputfile.close()
        print outputfile.name.strip('./../'), "Generate Success!"

    def get_all_source_file(self, foldername):
        return os.listdir(r'./../' + str(foldername) + str('/'))

    def parseAll(self):
        ls = self.get_all_source_file('source')
        style = r'./../themes/style.css'
        for item in ls:
            self.parse(style=style, infile=item)
