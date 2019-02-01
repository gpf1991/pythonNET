import os, sys
from socket import *

def client_handler(c):
    print('客户端:', c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print('Receive:', data.decode())
        c.send(b'thanks')
    c.close()



# 创建套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

s = socket()  # TCP套接字
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 循环等待接收客户端请求
print('Listen to the port 8888...')
while True:
    try:
        c, addr = s.accept()
        # print('c:', c)
    except KeyboardInterrupt:
        s.close()
        sys.exit('退出服务器')
    except Exception as e:
        print('Error:', e)
        continue
    # 创建新的进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        p = os.fork()
        if p == 0:  # 二级子进程,避免僵尸进程
            s.close()
            client_handler(c)  # 处理具体请求
            sys.exit(0)  # 子进程处理完请求即退出
        else:
            os._exit(0)
    # 父进程或者创建进程失败都继续等待下一个客户端连接
    else:
        c.close()
        os.wait()
    


