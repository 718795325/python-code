#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: settings.py
@time: 2020/3/4 3:21 下午
'''
import os


# 基础配置
class Config(object):
    # 项目根目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DEBUG = False
    TESTING = False
    SECRET_KEY = "slfdm90popPP(8998w8990r03pjM<M,my3837"
    DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost:3306/day06'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost:3306/day05'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class TestingConfig(Config):
    TESTING = True


CONFIG = {
    'default':Config,
    'develop': DevelopmentConfig,
    'product':ProductionConfig,
    'testing':TestingConfig
  }