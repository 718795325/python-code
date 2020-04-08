#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: views.py
@time: 2020/2/29 8:21 上午
'''
from datetime import timedelta, datetime

from flask import Blueprint, request, make_response, render_template, redirect

from App.models import User

bp = Blueprint("bp",__name__)

@bp.route("/login/",methods=['GET','POST'])
def login():
    if request.method == "POST":
        # 处理
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)
        user = User.query.filter(User.username==username,User.password==password).first()
        print(user)
        if user: # 登录成功
            # 写cookie
            response = redirect("/")
            # 有效期是一天
            # 设置cookie
            # response.set_cookie("username",username,max_age=3600*24)

            dest = datetime.now() + timedelta(days=3)
            # expires优先级高于max_age
            response.set_cookie("username",username,expires=dest)
            return response
        else: # 登录失败
            return redirect("/login/")

    return render_template("login.html")






# 默认是get请求，如果有其他请求，应该子啊路由中指定methods
@bp.route("/",methods=['GET','POST'])
def index():
    # 请求对象request,全局对象
    # print(type(request))
    # 1.GET请求的参数获取
    # args 用户get请求的参数字典，ImmutableMultiDict 多值字典
    # print(request.args,type(request.args))
    # # 获取单一值
    # print(request.args.get("name"))
    # # 获取多值参数
    # print(request.args.getlist("hobby"))

    # 2.POST参数获取
    #ImmutableMultiDict([('username', '晓峰'), ('password', '123'), ('a', '1'), ('a', '2')])
    # print(request.form)
    # print(request.form.get('username'))
    # print(request.form.getlist('a'))

    # 3.GET和POST请求参数合体values
    # print(request.values)
    # print(request.values.get('username'))
    # print(request.values.getlist('a'))

    # 4.客户端请求地址
    # print(request.remote_addr)
    #
    # # 5.请求的完整url
    # print(request.url)
    # print(request.base_url)
    # print(request.host_url)

    # 6.请求路径
    # print(request.path)

    # 7.请求方法, 方法都是大写
    # print(request.method)

    # 其他信息
    # print(request.headers)

    # 8 cookie
    username = request.cookies.get('username')
    if username:
        return "你是合法用户"
    else:
        return "你是非法用户，请先登录"

# 退出登录
@bp.route("/logout/")
def logout():
    response = make_response("退出登录")
    # 删除指定cookie一个键值对
    response.delete_cookie('username')
    return response



@bp.route("/res/")
def handle_response():
    # 手动生成响应对象
    # with open("static/1.jpeg",'rb') as fp:
    #     content = fp.read()
    # res = make_response(content)

    # 自定义响应对象
    res = make_response("<h2>Hello world</h2>")
    res.headers['hello'] = "world"
    print(res.__dict__)
    # res.headers['Content-Type'] = "image/jpeg"
    return res

    # 自动生成响应对象
    # 返回了内容和状态码
    # return "hello",200