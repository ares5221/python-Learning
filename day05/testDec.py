#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/6/11'
"""
'''
def foo():
    print('foo')
print(foo)  # foo
foo()  # 表示执行foo函数
'''

#### 第二波 ####
def foo(x):
    print('foo' ,foo)
foo = lambda x: x + 1

print(foo(2))  # 执行下面的lambda表达式，而不再是原来的foo函数，因为函数 foo 被重新定义了
