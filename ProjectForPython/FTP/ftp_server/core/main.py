import socketserver
import json,os
import hashlib,re
import settings

STATUS_CODE  = {
    200 : "Task finished",
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
    255 : "Filename doesn't provided",
    256 : "File doesn't exist on server",
    257 : "ready to send file",
    258 : "md5 verification",
    259 : "path doesn't exist on server",
    260 : "path changed",
}

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

    def pwd(self,*args):
        self.current_dir =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        current_relative_dir = self.get_relative_path(self.current_dir)
        self.send_response(200, data=current_relative_dir)

    def get_relative_path(self, abs_path):
        """return relative path of this user"""
        relative_path = re.sub("^%s" % settings.BASE_DIR, '', abs_path)
        if not relative_path: #means the relative path equals to home dir
            relative_path = abs_path
        print(("relative path", relative_path, abs_path))
        return relative_path

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            if not self.data:
                print("client is closed...")
                break
            cmd_dic = json.loads(self.data.decode())
            if cmd_dic.get('action') is not None:
                action = cmd_dic["action"]
                if hasattr(self, action):
                    func = getattr(self, action)
                    func(cmd_dic)
                else:
                    print("invalid cmd")
                    self.send_response(251)
            else:
                print("invalid cmd format")
                self.send_response(250)

    def send_response(self, status_code, data=None):
        '''向客户端返回数据'''
        response = {'status_code': status_code,
                    'status_msg': STATUS_CODE[status_code],
                    }
        # print("data",data)
        if data:
            # print("goes here....")
            response.update({'data': data})
        # print("-->data to client",response)
        self.request.send(json.dumps(response).encode())

if __name__ == "__main__":

    HOST, PORT = "localhost", 9989
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()