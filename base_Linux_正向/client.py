#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
这个文件放在我们的机器上
"""
import socket

HOST = ''   # 如果是本机最为服务端，地址可以不用填写
PORT = 8888
BUFSIZE = 10240
ADDR = (HOST, PORT)

tcp_cient = socket.socket()
tcp_cient.connect(ADDR)

print("客户端：\n")

# 数据交互循环
while True:
    msg = input('>>>')
    if msg:
        tcp_cient.send(msg.encode())   # 只能发送 bytes 类型的数据
        data = tcp_cient.recv(BUFSIZE)
        if not data:
            break
        print(data.decode())
    else:
        break

# tcp_cient.close()
# c.close()    # 主动断开   # 服务端会recv到一个空字符串