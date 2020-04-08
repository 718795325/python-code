#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: views.py
@time: 2020/3/3 9:00 上午
'''
from random import randint

from flask import Blueprint, render_template, request, session, make_response, redirect, jsonify, current_app
from flask_mail import Message

from App.SMS import sms
from App.extends import mail
from App.forms import RegisterForm
from App.models import User
from App.verifycode import  vc

bp = Blueprint("bp",__name__)

@bp.route("/verify/")
def verify_code():
    vc.generate()
    return response
