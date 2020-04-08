#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: settings.py
@time: 2020/2/28 9:22 上午
'''
# 服务器地址
HOST = "127.0.0.1"
USER = "root"
PASSWORD = "123"
PORT = 3306
# DATABASE = 'day06'
DATABASE = 'blog'
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@localhost:3306/day05"
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = False