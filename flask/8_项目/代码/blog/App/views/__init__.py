#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: __init__.py.py
@time: 2020/3/4 3:20 下午
'''
from App.views.views import blog
from App.views.user import us

# 注册蓝图
def register_blueprint(app):
    app.register_blueprint(blog)
    app.register_blueprint(us)
