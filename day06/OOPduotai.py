#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/6/22'
"""
class Father:
    pass

class Son1(Father):
    def detail(self):
        print("This is Son 1")

class Son2(Father):
    def detail(self):
        print("This is Son 2")

def Func(obj):
    obj.detail()
# 由于在Java或C#中定义函数参数时，必须指定参数的类型
# 为了让Func函数既可以执行S1对象的show方法，又可以执行S2对象的show方法，所以，定义了一个S1和S2类的父类
# 而实际传入的参数是：S1对象和S2对象
s1 = Son1()
s2 = Son2()

Func(s1)
Func(s2)
