#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
这个文件放在我们的机器上
"""
import socket

HOST = '192.168.111.1'   # 如果是本机最为服务端，地址可以不用填写
PORT = 8888
BUFSIZE = 10240
ADDR = (HOST, PORT)

tcp_cient = socket.socket()
tcp_cient.connect(ADDR)

print("客户端：\n")

# 数据交互循环
while True:
    try:
        msg = input('>>>')
        if msg:
            tcp_cient.send(msg.encode('gbk'))  # 只能发送 bytes 类型的数据
            data = tcp_cient.recv(BUFSIZE)
            if not data:
                break
            # print(data.decode('utf-8'))
            print(data.decode('gbk'))
        else:
            break
    except Exception as e:
        print(e)
        continue

