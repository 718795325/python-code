#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: views.py
@time: 2020/2/26 2:58 下午
'''
from flask import Blueprint, render_template, g

blog = Blueprint('blog',__name__)


@blog.route('/')
def hello_world():
    g.name = '全局对象'
    return render_template("login.htm")

@blog.route('/index/')
def index():
    g.name = '全局对象'
    return render_template("index.html")