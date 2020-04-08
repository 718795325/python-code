#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: settings1.py
@time: 2020/2/25 10:55 上午
'''

# 公共配置
class BaseConfig:
    SECRET_KEY = "sjkdfksdklfsdm,fm,wrio3wiorwiojrejioewrdm,as,md"


class Development(BaseConfig):
    DEBUG = True
    SERVER_NAME = "127.0.0.1:7007"

