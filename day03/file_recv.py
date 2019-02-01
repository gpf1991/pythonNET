
from socket import *

s = socket()

s.bind(('0.0.0.0', 8888))

s.listen(5)

c, addr = s.accept()

f = open('b.gif', 'wb')

while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

print('OK')
c.close()
s.close()
