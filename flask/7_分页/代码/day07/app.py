from flask import Flask
from flask_script import Manager

from App.extends import init_third
from App.views import bp

app = Flask(__name__)
app.config.from_pyfile("settings.py")
manager = Manager(app)
init_third(app)

# 注册蓝图
app.register_blueprint(bp)

if __name__ == '__main__':
    manager.run()
