#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: views.py
@time: 2020/2/28 9:22 上午
'''
from flask import Blueprint, render_template
from sqlalchemy import distinct, or_, func

# from App.models import *
from App.blog import *

bp = Blueprint('bp',__name__)

@bp.route("/")
def home():
    #查询文章数据
    articles = Article.query.all()
    return render_template("index.html",**locals())




@bp.route("/o2m/")
def one_to_many():
    # 得到用户
    # user = User.query.get(2)
    # # 获取用户的评论
    # data = user.replies.filter(Reply.rid>1).all()

    # 从评论查用户
    # reply = Reply.query.get(4)
    # data = reply.user
    # print(data)
    return "一对多"

@bp.route("/o2o/")
def one2one():
    # 由用户查详情
    # user = User.query.get(2)
    # print(user.detail)

    # 由详情查用户
    # detail = UserDetail.query.get(1)
    # print(detail.user)

    return "一对一"


@bp.route("/index/")
def index():
    #查询
    # 获取数据
    #select * from user
    # all
    # data = User.query.all()
    # first() 获取一条数据
    # data = User.query.first()
    #get() 跟主键获取记录
    # data = User.query.get(2)
    # data = db.session.query(User).get(2)

    # select username from user
    # 指定字段列表
    # data = User.query.with_entities(User.username).all()
    #去除重复记录
    # data = db.session.query(User).with_entities(User.gender).distinct().all()
    # data = db.session.query(User.gender).distinct().all()
    # data = User.query.with_entities(distinct(User.gender)).all()

    # where
    # select * from user where gender=1
    # data = User.query.filter(User.gender==1,User.uid!=2).all()

    # or_
    # select * from user where User.uid=5 or User.gender=0
    # data = User.query.filter(or_(User.uid==5,User.gender==0),User.username.like("%李%"))

    # 字符串操作 like
    # data = User.query.filter(User.username.like("%李%")).all()

    # in not in
    # select * from user where uid in [1,2,3,4]
    # data = User.query.filter(User.uid.in_([1,2,3,4]))

    # is NULL is not null
    # select * from user where gender is null
    # data  = User.query.filter(User.gender==None).all()
    # data  = User.query.filter(User.gender!=None).all()

    # group by
    # https://www.osgeo.cn/sqlalchemy/orm/mapping_styles.html
    # num = func.avg(User.uid) # 字段别名
    # data = User.query.with_entities(num).all()
    # data = db.session.query(num).all()
    #select gender,avg(uid) from user group by gener
    # data = db.session.query(User.gender,num).group_by(User.gender).all()

    # order by
    # data = User.query.order_by(User.username,-User.uid).all()

    # limit
    # data = User.query.all()[:1]
    # select * from user limit 1
    # data = User.query.limit(1)
    # select * from user limit 2,1
    # data = User.query.offset(2).limit(1)

    # 多表联合查询
    # 隐式内连接
    # select * from user u,reply r where u.uid=r.uid
    # data = db.session.query(User,Reply).filter(User.uid==Reply.uid,User.gender==0).all()
    # 显示内连接
    # select * from user join Reply on user.uid=reply.uid
    # data = db.session.query(User).join(Reply,User.uid==Reply.uid).filter(User.uid>2)

    # 外连接
    # select * from user left join reply on user.uid=reply.uid
    # data = db.session.query(User).outerjoin(Reply,User.uid==Reply.uid).all()

    # 原生sql
    # data = db.session.execute("select * from user").fetchall()
    # print(data)
    return "首页"








""""
insert into article(title,content,cid) values('关键时期！中央企业砥柱中流稳经济！','在统筹推进新冠肺炎疫情防控和经济社会发展的关键时期，中央企业分区分级精准复工复产，既推动自身高质量发展，又引领带动上下游其他企业协同发展，助力稳就业、稳金融、稳外贸、稳外资、稳投资、稳预期，为经济发展增添新动能。',1)
insert into article(title,content,cid) values('【“数”说疫情】外国人眼中的中国战疫 ','在统筹推进新冠肺炎疫情防控和经济社会发展的关键时期，中央企业分区分级精准复工复产，既推动自身高质量发展，又引领带动上下游其他企业协同发展，助力稳就业、稳金融、稳外贸、稳外资、稳投资、稳预期，为经济发展增添新动能。',1)
insert into article(title,content,cid) values('外贸外资长期向好趋势不会改变','在统筹推进新冠肺炎疫情防控和经济社会发展的关键时期，中央企业分区分级精准复工复产，既推动自身高质量发展，又引领带动上下游其他企业协同发展，助力稳就业、稳金融、稳外贸、稳外资、稳投资、稳预期，为经济发展增添新动能。',1)

"""