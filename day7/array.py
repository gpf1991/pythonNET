from multiprocessing import Process, Array
import time

# 创建共享内存
# shm = Array('i', [1,2,3,4])

# 开辟５个整型空间
# shm = Array('i', 5)

# 存入字节串
shm = Array('c', b'hello')

def fun():
    for i in shm:
        time.sleep(0.5)
        print(i)
    shm[0] = b'z'  # 修改共享内存


p = Process(target=fun)
p.start()
p.join()

for i in shm:
    print(i)

print(shm.value)  # 打印字符串

shm.value = b'hi'
print(shm.value)  # 打印字符串