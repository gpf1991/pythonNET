from multiprocessing import Process, Value
import time, random

# 创建共享内存
money = Value('i', 10000)

# 操作共享内存增加
def boy():
    for i in range(30):
        time.sleep(0.2)
        # 对value属性操作即对共享内存操作
        money.value += random.randint(1, 1000)

def girl():
    for i in range(30):
        time.sleep(0.16)
        money.value -= random.randint(100, 900)

b = Process(target=boy)
g = Process(target=girl)
b.start()
g.start()
b.join()
g.join()

print('月余额：', money.value)

money.value = 12000
print(money.value)  # 打印字符串
