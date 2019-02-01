from socket import *
import sys 

#从命令行传入服务器IP PORT
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

#创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

#消息收发
while True:
    data = input("Msg>>")
    if not data:
        break 
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("From server:",msg)

sockfd.close()






