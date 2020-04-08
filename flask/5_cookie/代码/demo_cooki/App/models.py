# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from App.ext import db



class Detail(db.Model):
    __tablename__ = 'detail'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(11))
    email = db.Column(db.String(200))
    uid = db.Column(db.ForeignKey('user.uid', ondelete='CASCADE'), unique=True)

    user = db.relationship('User', primaryjoin='Detail.uid == User.uid', backref='details')



class Reply(db.Model):
    __tablename__ = 'reply'

    rid = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(3000))
    uid = db.Column(db.ForeignKey('user.uid', ondelete='CASCADE'), index=True)
    create_time = db.Column(db.DateTime)

    user = db.relationship('User', primaryjoin='Reply.uid == User.uid', backref='replies')



class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.Integer)



class UserDetail(db.Model):
    __tablename__ = 'user_detail'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(11))
    email = db.Column(db.String(200))
    uid = db.Column(db.ForeignKey('user.uid', ondelete='CASCADE'), unique=True)

    user = db.relationship('User', primaryjoin='UserDetail.uid == User.uid', backref='user_details')
