import os
from time import sleep

pid = os.fork()
print(pid)

if pid == 0:
    print('Child PID:', os.getpid())
    os._exit(0)
else:
    print('Parent process')
    while True:
        sleep(2)    

