#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#创建一个生成器
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b#此处天剑一个yield就变成了一个生成器
        a,b = b,a+b
        n = n+1
    #return "Done"

# fib(10)
#print(fib(10))
f = fib(10)
print(f.__next__())
print(f.__next__())
#通过next一直取f的值，当超过f中内容个数的时候，会抛出异常stepIteration，需要catch
g = fib(6)
while True:
    try:
        x= next(g)
        print('g: ',x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break