#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle

# 从之前序列化的dump.txt文件里边读取内容
f = open('dump.txt', 'rb') # 设定文件选项模式为rb
d = pickle.load(f) # 调用load做反序列处理过程
f.close() # 关闭文件资源
print(d)
print('name is %s' % d['name'])