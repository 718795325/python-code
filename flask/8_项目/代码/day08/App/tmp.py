#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: tmp.py
@time: 2020/3/4 2:52 下午
'''
from werkzeug.security import generate_password_hash,check_password_hash
import hashlib
# 生成签名
res = generate_password_hash('123')
# res1 = hashlib.sha3_256(b'123').hexdigest()
# print(res)
# print(res1)

# 密码验证
# 第一个参数，签名的密码，没签名的密码原文
print(check_password_hash(res,'123'))