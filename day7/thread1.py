import threading, os
from time import sleep

a = 1

# 线程函数
def music():
    global a 
    print('a = %d' %a)
    a = 10000
    for i in range(5):
        sleep(2)
        print('播放"需要人陪"', os.getpid())

# 创建线程对象
t = threading.Thread(target=music)
t.start()

# 主线程运行
for i in range(3):
    sleep(3)
    print('播放"听说"', os.getpid())

t.join()

print('main a = %d' %a)