from test import *
import time

t = time.time()

# for i in range(10):
#     count(1, 1)

for i in range(10):
    write()
    read()

# print('Line CPU:', time.time() - t)
print('Line IO:', time.time() - t)


