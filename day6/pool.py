from multiprocessing import Pool
from time import sleep,ctime

# 事件函数
def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

# 创建进程池
pool = Pool()

result = []

# 向进程池中添加事件
for i in range(10):
    msg = 'hello %d' % i
    # 异步执行：多个一同执行
    r = pool.apply_async(func=worker, args=(msg,))
    result.append(r)

    # 同步执行：一个一个执行
    # pool.apply(func=worker, args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()

for i in result:
    print(i.get()) #可以获取进程事件的返回值
