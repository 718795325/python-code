from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap

# 导入蓝图对象
from views import bp
from views2 import res

app = Flask(__name__)
# 实例化bootsrap对象
bootstrap = Bootstrap(app)
manager = Manager(app)

# 注册蓝图对象
app.register_blueprint(bp)
app.register_blueprint(res)


if __name__ == '__main__':
    manager.run()
