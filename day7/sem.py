from multiprocessing import Process,Semaphore
from time import sleep
import os

# 创建信号量
sem = Semaphore(3)

# 创建进程函数
def fun():
    print('%d 想执行事件' %os.getpid())
    # 消耗一个信号量
    sem.acquire()
    print('%d 执行事件' %os.getpid())
    print('---------------------')
    sleep(3)
    print('%d 执行完毕' %os.getpid())
    sem.release()  # 执行完成后添加(释放)一个信号量

jobs = []
# 5个进程想执行事件
for i in range(5):
    p = Process(target=fun)
    jobs.append(p)
    p.start()

for i in jobs:
    print(i)
    i.join()

print('Sem:', sem.get_value())