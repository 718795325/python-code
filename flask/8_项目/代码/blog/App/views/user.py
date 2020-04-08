#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: user.py
@time: 2020/3/4 3:21 下午
'''

from flask import Blueprint

us = Blueprint("us",__name__,url_prefix='/user')

@us.route("/hello/")
def hello_world():
    return "Hello"