#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: extends.py
@time: 2020/3/4 3:21 下午
'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# 初始化第三方模块
def init_third(app):
    db.init_app(app)




