#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: views.py
@time: 2020/2/24 2:51 下午
'''

urlpatterns = []


# 路由装饰器
def wrapper(route):
    def inner(func):
        # 将(匹配规则，函数地址)添加到路由表
        urlpatterns.append((route,func))
        return func
    return inner


# 首页视图函数
@wrapper(r'/$')
def index(environ,start_response):
    start_response("200 ok",[('Content-type','text/html')])
    with open("templates/index.html", 'rb') as fp:
        html = fp.read()
    return [html]

# 用户列表页面
@wrapper(r'/list$')
def list(environ,start_response):
    start_response("200 ok", [('Content-type', 'text/html')])
    with open("templates/list.html", 'rb') as fp:
        html = fp.read()
    return [html]

@wrapper(r'/hello$')
def hello(environ,start_response):
    start_response("200 ok", [('Content-type', 'text/html')])
    return [b'hello']

# 路由表
# (匹配规则(匹配请求路径)，视图函数名)
# urlpatterns = [(r'/$',index),(r'/list$',list)]

print(urlpatterns)