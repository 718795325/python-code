#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: app2.py
@time: 2020/2/25 11:05 上午
'''
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
# 实例管理器对象,负责接收终端传来的参数，解释
manager = Manager(app)

@app.route("/")
def index():
    return "Hello world"

if __name__ == '__main__':
    # -d 调试模式  -h 服务器地址  -p 端口号
    #  python app2.py runserver -d -p 8008
    manager.run()