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

from App.models import *

bp = Blueprint('bp',__name__)

@bp.route("/")
def home():
    #查询文章数据
    articles = Article.query.all()
    return render_template("index.html",**locals())

# 博文分类展示
@bp.route("/list/")
@bp.route("/list/<int:cid>/")
@bp.route("/list/<int:cid>/<int:page>/")
def list_article(cid=-1, page=1):
    if cid < 0:  # 如果cid不带参数，值-1，就查询默认分类
        # 获取默认分类中所有的文章数据
        category = Category.query.first()
        cid = category.cid  # 获取第一个cid
    # 要实现分页，把articles换成分页对象
    # articles = db.session.query(Article, Category).filter(Article.cid == Category.cid, Category.cid == cid).all()
    # articles = db.session.query(Article, Category).filter(Article.cid == Category.cid, Category.cid == cid).all()
    obj = db.session.query(Article, Category).filter(Article.cid == Category.cid, Category.cid == cid)
    pagination = obj.paginate(page,2)

    # article_num = len(articles)
    print(pagination.items)

    # 提取分类数据
    categories = Category.query.all()
    print(categories)

    # 最近3篇文章
    three_articles = Article.query.order_by(-Article.create_time).all()[:3]
    return render_template("blog.html",**locals())


