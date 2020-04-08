#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: settings.py
@time: 2020/3/5 11:37 上午
'''
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
params = {
    'static_path': os.path.join(BASE_DIR,'static'),
    'template_path': os.path.join(BASE_DIR,'templates'),
    'debug':True,
    'cookie_secret': "2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A=",
    'xsrf_cookies': True,
    "login_url": "/login/",
}
