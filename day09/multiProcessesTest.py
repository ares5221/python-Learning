#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import time
import threading
def thread_run():
    print(threading.get_ident())

def run(name):
    time.sleep(2)
    print(name, " 进程启动")
    #在进程中再启动线程
    t = threading.Thread(target=thread_run, )
    t.start()

if __name__ == '__main__':
    # mp = multiprocessing.Process(target=run, args=("LJ",))
    # mp.start()
    # mp.join() # 等待进程执行完毕
# 生成多个进程
    for i in range(10):
        p = multiprocessing.Process(target=run, args=('Jerey %s' %i,))
        p.start()