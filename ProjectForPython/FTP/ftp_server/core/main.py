import socketserver
import json,os
import hashlib
class MyTCPHandler(socketserver.BaseRequestHandler):

    def put(self,*args):
        '''接收客户端文件'''
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["size"]
        if os.path.isfile(filename):
            f = open(filename + ".new","wb")
        else:
            f = open(filename , "wb")

        self.request.send(b"200 ok")
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("file [%s] has uploaded..." % filename)

    def get(self, *args):
        '''给客户端传输文件'''
        get_cmd_dic = args[0]
        fileName = get_cmd_dic["filename"]
        print("要传送的文件为 ",fileName)
        if os.path.isfile(fileName):
            f = open(fileName, "rb")
            m = hashlib.md5()  #用于校验传输文件是否被损坏
            file_size = os.stat(fileName).st_size
            self.request.send(str(file_size).encode())  # send file size
            clien_msg = self.request.recv(1024)  # wait client for ack
            print("IP:",self.client_address[0],"Port:",self.client_address[1],":",clien_msg.decode("utf-8"))
            for line in f:
                m.update(line)
                self.request.send(line)
            print("file md5:", m.hexdigest())
            f.close()
            self.request.send(m.hexdigest().encode())  # send md5
        print("send done")

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)

            except ConnectionResetError as e:
                print("err",e)
                break
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()