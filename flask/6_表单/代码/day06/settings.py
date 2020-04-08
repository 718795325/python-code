#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: settings.py
@time: 2020/3/2 9:17 上午
'''
import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@localhost:3306/day06"
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 签名加密，session使用
SECRET_KEY = "i9490kl*(780990HGjhsoid7872378287mn,,.,ghghY!@3"

# 文件上传目录
UPLOADED_FOLDER = os.path.join(os.getcwd(),'static/upload')
UPLOADED_PHOTOS_DEST = os.path.join(os.getcwd(),'static/upload')
MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2M

