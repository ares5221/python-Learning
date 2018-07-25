#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko
private_key = paramiko.RSAKey.from_private_key_file('/Users/ljf/.ssh/id_rsa')
transport = paramiko.Transport(('192.168.199.146', 22))
transport.connect(username='fishman', password='9')
sftp = paramiko.SFTPClient.from_transport(transport)

# LocalFile.txt 上传至服务器 /home/fishman/test/remote.txt
# sftp.put('LocalFile.txt', '/home/fishman/test/remote.txt')
# 将LinuxFile.txt 下载到本地 fromlinux.txt文件中
sftp.get('/home/fishman/test/LinuxFile.txt', 'fromlinux.txt')

transport.close()