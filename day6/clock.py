from multiprocessing import Process
import time

class ClockProcess(Process):
    def __init__(self, value):
        super().__init__()
        self.value = value

    # 重写run 方法
    def run(self):
        for i in range(5):
            print('The time is:', time.ctime())
            time.sleep(self.value)

# 创建自定义类进程对象
p = ClockProcess(2)
p.start()  # 自动调用run
p.join()


