#!/usr/bin/env python
# -*- coding: utf-8 -*-
list_1 = [1,2,3,4,5]
list_1 = set(list_1)
print(list_1,type(list_1))
#集合是无序的，主要用来去重以及测试两组数据之间的交并补关系
list_2 = set([3,5,9,10])
print(list_1,list_2)
#交集
print(list_1.intersection(list_2))
#并集
print(list_1.union(list_2))
#补集
print()
#差集
print(list_1.difference(list_2))
#对称差集
print(list_1.symmetric_difference(list_2))
#子集
print(list_1.issubset(list_2))
#父集
print(list_1.issuperset(list_2))
print("-----------------------------------")
s = set([3, 5, 9, 10])  # 创建一个数值集合

t = set("Hello")  # 创建一个唯一字符的集合

a = t | s  # t 和 s的并集

b = t & s  # t 和 s的交集

print(t - s)  # 求差集（项在t中，但不在s中）

d = t ^ s  # 对称差集（项在t或s中，但不会同时出现在二者中）

#基本操作：

t.add('x')  # 添加一项

s.update([10, 37, 42])  # 在s中添加多项

#使用remove()S可以删除一项：

t.remove('H')

len(s)#set的长度

t in s
#测试x是否是s的成员

t not in s
#测试x是否不是s的成员


s.copy()#返回set “s”的一个浅复制
