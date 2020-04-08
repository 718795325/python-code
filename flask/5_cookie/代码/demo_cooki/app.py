from flask import Flask
from flask_script import Manager

from App.ext import db, migrate
from App.views import bp

app = Flask(__name__)
app.config.from_pyfile("settings.py")

db.init_app(app)
migrate.init_app(app)

manager = Manager(app)

# 注册蓝图
app.register_blueprint(bp)

if __name__ == '__main__':
    manager.run()
