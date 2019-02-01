from socket import *
from select import *

# 准备要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 添加关注列表
rlist = [s]
wlist = []
xlist = []

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
        # 客户端连接套接字就绪，则接收消息
        else:
            data = r.recv(1024)
            if not data:
                # 客户端退出从关注列表移出
                rlist.remove(r)
                r.close()
                continue
            print('Receive from %s:%s' % (r.getpeername(), data.decode()))
            # r.send(b'Receive')
            wlist.append(r)

    for w in ws:
        w.send(b'Receive ur msg')
        wlist.remove(w)

    for x in xs:
        pass

