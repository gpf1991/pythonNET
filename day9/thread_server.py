from socket import *
from threading import Thread
import sys, os

# 客户端处理函数
def handler(c):
    print('Connect from:', c.getpeername()) #打印客户端地址
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Thanks')
    c.close()


# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 接收客户端请求
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit('服务器退出')
    except Exception as e:
        print('服务端异常：', e)
        continue

    # 创建线程
    t = Thread(target=handler, args=(c,))
    t.setDaemon(True)  # 设置Daemon值为True,表示若主线程退出，则支线程也退出
    t.start()
    

