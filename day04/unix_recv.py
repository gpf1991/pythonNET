from socket import *
import os

if os.path.exists('./gpf'):
    os.remove('./gpf')

# 创建本地套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)

# 绑定套接字文件
sockfd.bind('./gpf')

# 监听
sockfd.listen(3)

while True:
    c, addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()

sockfd.close()


