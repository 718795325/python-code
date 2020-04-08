from flask import Flask

from flask_script import Manager

from views import ac
from ext import db

app = Flask(__name__)

#数据库连接串："数据库类型+连接驱动://用户名:密码@数据库服务器地址:端口/数据库名"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@127.0.0.1:3306/day03"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # 不用跟踪数据的变化


# 初始化数据库访问对象
db.init_app(app)


manager = Manager(app)
app.register_blueprint(ac)

if __name__ == '__main__':
    manager.run()
