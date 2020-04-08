#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: models.py
@time: 2020/2/27 10:11 上午
'''
from App.ext import db

# 自定义基类实现增加、删除、修改记录
class BaseModel:
    # 保存新增或修改的一条记录
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    @classmethod
    def save_all(cls,*args):
        try:
            db.session.add_all(args)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    # 删除记录
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False





# 必须继承自Model
class User(db.Model,BaseModel):
    uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    # nullable本列不能为空，必须有值
    username = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(128),nullable=False)
    # name指的是数据库表中的字段名
    sex = db.Column(db.Boolean,default=False,name='gender')

    __tablename__ = 'user'

    def __str__(self):
        return "{}   {}".format(self.uid,self.username)


class Reply(db.Model):
    __tablename__ = 'reply'

    rid = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(3000))
    uid = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)