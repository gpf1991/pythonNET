from socket import *

s = socket()
s.connect(('127.0.0.1', 8888))

while True:
    data = input('>>')
    if not data:
        break
    s.send(data.encode())
    data = s.recv(1024)
    print(data.decode())

s.close()
