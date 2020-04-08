#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    配置文件
@author:  
@contact: 
@file: settings.py
@time: 2020/3/3 9:00 上午
'''
from datetime import timedelta

DEBUG = True
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@localhost:3306/day06"
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 签名加密，session使用
SECRET_KEY = "i9490kl*(780990HGjhsoid7872378287mn,,.,ghghY!@3"

# session是否持久存储
PERMANENT = True
# session存活时间
PERMANENT_SESSION_LIFETIME = timedelta(days=3)


# 邮件配置
MAIL_SERVER = "smtp.126.com"
MAIL_USERNAME = "landmark_csl@126.com"
MAIL_PASSWORD = "land123"
