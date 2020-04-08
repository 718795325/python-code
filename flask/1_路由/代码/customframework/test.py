#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: test.py
@time: 2020/2/24 3:17 下午
'''
#
# t1 = 3, 5
# print(t1,type(t1))
# a, b = t1
# print(a, b)

# flask路由装饰器
def wrapper(route):
    print(1111)
    def inner(func):
        print("哈哈哈")
        return func
    return inner

@wrapper(r"/") # == @inner  # hello = inner(hello)
def hello():
    print("首页")
print(hello)