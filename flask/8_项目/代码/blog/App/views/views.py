#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: views.py
@time: 2020/3/4 3:20 下午
'''

from flask import Blueprint, render_template

blog = Blueprint('blog',__name__)


@blog.route("/")
def index():
    return render_template("index.html")