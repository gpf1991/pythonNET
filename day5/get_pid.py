import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Create process failed')
elif pid == 0:
    sleep(1)
    print('Child PID:', os.getpid())
    print('Get Parent PID:', os.getppid())
else:
    print('Parent PID:', os.getpid())
    print('Get Child PID:', pid)
    os._exit(0)

