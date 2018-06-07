#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/6/7'
"""
data = [10, 4, 33, 21, 54, 3, 8, 11, 5, 22, 2, 1, 17, 13, 6]
print("before sort:", data)
#冒泡排序，每次将一个最大的放到最后，可以优化加一个标志位，标志已经排序的，不需要每次比较已经排好的后面的数
for j in range(len(data)):
    tmp = 0
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            tmp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = tmp
    print(data)

print("after sprt:",data)