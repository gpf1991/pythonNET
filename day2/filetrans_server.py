from socket import *

# 创建套接字
sockfd = socket()

# 绑定地址
sockfd.bind(('0.0.0.0', 1108))

# 设置监听
sockfd.listen(9)

connfd, addr = sockfd.accept()

with open('b.gif', 'ab') as f:
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        f.write(data)
print('over')
connfd.close()
sockfd.close()



# while True:
#     # 等待处理客户连接
#     print("Waiting for connect...")
#     connfd, addr = sockfd.accept()
#     print('Connect from:', addr)  #打印客户端地址
#     while True:
#         data = connfd.recv(1024)
#         if not data:
#             break
#         print('Receive Msg:', data.decode())
#         n = connfd.send(b'I see')
#         print('Send %d bytes' % n)
#     connfd.close()

# sockfd.close()




