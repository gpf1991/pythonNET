from socket import *


sockfd = socket(AF_UNIX, SOCK_STREAM)

# 两端需要使用相同的套接字文件
sockfd.connect('./gpf')

while True:
    msg = input('>>')
    if not msg:
        break
    sockfd.send(msg.encode())

sockfd.close()

