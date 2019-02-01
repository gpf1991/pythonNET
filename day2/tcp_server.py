#tcp_server.py

import socket

#创建TCP套接字
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0',8888))

#设置监听
sockfd.listen(5)

while True:
    #等待处理客户端连接
    print("Waiting for connect...")
    connfd,addr = sockfd.accept()
    print("Connect from",addr)  #打印客户端地址
    #消息收发
    while True:
        data = connfd.recv(1024) 
        #客户端退出,服务端recv立即返回空字串
        if not data:
            break
        print("Receive Msg:",data.decode())
        n = connfd.send(b"I see")
        print("Send %d bytes"%n) 
    connfd.close()

#关闭套接字
sockfd.close()







