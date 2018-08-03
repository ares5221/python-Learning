#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process, Pipe
def f(conn):
    conn.send([42, None, 'hello from child'])
    conn.send([42, None, 'hello from child3'])
    print("from parent", conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  #声明一个管道的两端，默认全双工
    p = Process(target=f, args=(child_conn,))
    p.start()
    print("parent",parent_conn.recv())  # 父进程接收来自子进程p中发送的信息
    print("parent",parent_conn.recv())  # 父进程接收子进程发送的第二条消息，
    # print(parent_conn.recv()) #如果子进程没发送，那么会阻塞一直等待
    parent_conn.send(" hello child process")  # 父进程给子进程发送信息，子进程会相应接收
    p.join()