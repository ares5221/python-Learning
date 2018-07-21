import socket
import json
import os,sys
"""实现多线程的FTP的上传下载，下载可通过md5校验文件"""
class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()
    def help(self):
        msg = '''
        ls
        pwd
        cd ../..
        get filename
        put filename
        '''
        print(msg)
    def connect(self,ip,port):
        self.client.connect((ip, port))
    def interactive(self):#交互
        #self.authenticate()#验证
        while True:
            cmd = input(">>").strip()
            if len(cmd) ==0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,"cmd_%s" % cmd_str):
                func = getattr(self,"cmd_%s" % cmd_str)
                func(cmd)
            else:
                self.help()
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
    ftp.connect("localhost", 9999)
    ftp.interactive()
