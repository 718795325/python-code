#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: extends.py
@time: 2020/3/3 8:58 上午
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate(db=db)
mail = Mail()
bst = Bootstrap()


# 初始化第三方库
def init_third(app):
    db.init_app(app=app)
    migrate.init_app(app)
    mail.init_app(app)
    bst.init_app(app)
