from multiprocessing import Process
from time import sleep, ctime
import os

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())

p = Process(target=tm, name = 'PPP')

p.daemon = False  # 必须在start前使用

p.start()

print('Process name:', p.name)
# print('Process Parent PID:', os.getppid())
print('Process PID:', p.pid)
print('Process alive:', p.is_alive())

p.join()

print('Process alive:', p.is_alive())
