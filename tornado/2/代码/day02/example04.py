#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: example04.py
@time: 2020/3/6 4:29 下午
'''
from tornado.web import StaticFileHandler, RedirectHandler
from aiomysql import create_pool
import time

from tornado import web
import tornado
from tornado.web import template

class MainHandler(web.RequestHandler):
    def initialize(self, db):
        self.db = db
    # 异步访问
    async def get(self, *args, **kwargs):
        uid = ""
        username = ""
        password = ""

        async with create_pool(host=self.db["host"], port=self.db["port"],
                               user=self.db["user"], password=self.db["password"],
                               db=self.db["name"], charset="utf8") as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute("SELECT uid, username, password from user")
                    try:
                        uid, username, password = await cur.fetchone()
                    except Exception as e:
                        print(e)
                        pass
        self.render("message.html", uid=uid,  username=username, password=password)
# 配置
settings = {
    "static_path": "static",#静态资源路径
    "template_path": "templates",   #模板路径
    'debug':True,
    "db": {    #数据库配置
        "host": "127.0.0.1",
        "user": "root",
        "password": "123",
        "name": "day06",
        "port": 3306
    }
}

if __name__ == "__main__":
    app = web.Application([
        ("/", MainHandler, {"db": settings["db"]}),], **settings)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()