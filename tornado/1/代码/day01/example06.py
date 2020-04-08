#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    输出
@author:  
@contact: 
@file: example06.py
@time: 2020/3/5 3:18 下午
'''

import tornado.web
import tornado.ioloop
import tornado.options

from settings import params


# 定义接收参数的名称和类型，缺省值
tornado.options.define('p',default=9090,type=int)

class IndexHandler(tornado.web.RequestHandler):
    # 限于http的方法执行,自动执行
    def set_default_headers(self):
        self.set_header("password",'123')
    def get(self):
        # write会自动将多个输出组成一个字符串返回
        # self.write("不到长城非好汉")
        # self.write("----------")
        # self.write("可上九天揽月")

        #自定义响应头
        # self.set_header("hello",'world')
        #send_error会终止代码继续执行，转而跳转到write_error执行
        self.send_error(500,title="服务器错误")

        # 可以直接输出字典
        self.write({'name':'admin','age':30})

    # 错误页面定制
    def write_error(self, status_code, **kwargs):
        self.write("你的页面不见了--")
        self.write(str(status_code))
        self.write(kwargs)


class ShowHandler(tornado.web.RequestHandler):
    def get(self):
        print("show")
        # 页面跳转
        self.redirect('/')


def main():
    # 接收命名行参数
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [(r'/',IndexHandler),
         (r'/show/',ShowHandler),
         ],
        **params
    )
    app.listen(tornado.options.options.p)
    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()