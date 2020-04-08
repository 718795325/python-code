from flask import Flask
from flask_script import Manager
from views import blog
app = Flask(__name__)

manager = Manager(app)
app.register_blueprint(blog)


if __name__ == '__main__':
    manager.run()
