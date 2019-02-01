# 创建二级子进程避免僵尸

import os
from time import sleep

def f1():
    sleep(3)
    print('事件1...')

def f2():
    sleep(4)
    print('事件2...')

pid = os.fork()

if pid < 0:
    print('Failed')
elif pid == 0:
    p = os.fork()  #创建二级子进程
    if p == 0:
        f2()    # 二级子进程完成事件
    else:
        os._exit(0)  #一级子进程退出
else:
    os.wait() #等待回收一级子进程
    f1()
