#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: views.py
@time: 2020/2/26 3:50 下午
'''
import hashlib

from flask import Blueprint
from ext import db

ac = Blueprint('ac',__name__)

# 模型
class User(db.Model):
    # autoincrement 自增长
    uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(30))
    password_hash = db.Column(db.String(128),nullable=False)
    # 对应的数据库中的表名
    __tablename__ = 'user'


@ac.route('/create')
def create_table():
    # 在数据库中创建所有表(一个模型一个表)
    # db.create_all()
    return "create"

@ac.route("/drop/")
def drop_table():
    # db.drop_all()
    return "删除模型所对应的表"

###############################
# 添加记录
@ac.route("/add/")
def add_records():
    try:
        # # 对象对应记录
        # user = User(username="张三",password_hash="123")
        # db.session.add(user)
        # # sqlalchemy默认开启事务
        # db.session.commit()
        # uid = user.uid
        # return str(uid)
        # 添加多条记录
        user1 = User()
        user1.username = '吴浩'
        user1.password_hash = hashlib.sha1("123".encode("utf8")).hexdigest()

        user2 = User(username='汪益舟',password_hash="3334")
        db.session.add_all([user1,user2])
        db.session.commit()
        return "插入记录"
    except:
        db.session.rollback()
        return "数据插入失败"
