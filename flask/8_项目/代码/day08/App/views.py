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


from App.SMS import sms
from App.extends import mail
from App.forms import RegisterForm
from App.models import User
from App.verifycode import  vc

bp = Blueprint("bp",__name__)

# 这个装饰器修饰的函数在路由之前执行
@bp.before_request
def req_before():
    print("before request")
    # 如果返回None,则正常通过，可以继续访问
    # return "等会访问吧"

# 在用户获取响应之前拦截
@bp.after_request
def response_after(response):
    print("hello")
    print(response,type(response))
    response = make_response("hello")
    return response




@bp.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")
@bp.route("/verify/")
def verify_code():
    result = vc.generate()
    # 把验证码字符串保存到session
    session['code'] = vc.code
    # 创建响应对象
    response = make_response(result)
    response.headers["Content-Type"] = "image/png"
    return response

# 短信验证
@bp.route("/send/",methods=["GET","POST"])
def send_sms():
    phone = request.values.get('phone')
    print(phone)
    if phone:
        # 产生验证码
        num = randint(1000,9999)
        # 添加到session
        session['sms'] = str(num)
        para = "{'number':'%d'}" % num
        res = sms.send(phone,para)
        print(res,type(res))
        return jsonify({'code':1,'msg':'发送成功'})
    return jsonify({"code":0,'msg':"电话号码不存在"})

# 用户注册
@bp.route("/register/",methods=['GET','POST'])
def register_user():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form)
            return redirect('/')
    return render_template("register1.htm",**locals())

@bp.route("/list/")
@bp.route("/list/<int:page>/")
def list_user(page=1):
    # 参数：当前页码，每页记录个数
    pagination = User.query.paginate(page,5)

    # 每页显示5个页码

    # 页码少于5页，全显
    if pagination.pages <= 5:
        pagination.page_range = range(1,6)
    # 如果多于5页
    else:
        # 当前页码如果大于等于3并且page+2小于总页数 [page-2,page+2]
        if page >= 3 and page+2 <= pagination.pages:
            pagination.page_range = range(page-2,page+3)
        # 当前页码如果大于等于3并且page+2大于总页数
        elif page >= 3 and page+2 > pagination.pages:
            pagination.page_range = range(pagination.pages - 5, pagination.pages+1)
        # 如果页码小于3  [1,5]
        elif page < 3:
            pagination.page_range = range(1,6)
    return render_template('list.html',**locals())