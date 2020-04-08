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

from settings import params


# 定义接收参数的名称和类型，缺省值
tornado.options.define('p',default=9090,type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("不到长城非好汉")


def main():
    # 接收命名行参数
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [(r'/',IndexHandler)],
        **params
    )
    app.listen(tornado.options.options.p)
    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()