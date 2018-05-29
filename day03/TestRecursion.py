#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/5/28'
"""
#calcute jiecheng
'''
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return (n * factorial(n-1))
num = 10
res = factorial(num)
print("The number %s its factorial is %s" %(num,res))
'''
'''
#cal 斐波那契
def Fibonacci (n):
    if n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
num = 10
res = Fibonacci(num)
print("The number %s its Fibonacci is %s" %(num,res))
'''

data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]
def binary_search(dataset,find_num):
    print(dataset)
    if len(dataset) >1:
        mid = int(len(dataset)/2)
        if dataset[mid] == find_num:
            print("We find it %s ,and its index is %s"%(find_num,mid))
        elif dataset[mid] < find_num:
            print("\033[31;1m要找的数在%s右边\033[0m" %dataset[mid])
            return binary_search(dataset[mid +1:],find_num)
        else:
            print("\033[32;1m要找的数在%s左边\033[0m" %dataset[mid])
            return binary_search(dataset[0:mid],find_num)
    else:
        if dataset[0] == find_num:
            print("We find it",dataset[0])
        else:
            print("the number %s is not in the dataset" %find_num)

binary_search(data,13)