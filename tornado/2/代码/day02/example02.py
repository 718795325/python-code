#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: example02.py
@time: 2020/3/6 4:10 下午
'''
import time

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.websocket
from settings import config


tornado.options.define('port',default=9000,type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(3)
        self.write(("hello"))


def main():
    app = tornado.web.Application(
        [(r'/',IndexHandler),],
        **config
    )
    server = tornado.web.HTTPServer(app)
    server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
