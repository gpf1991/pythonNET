from socket import *

# 创建套接字
sockfd = socket()

# 发起连接请求
sockfd.connect(('127.136.4.48', 1108))

with open('bee.gif', 'rb') as fr:
    # 消息收发
    while True:
        data = fr.read(1024)
        if not data:
            break
        sockfd.send(data)

print('transmition is over')
fr.close()
sockfd.close()
