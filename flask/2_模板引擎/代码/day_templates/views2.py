#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: views2.py
@time: 2020/2/26 2:36 下午
'''
from flask import Blueprint, render_template

res = Blueprint('res',__name__,url_prefix='/res')

@res.route('/index')
def index():
    return render_template('static.html')