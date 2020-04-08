# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from App.ext import db

# class User(db.Model):
#     __tablename__ = 'user'
#
#     uid = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(30), nullable=False)
#     password = db.Column(db.String(128), nullable=False)
#     gender = db.Column(db.Integer)
#     # replies不会再user表中生成字段
#     # backref由评论查询用户时使用,反向引用
#     # lazy:加载关联数据的时机
#     replies = db.relationship('Reply',backref='user',lazy="dynamic")
#     # 和UserDetail是一对一关系
#     # uselist = False 体现一对一
#     detail = db.relationship('UserDetail',backref='user',uselist=False)

# 用户详情，和用户是一对一关系
# class UserDetail(db.Model):
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     phone = db.Column(db.String(11))
#     email = db.Column(db.String(200))
#     # 外键表示一对多，但unique=True,限制uid的取值不能重复，所以就是一对一
#     uid = db.Column(db.Integer,db.ForeignKey("user.uid",ondelete='CASCADE'),unique=True)
#     __tablename__ = 'detail'

#
# class Reply(db.Model):
#     __tablename__ = 'reply'
#
#     rid = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(3000))
#     # 外键在多端
#     # db.ForeignKey("被参照表的表名.主键名",ondelete="CASCADE")
#     uid = db.Column(db.Integer,db.ForeignKey("user.uid",ondelete="CASCADE"))
#     create_time = db.Column(db.DateTime)
#
#
#



