#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: views.py
@time: 2020/3/2 9:17 上午
'''
import hashlib
import os
from datetime import datetime

from flask import Blueprint, render_template, request, session, redirect, url_for, flash, current_app
from flask import request
from App.ext import db ,photos
from App.forms import RegisterForm
from App.models import User, Sessions

blue = Blueprint("blue",__name__)
# 用户验证装饰器
def check_login(func):
    def inner(*args,**kwargs):
        # 验证逻辑
        if session.get("username"):
            return func(*args,**kwargs)
        else:
            return redirect("/login/")
    return inner

@blue.route("/")
def index():
    # 判断是否登录
    username = session.get('username')
    print(username)
    return render_template("index.html")

@blue.route("/login/",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print(request.values.to_dict())
        username = request.values.get('username')
        password = request.values.get('password')
        # 验证用户名和密码
        user = User.query.filter(User.username==username,User.password==password).first()
        if user:
            # 设置session
            session['username'] = "sdfdsfds"
            session['uid'] = "sdfkjsdfjk"
            session['hello'] = "3333"
            return redirect("/")
        else:
            # 消息闪烁
            flash("用户名或密码错误")
            return redirect(url_for("blue.login"))
    return render_template("login.html")

@blue.route("/logout/")
def logout():
    # 清除单个键值对
    # session.pop('username')
    session.clear()
    return redirect("/")

@blue.route("/reply/")
@check_login
def user_reply():
    return "回复"

@blue.route("/session/")
def handle_session():
    from uuid import uuid4
    import json
    # sessionid = uuid4().hex
    # userinfo = {"username":'tom','password':'123'}
    # value = json.dumps(userinfo)
    # print(value,type(value))
    # sess = Sessions(sessionid=sessionid,value=value)
    # db.session.add(sess)
    # db.session.commit()

    # 获取session
    sessionid = "5b25470aa3ce42eb950ef9f6aa2e32da" #request.cookies.get("session")
    sess = Sessions.query.filter(Sessions.sessionid==sessionid).first()
    print(sessionid,sess)
    print(sess.value)
    userinfo = json.loads(sess.value)
    print(userinfo,type(userinfo))
    print(userinfo.get('username'))
    return "session"

@blue.route("/register/",methods=['GET','POST'])
def register_user():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        # 验证成功，返回True，否则返回False
        if form.validate_on_submit():
            # 获取验证数据
            username = form.username.data
            password = form.password.data
            user = User(username=username)
            # 保存用户信息
            user.password = hashlib.sha1(password.encode('utf8')).hexdigest()
            db.session.add(user)
            db.session.commit()
            return redirect("/")
    return render_template("register.html",**locals())

@blue.route("/format/")
def format_time():
    time = datetime.utcnow()
    return render_template("formatdatetime.html",**locals())


# 文件上传
@blue.route("/upload/",methods=['GET','POST'])
def upload():
    if request.method == "POST":
        # 获取文件上传对象
        fobj = request.files.get("photo")
        if fobj:
            #保存文件路径
            # current_app是当前应用程序对象的分身
            path = current_app.config.get('UPLOADED_FOLDER')
            path = os.path.join(path,fobj.filename)
            print(path)
            # 保存文件
            fobj.save(path)
            return "文件上传成功"
        return "文件上传失败"
    return render_template('upload.html')


@blue.route("/file/",methods=["GET",'POST'])
def upload_file():
    if request.method == "POST":
        fobj = request.files.get("photo")
        if fobj:
            photos.save(fobj)
            return "上传成功"
        return "上传失败"
    return render_template("upload2.html")
