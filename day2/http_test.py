from socket import * 

#创建套接字
s = socket()
s.bind(('0.0.0.0',8000))
s.listen(5)

c,addr = s.accept()
print("Connect from:",addr)
print("**********************************")
data = c.recv(4096)
print(data)
print("**********************************")
c.close()
s.close()

