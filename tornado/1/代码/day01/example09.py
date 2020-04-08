#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: example09.py
@time: 2020/3/6 10:09 上午
'''


import tornado.web
import tornado.ioloop
import tornado.options
from tornado.web import url

from settings import params


# 定义接收参数的名称和类型，缺省值
tornado.options.define('port',default=9090,type=int)

def square(n):
    return n * n

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 获取cookie
        # username = self.get_cookie('username')
        # 获取安全的cookie
        username = self.get_secure_cookie('username')


        houses = [
            {
                "price": 398,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            },
            {
                "price": 398,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            },
            {
                "price": 200,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            },
            {
                "price": 120,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            },
            {
                "price": 398,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            }]
        content = "<h1>意大利除了足球还有新冠</h1>"
        self.render("index1.html",houses=houses,content=content,square= square,username=username)


class ShowHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("child.html",title="继承")


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        # 设置cookie
        # self.set_cookie('username','admin',expires_days=3)
        # 安全的cookie
        # self.set_secure_cookie('username','admin')
        self.render("login.html")
    def post(self):
        print(self.request.body)
        username = self.get_argument('username')
        self.set_secure_cookie('username',username)
        self.redirect("/")


class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie('username')
        # 反向引用，根据name求请求路径
        print(self.reverse_url('index'))
        self.redirect(self.reverse_url('index'))

class UserCheckHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        # 验证逻辑
        username = self.get_secure_cookie('username')
        print(username)
        return username

class ReplyHandler(UserCheckHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("reply.html")

    #提交回复
    @tornado.web.authenticated
    def post(self):
        self.write("提交回复")



def main():
    # 接收命名行参数
    tornado.options.parse_command_line()
    # 路由的写法
    app = tornado.web.Application(
        [url(r'/',IndexHandler,name='index'),
         (r'/show/',ShowHandler),
         (r'/login/',LoginHandler),
         (r'/logout/',LogoutHandler),
         (r'/reply/',ReplyHandler),
         ],
        **params
    )
    app.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()