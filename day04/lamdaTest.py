#!/usr/bin/env python
# -*- coding: utf-8 -*-
l = [100, 20, 24, 50, 110]
new = list(filter(lambda x: x<50, l))
# 同理，py3得套个list来转化成list函数，便于打印出来
print(new)

l = [1,2,3]
new_list = list(map(lambda i: i+1, l))
print(new_list)
# Py3里，外面需要套个list：
# 这是为了让里面的值给显示出来，要不然你会得到这是个map函数# 而不是里面的值。# Py2的童鞋不虚
# 我们也可以把两个数组搞成一个单独的数组
l2 = [4,5,6]
new_list = list(map(lambda x,y: x+y, l, l2))
print(new_list)