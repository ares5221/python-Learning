#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
# 此处定义一个dict字典对象
d = dict(name='思聪', age=29, score=80)
str = pickle.dumps(d) # 调用pickle的dumps函数进行序列化处理
print(str)
# 你可以看看它长什么样子

# 定义和创建一个file文件对象，设定模式为wb
f = open('dump.txt', 'wb')
# 将内容序列化写入到file文件中
pickle.dump(d, f)
f.close() # 最后关闭掉文件资源