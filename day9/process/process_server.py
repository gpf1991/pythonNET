from socket import *
from multiprocessing import Process
import sys, os
import signal  # 信号处理模块

# 客户端处理函数
def handler(c):
    print('Connect from:', c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Thanks')
    c.close()
    sys.exit(0)  # 客户端退出，子进程也退出


# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 忽略子进程退出释放资源请求，交由系统处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

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

    # 创建进程
    p = Process(target=handler, args=(c,))
    p.daemon = True
    p.start()


