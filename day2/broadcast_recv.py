from socket import * 

# 创建数据报套接字
s = socket(AF_INET,SOCK_DGRAM)

#设置套接字可以接受广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.bind(('0.0.0.0',9999))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print("接收广播:",msg.decode())
    except KeyboardInterrupt:
        print("停止接收")
        break 
    except Exception as e:
        print(e)

s.close()







