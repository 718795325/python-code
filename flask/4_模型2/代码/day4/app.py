from flask import Flask
from flask_script import Manager
from App.ext import db
from App.views import bp

app = Flask(__name__)
app.config.from_pyfile("settings.py")
manager = Manager(app)

db.init_app(app)
app.register_blueprint(bp)



if __name__ == '__main__':
    manager.run()
