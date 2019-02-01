import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Create process failed')
elif pid == 0:
    print('Child %d process exit' % os.getpid())
    os._exit(2)
else:
    # 阻塞等待处理子进程退出
    pid, status = os.wait()
    print('pid:', pid)  # 退出的子进程PID
    print('status:', os.WEXITSTATUS(status)) #子进程退出状态
    print('Parent process...')
    while True:
        pass