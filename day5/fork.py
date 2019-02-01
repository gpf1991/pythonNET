import os
from time import sleep

print('*******************')
a = 1

# 创建进程
pid = os.fork()
print(pid)

if pid < 0:
    print('Create process failed')
elif pid == 0:
    a += 1
    print('Child Process')
    print('a = %d' % a)
    a = 10000
else:
    sleep(1)
    print('Parent Process')
    print('Parent a :', a)
