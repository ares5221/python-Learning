#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko
private_key = paramiko.RSAKey.from_private_key_file('/Users/ljf/.ssh/id_rsa')
# 实例化一个transport对象
transport = paramiko.Transport(('192.168.199.146', 22))
# 建立连接
transport.connect(username='fishman', pkey=private_key)
ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
res,err = stdout.read(),stderr.read()
result = res if res else err
print(result.decode())
# 关闭连接
ssh.close()