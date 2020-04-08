#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    自定义web应用
@author:  成少雷
@contact: 
@file: application.py
@time: 2020/2/24 10:58 上午
'''
import re

from views import *

def application(environ,start_response):
    """
    自定义的web应用
    :param environ: 客户端请求的信息，字典
    :param start_response: 函数，创建响应头
    :return: 返回一个可迭代对象，一般是列表或元组：[b'hellow']
    """
    # print(environ)
    # for key in environ:
    #     print(key,environ[key])

    # 用户的请求路径(端口号后面到？前的内容)
    print(environ['PATH_INFO'])
    path = environ['PATH_INFO']
    # 第一个参数，是状态码

    # 路由问题： 把用户请求转换为对应函数调用
    # if path == '/': # 首页
    #     return index(environ,start_response)
    #     # with open("templates/index.html",'rb') as fp:
    #     #     html = fp.read()
    #     # return [html]
    # elif path == "/list":
    #     return list(environ,start_response)
    #     # start_response("503 ok", [('Content-type', 'text/html')])
    #     # html = "<html><head><meta charset='utf-8'></head><body><h1>用户列表</h1></body></html>"
    #     # return [html.encode('utf-8')]
    # else:
    #     start_response("503 ok", [('Content-type', 'text/html')])
    #     return [b"Hello world"]

    # 第二版路由
    for pattern, func in urlpatterns:
        if re.match(pattern,path):  # 匹配成功
            return func(environ,start_response)
    else: # 匹配不成功
        start_response("404 Not Found", [('Content-type', 'text/html')])
        return [b"File Not Found"]