import os
from time import sleep

pid = os.fork()
print(pid)

if pid < 0:
    print('Create process error')
elif pid == 0:
    sleep(2)
    print('New process')
else:
    sleep(3)
    print('The old process')

print('fork test end...')
