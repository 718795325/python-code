#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: forms.py
@time: 2020/3/3 8:59 上午
'''
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Regexp, ValidationError


class RegisterForm(FlaskForm):
    phone = StringField(validators=[Regexp(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')])
    sms = StringField()
    code = StringField()

    # 字段验证
    def validate_sms(self,field):
        print(field.data,session.get("sms"))
        if field.data != session.get("sms"):
            raise ValidationError("短信验证失败")

    def validate_code(self,field):
        print(field.data ,session.get('code'))
        if field.data != session.get('code'):
            raise ValidationError("验证码匹配失败")
