#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/5/29'
"""
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
'''
#将列表中数据都加1
b = []
for i in a:
    b.append(i+1)
print(b)

#迭代器
a = map(lambda x:x+1,a)
print(a)
for i in a:
    print(i)
'''
#迭代器相当于三行代码实现的for循环
b =[i*2 for i in range(10)]
print(b)
#生成器 只有在调用的时候才会生成相应的数据
#只记录当前的位置，只有一个next方法
c = (i*1 for i in range(10))
print(c.__next__())
print(c.__next__())
print(c.__next__())


