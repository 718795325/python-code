#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    模板
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
    def get(self):

        # self.render("index.html",price=1200,
        #             title="宽窄巷子+160平大空间+文化保护区双地铁",
        #             comments="整套出租 - 5分/6点评 - 北京市丰台区六里桥地铁",
        #             score=5,
        #             position="北京市丰台区六里桥地铁"
        #             )
        house_info = {
            "price": 398,
            "title": "宽窄巷子+160平大空间+文化保护区双地铁",
            "score": 5,
            "comments": 6,
            "position": "北京市丰台区六里桥地铁",
            'a':[1,2,3]
        }
        self.render("index.html",**house_info)


class ShowHandler(tornado.web.RequestHandler):
    # 接收路由中的附加参数，参数个数和initialize中参数一致
    def initialize(self,name,age):
        self.name = name
        self.age = age
    # def initialize(self,**kwargs):
    #     self.name = kwargs.get('name')
    #     self.age = kwargs.get('age')

    def get(self):
        self.write("姓名:{}".format(self.name))


class ListHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("路由")


class DetailHandler(tornado.web.RequestHandler):
    def get(self,aid):
        print(aid,type(aid))
        self.write("详细信息"+aid)


def main():
    # 接收命名行参数
    tornado.options.parse_command_line()
    # 路由的写法
    app = tornado.web.Application(
        [(r'/',IndexHandler),
         (r'/show/',ShowHandler,{'name':'admin','age':20}),
         url(r'/list/',ListHandler,name='list'),
         (r'/detail/(\d+)/',DetailHandler),
         ],
        **params
    )
    app.listen(tornado.options.options.p)
    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()