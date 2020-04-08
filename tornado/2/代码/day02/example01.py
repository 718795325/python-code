#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: example01.py
@time: 2020/3/6 9:24 上午
'''
import json

import requests   # 第三方库，负责发起请求,需要安装： pip install requests
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.websocket
from settings import config


tornado.options.define('port',default=9000,type=int)

class ClientHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("chat.html")

ws_client = set()

class ServerHandler(tornado.websocket.WebSocketHandler):
    def open(self,*args):
        ws_client.add(self)

    # 接收客户端发过来的消息
    def on_message(self, message):
        print(message)
        dict1 = {
            "reqType":0,
            "perception": {
                "inputText": {
                    "text": message
                },
            },
            "userInfo": {
                "apiKey": "ed5435dd22ff4722a23ef4702311f779",
                "userId": "csl"
            }
        }
        # 把来自客户端的信息发送给图灵机器人
        res = requests.post(url="http://openapi.tuling123.com/openapi/api/v2",
                            json=dict1)
        # 获取返回的消息
        # print(res.text)
        res = json.loads(res.text)  # 转换为字典
        print(res)
        res = res["results"][0]["values"]["text"]
        print(res)
        # 回复客户端
        self.write_message(res)


    def on_close(self):
        ws_client.remove(self)




def main():
    app = tornado.web.Application(
        [(r'/',ClientHandler),
         (r'/ws',ServerHandler),
         ],
        **config
    )
    server = tornado.web.HTTPServer(app)
    server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
