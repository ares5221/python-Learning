#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/5/30'
"""
import time
user, passwd = 'liujiefei','123456'

def auth():
    def wrapper(*args, **kwargs):
        username = input("UserName: ").strip()
        password = input("PassWord: ").strip()
        if username == user and password == pass

def index():
    print("Welcom to index page")
@auth
def home():
    print("welcome to home page")
@auth
def bbs():
    print("welcome to bbs page")