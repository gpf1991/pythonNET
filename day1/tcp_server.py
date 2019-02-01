#tcp_server.py

import socket

#创建TCP套接子
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0',8888))

#设置监听
sockfd.listen(5)

#等待处理客户端连接
print("Waiting for connect...")
connfd,addr = sockfd.accept()
print("Connect from",addr)  #打印客户端地址

#消息收发
data = connfd.recv(1024)
print("Receive Msg:",data.decode())

n = connfd.send(b"I see")
print("Send %d bytes"%n)

#关闭套接子
connfd.close()
sockfd.close()







