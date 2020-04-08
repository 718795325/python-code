# coding: utf-8
from flask._compat import text_type
from flask_login import UserMixin
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from App.extends import db, login_manager


# 要使用登录管理器，用户类必须继承自UserMixin
class User(db.Model,UserMixin):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.Integer)

    # 如果表的主键不是id，需要重写这个方法
    def get_id(self):
        try:
            return text_type(self.uid) # 返回主键
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')


# 登录管理器的回调函数
@login_manager.user_loader
def get_user(uid):
    return User.query.get(uid)
