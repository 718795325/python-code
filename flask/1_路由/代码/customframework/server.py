#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    自定义web服务器
@author:  成少雷
@contact: 313728420
@file: server.py
@time: 2020/2/24 10:54 上午
'''
# 创建测试服务器
from wsgiref.simple_server import make_server

from application import application

# web服务器
# 端口范围：1024-65536 不能和已经存在的服务的端口重复
# 一个程序一个端口，不能重复
server = make_server('127.0.0.1', 8000, application)
print("服务器启动.....运行在8000端口")

# 等待用户请求，程序不会结束
server.serve_forever()

