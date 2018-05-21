#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
print(sys.path)

#test List
nameList = ["赘婿","qiangren","dawangraoming","lingaoqiming"]
print(nameList[0])#获取列表中第一元素
print(nameList[1:3])#切片输出第一第二元素
print(nameList[-3:-1])#输出倒数第二第三元素
print(nameList)
nameList.append("lvshu")#给列表尾端追加元素
nameList.insert(1,"吕小鱼")#插入元素在第一位置
nameList.remove("lvshu")#删除元素，也可用del及pop
#del nameList[1]
#nameList.pop()#默认删除最后一个元素
#print("del---->",nameList)
nameList.append("chenzuan")
nameList.insert(-1,"chenzuan")
print(nameList.count("chenzuan"))
print(nameList)
#nameList.clear()
nameList2 = ["凝仪","卢红提"]
nameList.extend(nameList2)#合并两个列表
print(nameList.index("chenzuan"))#返回找到的第一个元素的下标
print(nameList.sort())
print(nameList)
