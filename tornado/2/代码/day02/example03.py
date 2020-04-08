#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    tornado异步化
@author:  
@contact: 
@file: example03.py
@time: 2020/3/6 4:22 下午
'''
# tornado异步化
import time

import tornado.web
import tornado.ioloop
import asyncio
class IndexHandler(tornado.web.RequestHandler):
     async def get(self):
        await asyncio.sleep(5)
        self.write(time.ctime())

def main():
    app = tornado.web.Application([(r'/',IndexHandler)],debug=True)
    app.listen(8888)
    print("server start")
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()