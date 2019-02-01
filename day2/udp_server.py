#udp_server.py

from socket import *

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
sockfd.bind(('0.0.0.0',8888))

#消息收发
while True:
    data,addr = sockfd.recvfrom(1024)
    print("Receive from %s:%s"%(addr,data.decode()))
    sockfd.sendto(b"Thanks for your msg",addr)

#关闭套接字
sockfd.close()



