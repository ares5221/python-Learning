#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 基于私钥字符串进行连接
import paramiko
from io import StringIO
key_str = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAskNhrZGynBQD/5F//uuXvdUPBCfrcKcqoxAc5VZmdpscvGcO
2/wH3letHoZaAqu6edtSBiWl1m6925MuyZY3Ose3AGbEVu5mUTxXpT2GuYieJSLI
VN0cIW02FukcqxviJxd6IJye24IKT5iW1hcaqqWcHZBIpaZ79PvG9e360mxdcWkE
Iee7w4xu/Ma9KcrNjAc8paq7NUTYk3Ec/OsyU+0m7o2GP26YlAe/MOOgpkZcMxzp
PGYNIXHoKkjB426EMoZEl9MXBb9mSx5uRqX22t/OtzPutkNa9lPkFuSotX957BsB
1kCEbhzVpXVM1imET7CiR1b8BcJGAxt7GWTFkQIDAQABAoIBAH54j7Q0yiMxkCSh
dc3GF8H2htDMAZ3K+9T0eYu74LYFFj4UX9Zy2KJGUex2JSX/8CzEDU2PKDkaGFjP
80HR8R0i1BLU1jdWrAC2bvgszoiTBKAULU0IEg0lDlryyAQdpDVX0q2QcKQLfoU6
HMmHWsP2+ut+kgv0Mb19Y4rXbDwctmx53BJ0Ykk3RaQe8FiLOAAdFzxbGIUdIwLh
N8PEh9HW/wMFvJVEAgNu3oD0bONH+PZKasxqnOQlHrILSPQrNiXBOxCYr9u8cFx7
hl1V0yhQHnCF+JK2se6VXQnJ1pUVtWc3kRTtwas3x7IRPdNJDbj8WT6/n6ocUm+Q
OgEY9gECgYEA3CtYVABizz8GsHpged/xDkOKf9gET5m1kX/awdd3m6lkoWboB5OL
ym6YwxWpl6Fs0XHRAih3w2434MyTxqdgZf5ixMgq00PBr7itGycokLm1KO1GFjbZ
4tog3qwX6vejHsDl+TMWojxmkEjwQ1uPcQOeY96CvOafHH+kP5zmfAUCgYEAz0Ym
1y07sSfiKSDEO+99r7deex8fssk/xcFI3PgD/4zwu0zGF3QIB124cbZX6Sy6ut0d
jzX+RQm5OGUNR1m4Qg1syeNIEF/2mV0rL7+qPGIpYIsuoeuBwedNj7qTIDx4wKtm
aJcwdErEQwRJ7UOX9KEdPkKivyf4A+uT5fCsJR0CgYBE7tFF46UMLDiE8pvYLLRF
egIYCuM2pPKDLpuoSzToqL2YBycokBqZc80ib1rc3a67WL5OxarRpmWaXZL7BJaa
+G2mHOHDqZgv00tnj/gUcAB3Yuqps9y+OPtHnGwUphoNW+nk/wjcHLsj+6I2BKnB
gZeKvzUBvdcdTh13yUEknQKBgHBkmNEbPP/+IXutwdrCLYQnyXq30Mdwqzz/ZxQz
BHABK9RUeCHlkCj2X/qBJsBQudxz5ABxBbTH5gC3gvDKrMhcYT5EGSKP9rcIt09H
/faKP+eS8TFp882CMCOcxwS25b+L8ZcLTIHyvOOeIrweZ/qFlsbY+UjwUmNFzcfk
rmPdAoGBAJ9NWhf16aLQxUrPkUvHK9k7ONUadamBxA6NNvHMZxow81/p9VQK71o7
iUdJmC/+VOvGqbA3AbtqkbjBMUWGjEeVKLxMnCZngfu9J6bnWDUaYbQz3gVY63ca
KFWjRXO6GtynW0Dec0Nj/q22V5J+2ZCkIvSAQ+cI04d0Ij7RdKPl
-----END RSA PRIVATE KEY-----"""
private_key = paramiko.RSAKey(file_obj=StringIO(key_str))
transport = paramiko.Transport(('192.168.199.146', 22))
transport.connect(username='fishman', pkey=private_key)

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
res,err = stdout.read(),stderr.read()
result = res if res else err
print(result.decode())
# 关闭连接
ssh.close()
