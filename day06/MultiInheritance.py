#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/7/2'
"""
class  A(object):
    def fun(self):
        print("aaaa")
class B(A):
    def fun(self):
        print("bbbb")
class C:
    def fun(self):
        print("cccc")
class D(C):
    def fun(self):
        print("dddd")
class F(B,D):
    def fun(self):
        print("ffff")
if __name__ == '__main__':
    print(F.mro())
    #F==>B==>D==>A==>Object===>C
    ff = F()
    ff.fun()