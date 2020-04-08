from flask import Flask

app = Flask(__name__)

# 应用程序配置
# 1.直接使用配置字典config
# app.config['DEBUG'] = True
# app.config['ENV'] = "development"
# app.config["SECRET_KEY"] = "sdjkfwiuriwqrjkjsfnn,qoi"

# 2 加载配置文件
# app.config.from_pyfile("settings.py")

# 3.使用类进行配置
# from settings1 import Development
# app.config.from_object(Development)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
