from socket import *
import struct

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('0.0.0.0', 8888))

# 确定数据结构
# st = struct.Struct('i5sf')

while True:
    try:
        data, addr = s.recvfrom(1024)
        # 解析数据
        data = struct.unpack('i5sf', data)
        print(data)
    except:
        break

s.close()

