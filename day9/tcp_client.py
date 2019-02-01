#tcp_client.py

from socket import *
import sys

#创建套接字
sockfd = socket()

#发起连接请求
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

# # 从终端输入地址和端口
# if len(sys.argv) < 3:
#     print('argv is error')
# HOST = sys.argv[1]
# PORT = int(sys.argv[2])
# ADDR = (HOST, PORT)
# sockfd.connect(ADDR)

#消息收发
while True:
    data = input(">>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("From server:",data.decode())

sockfd.close()







