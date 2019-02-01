import os

filename = './day5.txt'

#获取文件大小
size = os.path.getsize(filename)

# 父子进程公用一个文件对象偏移量会相互影响
# f = open(filename, 'rb')

pid = os.fork()
if pid < 0:
    print('Failed')
elif pid == 0:
    # 复制上半部分
    f = open(filename, 'rb')
    fw = open('1', 'wb')
    n = size // 2
    while True:
        if n < 1024:  #如果大小小于1024字节
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()
else:
    # 复制下半部分
    f = open(filename, 'rb')
    fw = open('2', 'wb')
    f.seek(size//2, 0)  #　从头开始，向后偏移一半文件大小
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()
