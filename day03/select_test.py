from socket import *
from select import *

s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(3)

print('监控IO')
rs, ws, xs = select([s], [], [])
print('就绪rs:', rs)
print('就绪ws:', ws)
print('就绪xs:', xs)
