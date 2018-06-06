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

#迭代器相当于三行代码实现的for循环
b =[i*2 for i in range(10)]
print(b)
#生成器 只有在调用的时候才会生成相应的数据
#只记录当前的位置，只有一个next方法
c = (i*1 for i in range(10))
print(c.__next__())
print(c.__next__())
print(c.__next__())
'''
from collections import Iterable
class MyList(object):
    """自定义的一个可迭代对象"""
    def __init__(self):
        self.items = []
    def add(self, val):
        self.items.append(val)
    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator

class MyIterator(object):
    """自定义的供上面可迭代对象使用的一个迭代器"""
    def __init__(self, mylist):
        self.mylist = mylist
        # current用来记录当前访问到的位置
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self

if __name__ == '__main__':
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)
    for num in mylist:
        print(num)

mylist = MyList()
print(isinstance(mylist, Iterable))


