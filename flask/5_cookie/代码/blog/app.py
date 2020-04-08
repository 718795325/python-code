from flask import Flask
from flask_script import Manager
from App.views import bp
from App.ext import db
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)
app.config.from_pyfile("settings.py")

# 数据库初始化
db.init_app(app)

# 生成迁移对象
migrate =Migrate(db=db,app=app)

manager = Manager(app)
# 添加迁移命令
manager.add_command('db',MigrateCommand)

# 注册蓝图
app.register_blueprint(bp)



if __name__ == '__main__':
    manager.run()
