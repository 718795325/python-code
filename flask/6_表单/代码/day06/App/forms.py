#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    表单验证模块
@author:  
@contact: 
@file: forms.py
@time: 2020/3/2 2:38 下午
'''
import re

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

from App.models import User

# 自定义验证函数有两个参数，第一个表单对象，
# 第二个参数要验证的字段对象，用户输入的值是字段对象的data属性
def check_phone(form1,field):
    if not re.match(r'(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$',field.data):
        raise ValidationError("电话号码不符合规则")


class RegisterForm(FlaskForm):
    username = StringField("用户名",validators=[DataRequired("用户名必须输入")])
    password = PasswordField("密码",validators=[DataRequired("密码必须输入"),Length(min=3,max=12,message="密码长度必须在3-12位")])
    confirm = PasswordField("确认密码",validators=[EqualTo("password",message="两次密码不一致")])
    email = EmailField("邮箱",validators=[Email("邮箱格式错误")])
    phone = StringField("电话",validators=[check_phone])

    # 验证用户是否重名
    # 自定义的验证方法： validate_字段名
    def validate_username(self,field):
        # value是一个对象，获取用户输入的值应该是field.data
        print(field.data,"33333333")
        user = User.query.filter(User.username==field.data).first()
        if user:
            raise ValidationError("用户名重名")
        print("6666")
        return field
