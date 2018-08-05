#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import selectors
import socket
sel = selectors.DefaultSelector()
def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    #默认阻塞，有活动连接就返回活动的连接列表
    events = sel.select() #默认调用epoll，如果平台如windows不支持epool会调用select
    for key, mask in events:
        callback = key.data #accept
        callback(key.fileobj, mask)  #key.fileobj = 文件句柄，没建立好连接的r