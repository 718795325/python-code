#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: app4.py
@time: 2020/2/25 3:00 下午
'''
from flask import Flask, abort
from flask_script import Manager

app = Flask(__name__)
# 实例管理器对象,负责接收终端传来的参数，解释
manager = Manager(app)

@app.route("/")
def index():
    return "Hello world"

# 抛出异常
@app.route('/error/')
def handle_error():
    abort(500)  # 抛异常,后面代码不再执行
    # abort(403)

@app.errorhandler(500)
def handle_500(err):
    return "{name}是不是睡着，{name}的代码完蛋了".format(name="程序猿")



if __name__ == '__main__':
    manager.run()