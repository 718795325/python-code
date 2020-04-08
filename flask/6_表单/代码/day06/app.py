from flask import Flask
from flask_script import Manager
from flask_uploads import patch_request_class, configure_uploads
from App.ext import db, migrate, photos
from flask_migrate import MigrateCommand
from flask_moment import Moment


from App.views import blue

app = Flask(__name__)
app.config.from_pyfile("settings.py")

# # 配置上传对象
#
configure_uploads(app, photos)
# # 配置上传文件大小，默认为64M，
# # 若设置为None，则以MAX_CONTENT_LENGTH配置为准
patch_request_class(app, size=None)

db.init_app(app)
moment = Moment(app)

migrate.init_app(app=app)
manager = Manager(app)
manager.add_command('db',MigrateCommand)






app.register_blueprint(blue)

if __name__ == '__main__':
    manager.run()
