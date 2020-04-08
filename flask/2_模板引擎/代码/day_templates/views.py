#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: views.py
@time: 2020/2/25 3:23 下午
'''
from flask import Blueprint, render_template, redirect, url_for

from user import User
# 蓝图对象
# Blueprint(self,name,import_name)
# name是蓝图名称，不要重名
# import_name 模块名
# url_prefix 路由前缀: 以/开头，结尾不要有/
bp = Blueprint('bp',__name__,url_prefix='/bp')

# 视图函数不能重名

@bp.route('/')
def hello_world():
    # return 'Hello World!'
    # 第一个参数模板文件名，
    # 后面可以任意多个关键字参数，一个参数对应模板中一个变量
    # 1.传递所有的局部变量到模板,locals()是一个字典，包含了所有的局部变量
    # name = '国士无双'
    # return render_template('index.html',**locals())
    # 2.关键字参数传递
    # return render_template('index.html',name='米老鼠')

    # 3.传字典
    return render_template('index.html',**{'name':'唐老师'})




@bp.route('/hello/')
def hello():
    return '你好世界!'

@bp.route('/var/')
def render_vars():
    age = 20
    list1 = [20,98,76]
    dict1 = {'name':'tom','age':30}
    user = User('中国',71)
    return render_template('vars.html',**locals())

# 过滤器
@bp.route("/filter/")
def my_filter():
    name = 'tom'
    content = "<h1>过滤器</h1>"
    return render_template('filter.html',**locals())

@bp.route('/call/')
def call_me():
    # 如果有蓝图，url_for("蓝图名.视图函数名")
    return redirect(url_for("bp.render_vars"))

@bp.route("/test/")
def render_test():
    return render_template('test.html',num=90)

@bp.route("/express/")
def render_express():
    return render_template('表达式.html',num=10)

@bp.route("/control/")
def render_conrol():
    return render_template('流程控制.html',num=30,list1=[1,2,3,4,5])

@bp.route('/include/')
def render_include():
    return render_template('包含.html')

@bp.route("/macro/")
def render_maro():
    return render_template('宏.html')

@bp.route('/child/')
def render_child():
    return render_template('comm/child.html',title="继承")

@bp.route('/boot/')
def render_bootstrap():
    return  render_template('继承2.html')