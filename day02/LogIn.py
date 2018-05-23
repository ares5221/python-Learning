#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'ljf'
__mtime__ = '2018/5/23'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
import os
retry_limit = 3
retry_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'
while retry_count < retry_limit:
    username = input('\033[32;1mUsername:\033[0m')
    lock_check = open(lock_file)  #当用户输入名字后，打开lock文件，检测是否用户已经lock
    for line in lock_check.readlines():
        if username in line:
            print('\033[31;1mUser %s is locked!\033[0m' %username)
            #sys.exit()
            os._exit(0)
    password = input('\033[32;1mPassward:\033[0m')

    f = open(account_file,'rb')
    match_flag = False  #默认为falser，若匹配成功则设置为true
    for line in f.readlines():
        user,passwd = line.decode().strip('\n').split()  #去掉美航多余当\n并将这一行按空格分成两列，作为两个变量
        if username == user and password == passwd:
            print("match!!!!",username)
            match_flag = True
            break
    f.close()
    if match_flag == False:
        print("User unmatched!")
        retry_count += 1
    else:
        print("Welcom login my Python Learning!")
else:
    '''
    print("You account is Locked!")
    f.open(lock_file,"ab")
    f.write(username)
    f.close()
    '''
    print("input wrong name and passward too many times")
    os._exit(0)





















