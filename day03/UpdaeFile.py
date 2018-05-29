#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#实现修改文件，或者插入到指定位置
f = open("song.txt","r",encoding="utf-8")
f_new = open("song.bak","w",encoding="utf-8")

for line in f:
    if "就如夜晚的微风" in line:
        line = line.replace("就如夜晚的微风","替换为新的文本")
    f_new.write(line)
f.close()
f_new.close()