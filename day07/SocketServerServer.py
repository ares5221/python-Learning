#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        while True:
            self.data = self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            if not self.data:
                print(self.client_address,"断开了")
                break
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())

if __name__ == "__main__":

    HOST, PORT = "localhost", 7878
    # Create the server, binding to localhost on port 9999
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    #使用ThreadingTCPServer就会实现多并发，多个客户端会同时处理，不同于上面的当多个客户端请求时候会将后面当请求挂起
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
