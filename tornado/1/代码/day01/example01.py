#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: example01.py
@time: 2020/3/5 10:23 上午
'''
import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    # 一个请求对应一个和请求相对的方法
    def get(self):
        self.write("春暖花开")

    def post(self):
        self.write("post")


if __name__ == '__main__':
    # 创建一个web应用
    app = tornado.web.Application([(r'/',IndexHandler)])
    app.listen(9000)
    print("服务器运行......")
    # 开启事件循环
    tornado.ioloop.IOLoop.current().start()