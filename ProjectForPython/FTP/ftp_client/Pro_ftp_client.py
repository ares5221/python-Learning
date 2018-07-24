import socket
import json
import os,sys
import optparse
"""实现多线程的FTP的上传下载，下载可通过md5校验文件"""
STATUS_CODE  = {
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
}

class FtpClient(object):
    def __init__(self):

        # self.user = None
        # parser = optparse.OptionParser()
        # parser.add_option("-s", "--server", dest="server", help="ftp server ip_addr")
        # parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        # parser.add_option("-u", "--username", dest="username", help="username")
        # parser.add_option("-p", "--password", dest="password", help="password")
        # self.options, self.args = parser.parse_args()
        # self.verify_args(self.options, self.args)
        # self.connect(self,ip,port)
        self.client = socket.socket()

    def connect(self,ip,port):

        # self.client.connect((self.options.server, self.options.port))
        self.client.connect((ip , port))

    def verify_args(self, options, args):
        '''校验参数合法型'''
        if options.username is not None and options.password is not None:
            pass
        elif options.username is None and options.password is None:
            pass
        else:
            # options.username is None or options.password is None:
            exit("Err: username and password must be provided together..")
        if options.server and options.port:
            # print(options)
            if options.port > 0 and options.port < 65535:
                return True
            else:
                exit("Err:host port must in 0-65535")
        else:
            exit("Error:must supply ftp server address, use -h to check all available arguments.")

    def help(self):
        msg = '''
        ls                 #list files in current dir on FTP server
        pwd                #check current path on server
        cd ../..           #change directory , same usage as linux cd command
        get filename       #get file from FTP server
        put filename       #upload file to FTP server
        '''
        print(msg)

    def interactive(self):#交互
        #self.authenticate()#验证
        print("---start interactive with u...")
        while True:
            cmd = input(">>").strip()
            if len(cmd) ==0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,"cmd_%s" % cmd_str):
                func = getattr(self,"cmd_%s" % cmd_str)
                func(cmd)
            else:
                print("Invalid cmd,type 'help' to check available commands. ")
                self.help()

    def cmd_pwd(self,*args):
        data = {
            "action": "pwd"
        }
        self.client.send(json.dumps(data).encode())
        pwd_response = self.client.recv(1024)
        pwd_response = json.loads(pwd_response.decode())
        print("pwd result :",pwd_response)
        has_err = False
        if pwd_response.get("status_code") == 200:
            data = pwd_response.get("data")
            if data:
                print(data)
            else:
                has_err = True
        else:
            has_err = True
        if has_err:
            print("Error:something wrong.")

    def cmd_put(self,*args):
        """上传文件"""
        cmd_split = args[0].split()
        if len(cmd_split) >1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action": "put",
                    "filename":filename,
                    "size": filesize,
                    "overridden":True
                }
                self.client.send( json.dumps(msg_dic).encode("utf-8")  )
                print("send",json.dumps(msg_dic).encode("utf-8") )
                #防止粘包，等服务器确认。同时服务端返回标准信息如403，404，500等
                server_response = self.client.recv(1024)
                f = open(filename,"rb")
                for line in f:
                    self.client.send(line)
                else:
                    print("file upload success...")
                    f.close()
            else:
                print(filename,"is not exist")

    def cmd_get(self, *args):
        """下载文件"""
        cmd_get_split = args[0].split()
        if len(cmd_get_split) > 1:
            fileName = cmd_get_split[1]#读取要下载的文件名称
            get_msg_dic = {
                "action": "get",
                "filename": fileName,
            }
            self.client.send(json.dumps(get_msg_dic).encode("utf-8"))
            print("send", json.dumps(get_msg_dic).encode("utf-8"))
            fileSize = self.client.recv(1024)  # 从服务端返回文件大小
            print("要下载的文件的大小:", fileSize)
            self.client.send("准备好接收，可以发送".encode("utf-8"))#防止粘包
            received_size = 0
            received_data = b''
            if os.path.isfile(fileName):
                f = open(fileName + ".new", "wb")
            else:
                f = open(fileName, "wb")
            while received_size < int(fileSize.decode()):
                data = self.client.recv(1024)
                received_size += len(data)  # 每次收到的有可能小于1024，所以必须用len判断
                f.write(data)
                received_data += data
                str = '>' * (received_size // 30) + ' ' * (100 - (int(fileSize.decode() ) - received_size) // 30 )
                sys.stdout.write('\r'+str +'[%s%%]' % (received_size / (float(fileSize.decode()) )*100 ) )
                sys.stdout.flush()
            else:
                print("\n文件下载完毕...", received_size)
                file_md5 = self.client.recv(1024)  # 从服务端返回文件大小
                print("要下载的文件的md5 验证:", file_md5)
                f.close()

if __name__ == "__main__":
    ftp = FtpClient()
    ftp.connect("localhost", 9989)
    ftp.interactive()
