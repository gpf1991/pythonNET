from test import *
import multiprocessing as mp
import time

def io():
    write()
    read()

jobs = []
t = time.time()
for i in range(10):
    # p = mp.Process(target=count, args=(1, 1))
    p = mp.Process(target=io)
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
# print('Process CPU:', time.time() - t)
print('Process IO:', time.time() - t)



