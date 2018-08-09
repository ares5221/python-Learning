#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import threading, time
lock = threading.Lock()

def run(info_list, n):
    lock.acquire()
    info_list.append(n)
    lock.release()
    print('%s\n' % info_list)

if __name__ == '__main__':
    info = []
    for i in range(10):
        p = Process(target=run, args=[info,i])
        p.start()
        p.join()
    time.sleep(0.5)
    print('----------------threading---------------')
    for i in range(10):
        p = threading.Thread(target=run, args=[info, i])
        p.start()
        p.join()
