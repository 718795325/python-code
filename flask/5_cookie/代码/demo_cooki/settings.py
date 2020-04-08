#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: settings.py
@time: 2020/2/29 8:21 上午
'''
DEBUG = True

#  数据库
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = '123'
PORT = 3306
DATABASE = 'day06'
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KY = "2983oikls./f<>76546789ijk@#!@3fdcgvmn"
