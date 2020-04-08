#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: app.py
@time: 2020/2/24 4:39 下午
'''
from flask import Flask

# 实例化应用对象
# 必须传的参数是当前模块名
app = Flask(__name__)

@app.route('/')  # 路由
def index():
    return "Hello world"

@app.route('/list')
def user_list():
    return "用户列表"


if __name__ == '__main__':
    app.run(debug=True)

