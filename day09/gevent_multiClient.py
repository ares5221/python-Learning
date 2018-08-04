#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
_并发100个sock连接
"""
import socket,threading
def sock_conn():
    client = socket.socket()
    client.connect(("localhost",8001))
    count = 0
    while True:
        #msg = input(">>:").strip()
        #if len(msg) == 0:continue
        client.send( ("hello %s" %count).encode("utf-8"))
        data = client.recv(1024)
        print("[%s]recv from server:" % threading.get_ident(),data.decode()) #结果
        count +=1
    client.close()

for i in range(100):
    t = threading.Thread(target=sock_conn)
    t.start()
