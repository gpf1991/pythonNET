from socket import *

s = socket()
s.connect(('176.136.4.48', 8888))

f = open('bee.gif', 'rb')

while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

print('over')
f.close()
s.close()


