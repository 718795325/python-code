#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: test.py
@time: 2020/3/5 3:04 下午
'''
import re

# res = re.match(r'(\d{4})-(\d{8})$',"0311-80383382")
# print(res)
# print(res.groups())
# print(res.group(1),res.group(2))
res = re.match(r'/list/(\d+)/$',"/list/87/")
print(res.group(1))
res = re.match(r'/show/(?P<name>\w+)/(?P<age>\d+)/$',"/show/admin/20/")
print(res.group('name'),res.group('age'))