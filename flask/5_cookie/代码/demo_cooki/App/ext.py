#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    扩展模块
@author:  
@contact: 
@file: ext.py
@time: 2020/2/29 8:25 上午
'''
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(db)