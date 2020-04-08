#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: example07.py
@time: 2020/3/5 4:20 下午
'''
#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    命令参数
@author:
@contact:
@file: example03.py
@time: 2020/3/5 11:24 上午
'''

import tornado.web
import tornado.ioloop
import tornado.options
from tornado.web import url

from settings import params


# 定义接收参数的名称和类型，缺省值
tornado.options.define('p',default=9090,type=int)

class IndexHandler(tornado.web.RequestHandler):
    def initialize(self):
        print("调用了initialize()")

    def prepare(self):
        print("调用了prepare()")

    def set_default_headers(self):
        print("调用了set_default_headers()")

    def write_error(self, status_code, **kwargs):
        print(str(status_code))
        print(kwargs)
        print("调用了write_error()")
        self.write("write_error")

    def get(self):
        print("调用了get()")
        self.send_error(404,msg="你请求的页面不存在")
        self.write("get")

    def post(self):
        print("调用了post()")
        self.send_error(200)  # 注意此出抛出了错误

    def on_finish(self):
        print("调用了on_finish()")



def main():
    # 接收命名行参数
    tornado.options.parse_command_line()
    # 路由的写法
    app = tornado.web.Application(
        [(r'/',IndexHandler),

         ],
        **params
    )
    app.listen(tornado.options.options.p)
    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()