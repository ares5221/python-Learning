#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
打开文件的模式有：
r，只读模式（默认）。
w，只写模式。【不可读；不存在则创建；存在则删除内容；】
a，追加模式。【可读；   不存在则创建；存在则只追加内容；】
"+" 表示可以同时读写某个文件
r+，可读写文件。【可读；可写；可追加】
w+，写读
a+，同a
"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
rU
r+U
"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
rb
wb
ab
'''
f = open('song.txt',encoding = "utf-8")
#first_line = f.readline()
#print(first_line)
#print(f.read())
'''
f = open('geci','',encoding='utf-8')
f.write("大王饶命\n")
f.write("新亭侯")
'''

#高效率的读文件方式，变成迭代器，比readline效率高许多，reanline会读一行，内存保存一行，最后撑爆内存
count = 0
for line in f:
    if count == 9:
        print("10hang")
        count +=1
        continue
    print(line.strip())
    count += 1


#光标回0的位置
f.seek(0)
#显示光标位置
print(f.tell())
f.read(10)
print(f.tell())


#进度条演示flush将内存中的信息刷到硬盘中
import sys,time
for i in range(20):
    sys.stdout.write("$")
    sys.stdout.flush()
    time.sleep(0.1)
