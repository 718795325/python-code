#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    视图
@author:  
@contact: 
@file: views.py
@time: 2020/2/27 9:40 上午
'''
from flask import Blueprint, render_template, redirect, url_for
from App.models import User, db, Reply

"""
urlpatterns = [('/bp/',bp.home)]
"""


bp = Blueprint('bp',__name__,url_prefix='/bp')

@bp.route("/")
def home():
    return render_template("child1.html")

@bp.route("/show/")
def show():
    print(url_for("bp.home"))
    return redirect(url_for("bp.home"))

@bp.route("/create/")
def db_create():
    db.create_all()
    return "创建表"
# 修改记录
@bp.route("/update/")
def db_update():
    # 查询记录
    user = User.query.get(1)
    # print(user)
    # user.password = "123"

    # 删除记录
    if user:
        db.session.delete(user)
    # 默认是开启事务，必须手动提交
    db.session.commit()

    return "更新记录"

@bp.route("/change/")
def db_change():
    # 增加一条记录
    # user = User(username='华为',password='123')
    # user.save()
    # from hashlib import sha1
    # 更新
    # user = User.query.get(3)
    #     # if user:
    #     #     user.password = sha1("23423".encode('utf8')).hexdigest()
    #     #     user.save()

    # 删除
    # user = User.query.get(3)
    # if user:
    #     user.delete()

    # 增加多条记录
    user1 = User(username="李泽",password='123')
    user2 = User(username="骆鑫",password='123')
    User.save_all(user1,user2)
    return "change"

# 查询
@bp.route("/find/")
def find():
    # 基础查询
    # 1 get 根据主键值查询，获取一条记录，不成返回None，成功返回模型对象
    # user = User.query.get(3)
    # if user: # 判断对象是否存在
    #     print(user,type(user))

    # 2.all 查询表中的所有记录 [obj,obj...]
    # users = User.query.all()
    # print(users,type(users))

    # 3 first从结果集中取一条记录
    # user = User.query.first()
    # print(user,type(user))

    # 获取指定字段[(),(),....]
    # users = User.query.with_entities(User.username,User.uid).all()
    # users = db.session.query(User).with_entities(User.username).all()
    # print(users)

    # 去除重复记录
    # users = db.session.query(User.password).distinct().all()
    # print(users)

    # 排序
    # 字段前的-表示降序，默认是升序
    # data = User.query.order_by(-User.uid).all()
    # 多列排序
    # data = User.query.order_by(-User.sex,User.password).all()
    # # print(data)
    # for user in data:
    #     print(user)

    """
    select [字段列表]
    from [表名]
    [where]
    [group by]
    [having]
    [order by]
    [limit]
    """
    # 聚合函数 ：max min count sum avg
    from sqlalchemy import func
    # [(3,)]
    # data = db.session.query(func.count(User.uid)).all()
    # (3,)
    # data = db.session.query(func.count(User.uid)).first()
    # 3  scalar()直接获取数值，返回的必须是一条记录一个字段
    # data = db.session.query(func.count(User.uid)).scalar()
    # 统计记录个数可以直接使用count方法
    # data = db.session.query(User).count()

    # data = db.session.query(func.max(User.uid)).scalar()
    # data = User.query.with_entities(func.min(User.uid)).scalar()
    # print(data)

    # 分组
    # 统计user表中男和女的数目
    # [(False, 2), (True, 1)]
    # data = db.session.query(User.sex,func.count(User.uid)).group_by(User.sex).all()
    # having
    # [(False, 2)]

    # data = db.session.query(User.sex,func.count(User.sex)).group_by(User.sex).having(func.count(User.sex)>1).all()
    # num = func.count(User.sex).label("num")
    # data = db.session.query(User.sex,num).group_by(User.sex).having(num>1).all()
    # print(data)

    # limit offset
    # limit取开头n条记录
    # data = User.query.limit(2).all()
    # offset跳过n条记录
    # data = User.query.offset(1).limit(1).all()
    # print(data)

    # 条件查询
    # 关系运算
    # data = User.query.filter(User.uid==2).all()
    # data = User.query.filter(User.uid!=2).all()
    # uid != 2
    # data = User.query.filter(User.uid.__ne__(2)).all()
    # uid!=2 and uid < 5 默认多个条件之间是逻辑与的关系
    # data = User.query.filter(User.uid!=2, User.uid<5).all()

    # 字符串处理  like
    # data = User.query.filter(User.username.like("李%")).all()
    # data = User.query.filter(User.username.like('%鑫%')).all()

    # in_和notin_
    # data = User.query.filter(User.uid.in_([1,2,3])).all()
    # ~ 等价于notin_
    # data = User.query.filter(~User.uid.in_([1,2,3])).all()
    # data = User.query.filter(User.uid.notin_([1,2,3])).all()

    # 判空
    # sex is null
    # data = User.query.filter(User.sex==None).all()
    # is not null
    # data = User.query.filter(User.sex != None).all()

    from sqlalchemy import or_,not_
    # 逻辑运算
    # 逻辑或 or_
    # data = User.query.filter(or_(User.sex==None,User.uid<5)).all()
    # 逻辑非，not_
    data = User.query.filter(not_(User.sex==None)).all()
    print(data)
    return "查询"
    # return render_template('list.html',**locals())

@bp.route("/many/")
def db_union():
    # 不加连接条件的两表联合查询 笛卡尔积
    # data = db.session.query(User,Reply).all()
    # 内连接 连接条件User.uid == Reply.uid
    # select * from User u,Reply r where u.uid=r.uid
    # data = db.session.query(User,Reply).filter(User.uid==Reply.uid).all()
    # 显示内连接
    # data = db.session.query(User).join(Reply,User.uid==Reply.uid) #.all()

    # 外连接
    data = User.query.outerjoin(Reply,User.uid==Reply.uid).all()
    print(data)
    return "多表联合查询"