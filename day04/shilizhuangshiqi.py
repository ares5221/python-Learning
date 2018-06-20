#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/5/30'
"""
import time
user, passwd = 'liujiefei','123456'

def auth(auth_type):
    print("auth type :",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:",*args,**kwargs)
            if auth_type == "local":
                username = input("UserName: ").strip()
                password = input("PassWord: ").strip()
                if username == user and password == passwd:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args, **kwargs)
                    print("-----after authentication-----")
                    return res
                else:
                    exit("\033[32;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print("run with ladp")
        return wrapper
    return outer_wrapper

def index():
    print("Welcom to index page")

@auth(auth_type = "local")  #home = auth(home)
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type = "ldap")  #bbs = auth(bbs)
def bbs(auth_type = "ldap"):
    print("welcome to bbs page")


index()
#home()
print(home())
bbs()