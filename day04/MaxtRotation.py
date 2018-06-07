#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/6/7'
"""
array=[[col for col in range(4)] for row in range(4)] #初始化一个4*4数组
for row in array: #旋转前先看看数组长啥样
    print(row)

print('-----开始旋转矩阵----')
for i, row in enumerate(array):
    for index in range(i, len(row)):
        tmp = array[index][i]  # get each rows' data by column's index
        array[index][i] = array[i][index]  #
        array[i][index] = tmp
    for r in array:
        print (r)
    print('--one big loop --')