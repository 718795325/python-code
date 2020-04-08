#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: user.py
@time: 2020/3/4 9:13 上午
'''
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from App.models import User

us = Blueprint("us",__name__,url_prefix='/user')

@us.route("/login/",methods=["GET","POST"])
def user_login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)

        user = User.query.filter(User.username==username,User.password==password).first()
        if user:
            # 使用登录管理记录用
            # 参数必须是User的对象
            login_user(user)
            return redirect(url_for("bp.index"))
        else:
            flash("用户名或密码错误")

    return render_template("login.htm")

@us.route("/reply/")
@login_required
def reply_article():
    return "回复"

# 退出登录
@us.route("/logout/")
def user_logout():
    # 退出登录
    logout_user()
    return redirect('/')



@us.route("/register/",methods=["GET","POST"])
def user_register():
    return render_template("register1.htm")