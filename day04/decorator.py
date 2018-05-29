#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/5/29'
"""
import time
def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("The func run time is %s" %(stop_time - start_time))
    return warpper

@timmer
def testDecorator():
    time.sleep(3)
    print("In the Main method测试装饰器！")

testDecorator()