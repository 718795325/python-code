#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: ext.py
@time: 2020/3/2 9:17 上午
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet,IMAGES
"""
如果flask_uploads报错，需要进入flask_uploads模块，修改第26行改为：
from werkzeug.utils import secure_filename
from werkzeug.datastructures  import  FileStorage
"""

#数据库对象
db = SQLAlchemy()
migrate = Migrate(db=db)

# 创建上传对象
photos = UploadSet('photos', IMAGES)
