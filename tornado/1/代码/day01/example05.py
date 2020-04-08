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
        # 1.获取get传参
        # 获取单值
        # print(self.get_query_argument('name',default=None))
        #获取多个值,得到一个参数列表
        print(self.get_query_arguments('name'))

        # 请求对象
        print("**"*100)
        print(self.request.method)
        print(self.request.path)
        print(self.request.remote_ip)
        print(self.request.query)
        print(self.request.body)
        print(self.request.headers)

        self.write("春暖花开")

    def post(self):
        # 2.post参数
        print(self.get_body_argument('name'))
        #获取多个参数值
        print(self.get_body_arguments('name'))
        self.write("post")


class UserHandler(tornado.web.RequestHandler):
    def get(self,name,age):
        self.write(name+"   "+age)


if __name__ == '__main__':
    # 创建一个web应用
    app = tornado.web.Application([(r'/',IndexHandler),
                                   (r'/show/(?P<name>\w+)/(?P<age>\d+)/',UserHandler),
                                   ],debug=True)
    # 创建web server
    server = tornado.web.HTTPServer(app)
    server.listen(9000)

    print("服务器运行......")
    # 开启事件循环
    tornado.ioloop.IOLoop.current().start()