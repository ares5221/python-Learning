#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import random
def timmer(func):
    def wrapper():
        print('11111')
        start_time = time.time()
        func()
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
    return wrapper
def auth(func):
    def deco():
        print('22222')
        name=input('name: ')
        password=input('password: ')
        if name == 'egon' and password == '123':
            print('login successful')
            func() #wrapper()
        else:
            print('login err')
    return deco

@auth   # index = auth(timmer(index))
@timmer # index = timmer(index)
def index():
    time.sleep(3)
    print('welecome to index page')

index()