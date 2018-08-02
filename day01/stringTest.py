# -*- coding: utf-8 -*-
import string
# strip去除空格
s = ' abcd efg  '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s)

# 字符串连接
print('abc_' + 'defg')
s = 'abcdefg'
s += '\nhijk'
print(str)

# 大写小
s = 'abc defg'
print(s.upper())
print(s.upper().lower())
print(s.capitalize())

# 位置和比较
s_1 = 'abcdefg'
s_2 = 'abdefgh'
print(s_1.index('bcd'))
try:
    print(s_1.index('bce'))
except ValueError:
    print('ValueError: substring not found')
print(s_1 == s_1)   # cmp函数被Python3移除了
print(s_1 > s_2)
print(s_2 > s_1)

# 分割和连接
s = 'abc,def,ghi'
print(s.split(','))
s = '123\n456\n789'
numbers = s.splitlines()
print(numbers)
print('-'.join(numbers))

# 常用判断
s = 'abcdefg'
print(s.startswith('abc'))
print(s.endswith('efg'))
print('abcd1234'.isalnum())
print('\tabcd1234'.isalnum())
print('abcd'.isalpha())
print('12345'.isdigit())
print('  '.isspace())
print('acb125'.islower())
print('A1B2C'.isupper())
print('Hello world!'.istitle())

# 数字到字符串
print(str(5))
print(str(5.))
print(str(-5.23))

# 字符串到数字
print(int('1234'))
print(float('-23.456'))
# print(int('12.33'))#invalid literal for int() with base 10: '12.33'
#字符串转换时候可以做进制转换
print("转换为十进制-----------------")
print(int('11011',2))
print(int('777',8))
print(int('fff',16))

print("十进制转换为不同进制-----------------")
print("十进制转换为二进制", bin(18))
print("十进制转换为八进制", oct(30))
print("十进制转换为十六进制", hex(18))

# 格式化字符串
print('Hello %s!' % 'world')
print('%d-%.2f-%s' % (4, -2.3, 'hello'))

#字符串转换到数组
s = 'abcdefg'
l = list(s)
print(l)
