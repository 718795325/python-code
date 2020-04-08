#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    配置路由
@author:  
@contact: 
@file: app3.py
@time: 2020/2/25 11:16 上午
'''
from flask import Flask, redirect, url_for
from flask_script import Manager

app = Flask(__name__)
# 实例管理器对象,负责接收终端传来的参数，解释
manager = Manager(app)

@app.route("/")
def index():
    return "Hello world"

"""
路由规则：
1 必须以/开头
2. 最好以斜线结尾，如果不以斜线结尾，请求路径中末尾不能带斜线
@app.route('/list/<name>')
http://127.0.0.1:8009/list/tom/会报错

# 重定向 

"""

# 带参数路由,通过路由传参
@app.route('/list/<name>/')
def list(name):
    return "Hello:" + name

# 参数类型
# 1.string类型，默认的是
# string参数：<参数名>
@app.route('/show/<name>/<int:age>/')
def show(name, age):
    """
    :param name: 视图函数的参数名必须和路由参数的参数名一致
    :return:
    """
    print(name)
    return name

# 2 整型参数
# 整数参数： <int:参数名>
@app.route("/param/<int:age>/")
def get_para(age):
    print(type(age),age)
    return str(age)

# 3.path类型: 如果参数字符串中包含/，可以path类型，path类型可以把/当普通字符
# path参数：<path:参数名>
# http://127.0.0.1:8009/route/c:/python/
@app.route("/route/<path:c>")
def route(c):
    return c

# 4.float类型参数
# float参数：<float:参数名>
@app.route("/money/<float:money>")
def get_money(money):
    print(type(money))
    return str(money)

# 重定向
@app.route('/direct/')
def direct():
    print("direct")
    # 重定向,redirect("请求路径")
    # return redirect('/list/tom/')

    print(url_for('index'))  # index对应的路由是 "/"

    # url_for('函数名',参数名1=value,参数名1=value,...)
    # 功能： 根据函数名求出请求路径
    # 参数应该使用关键字参数传递
    print(url_for('list',name='admin')) #/list/admin/
    print(url_for('show',name='tom',age=20)) # /show/tom/20/

    # name = "admin"
    # return redirect('/list/{}/'.format(name))
    # return redirect(url_for('index'))
    # 多余的参数会变成get传参
    # return redirect(url_for('list',name='哈哈',sex='男'))
    # 请求路径一般是内部，但不局限于内部
    return redirect("http://www.baidu.com")



if __name__ == '__main__':
    manager.run()