from multiprocessing import Queue, Process
import time

# 创建消息队列
q = Queue()

def fun1():
    for i in range(5):
        time.sleep(1)
        q.put((1,2))  # 存储消息

def fun2():
    for i in range(5):
        time.sleep(1.5)
        a,b = q.get()  # 取出消息
        print('sum =', a + b)

p1 = Process(target = fun1)
p2 = Process(target = fun2)
p1.start()
p2.start()
p1.join()
p2.join()
