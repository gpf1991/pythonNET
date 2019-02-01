from multiprocessing import Process
from time import sleep

# 带参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working...")

# 按照位置传递参数
# p = Process(target=worker, args=(2, 'Levis'))

# 按照键的名称传递参数
# p = Process(target=worker, kwargs = {'sec':2, 'name':'Levis'})

# 混合传参
p = Process(target=worker, args=(2,), kwargs = {'name':'Levis'})

p.start()
p.join()
