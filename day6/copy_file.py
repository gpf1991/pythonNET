# 用fork创建父子进程，同时复制一个文件，各复制一半到一个新的文件中
#   查看文件大小：os.path.getsize()

import os

filename = './day6.txt'

#获取文件大小
size = os.path.getsize(filename)

# 父子进程公用一个文件对象偏移量会相互影响
# f = open(filename, 'rb')

pid = os.fork()
if pid < 0:
    print('Failed')
elif pid == 0:
    # 子进程复制文件的上半部分
    f = open(filename, 'rb')  #　以二进制只读模式打开文件
    fw = open('1', 'wb')  #　以二进制只写模式打开文件
    n = size // 2  #　获取文件的二分之一的数据
    while True:
        #　如果数据小于1024字节
        if n < 1024:  
            data = f.read(n)  #　全部读出来 
            fw.write(data)  #　然后写进新文件中
            print('copy is done')  # 复制完成
            break  #　复制完成后结束循环
        #　如果数据大小大于1024字节
        data = f.read(1024)  #　每次读1024字节(因为每次最多读1024字节)
        fw.write(data)  # 然后写进新文件中
        n -= 1024  #　原数据每次减少1024字节，然后进行下一次循环
    f.close()  # 关闭源文件
    fw.close()  # 关闭新文件
else:
    # 父进程复制文件的下半部分
    f = open(filename, 'rb')
    fw = open('2', 'wb')
    f.seek(size//2, 0)  # 从文件的二分之一处开始读写(从头开始，向后偏移一半文件大小)
    while True:
        data = f.read(1024)
        if not data:
            print('copy is done')
            break
        fw.write(data)
    f.close() 
    fw.close()
