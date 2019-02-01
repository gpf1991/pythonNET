from socket import *
from select import *
import sys, time

# 准备要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 添加关注列表
rlist = [s, sys.stdin]
wlist = []
xlist = []

f = open('aaa.txt', 'a')  # 日志文件

while True:
    # 监控IO的发生
    rs, ws, xs = select(rlist, wlist, xlist)

    # 遍历三个列表确定哪个IO发生
    for r in rs:
        # 如果遍历到s，说明s就绪，则由客户端发起连接
        if r is s:
            c, addr = r.accept() #阻塞等待处理客户端连接
            print('Connect from:', addr)
            rlist.append(c)
        # 如果遍历到sys.stdin，说明sys.stdin就绪，则由终端发起连接
        elif r is sys.stdin:
            data = sys.stdin.readline()
            data = time.ctime() + ' ' + data + '\n'
            f.write(data)
            f.flush()
        # 客户端连接套接字就绪，则接收消息
        else:
            data = r.recv(1024).decode()
            if not data:
                # 客户端退出从关注列表移出
                rlist.remove(r)
                r.close()
                continue
            data = time.ctime() + ' ' + data + '\n'
            f.write(data)
            f.flush()
            r.send(b'Add logging')

