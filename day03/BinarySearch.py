#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/6/6'
"""
def binary_search(data_list,find_num):
    mid_index = int(len(data_list) / 2)
    mid_value = data_list[mid_index]
    if len(data_list) >1:
        if find_num == mid_value:
            print("I hace find the number :%s,and index is %s" % (mid_value, mid_index))
        elif find_num < mid_value:
            print("In the list left mid_value is", mid_value)
            binary_search(data_list[:mid_index], find_num)
        elif find_num > mid_value:
            print("In the right mid_value is", mid_value)
            binary_search(data_list[mid_index:], find_num)
    else:
        print("the number is not exist")

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
if __name__ == '__main__':
    binary_search(primes,31)
