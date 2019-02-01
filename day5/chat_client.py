#coding=utf-8
from socket import *
import os, sys

def recv_msg(s):
    while True:
        data, addr = s.recvfrom(1024)
        # 服务器发来EXIT表示要退出
        if data.decode() == 'EXIT':
            sys.exit(0)
        print(data.decode()+'\n消息:', end='')

def send_msg(s, name, addr):
    while True:
        text = input('消息:')
        # 输入##表示退出聊天室
        if text == '##':
            msg = 'Q ' + name
            s.sendto(msg.encode(), addr)
            sys.exit('退出聊天室')
        msg = 'C %s %s' % (name, text)
        s.sendto(msg.encode(), addr)

# 创建套接字
def main():
    # 从命令行输入IP
    if len(sys.argv) < 3:
        print('argv is error!')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    # 创建套接字
    s = socket(AF_INET, SOCK_DGRAM)
    
    while True:
        name = input('请输入姓名:')
        msg = 'L ' + name
        # 发送给服务器
        s.sendto(msg.encode(), ADDR)
        # 等待回应
        data, addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print('您已进入聊天室')
            break
        else:
            print(data.decode())

    # 创建父子进程
    pid = os.fork()
    if pid < 0:
        sys.exit('创建进程失败')
    elif pid == 0:
        send_msg(s, name, ADDR)  # 发送消息
    else:
        recv_msg(s)  #接收消息

main()
