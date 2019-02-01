from multiprocessing import Pipe, Process
import os,time

# 创建管道对象
# fd1, fd2 = Pipe()
fd1, fd2 = Pipe(False) #fd1 --> 只读 recv， fd2 --> 只写 send

def fun(name):
    time.sleep(3)
    # fd1.send(name)
    # fd1.send([1,2,3,4])
    fd2.send('zyy')

jobs = []
for i in range(5):
    p = Process(target=fun, args=(i,))
    jobs.append(p)
    p.start()

# 从管道读取消息
for i in range(5):
    data = fd1.recv()
    print(data)

# 回收进程
for i in jobs:
    i.join()
