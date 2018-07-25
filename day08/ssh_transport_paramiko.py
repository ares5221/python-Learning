#!/usr/bin/env python
# -*- coding: utf-8 -*-
#SSHClient 封装 Transport
import paramiko
# 实例化一个transport对象
transport = paramiko.Transport(('192.168.199.146', 22))
# 建立连接
transport.connect(username='fishman', password='9')
# 将sshclient的对象的transport指定为以上的transport
ssh = paramiko.SSHClient()
ssh._transport = transport
# 执行命令，和传统方法一样
stdin, stdout, stderr = ssh.exec_command('df')
print (stdout.read().decode())
# 关闭连接
transport.close()
