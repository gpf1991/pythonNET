''''
ftp 文件服务器程序
fork server 训练
'''

from socket import *
import os, sys, time

# 全局变量设置
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
FILES = '/home/tarena/abc/'

# 将文件处理功能封装
class FtpServer(object):
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        print('执行List')
        # 获取文件列表
        file_list = os.listdir(FILES)
        # 如果文件目录为空，则不许获取
        if not file_list:
            self.connfd.send('文件列表为空'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILES + file):
                files = files + file + '#'
        # 将拼接好的文件字符串发送
        self.connfd.send(files.encode())

    def do_get(self, filename):
        try:
            fd = open(FILES + filename, 'rb')
        except Exception:
            self.connfd.send('文件不存在'.encode())
            return
        
        self.connfd.send(b'OK')
        time.sleep(0.1)
        # 发送文件内容
        while True:
            data = fd.read(1024)
            # 到文件结尾
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        fd.close()

    def do_put(self, filename):
        if os.path.exists(FILES + filename):
            self.connfd.send('该文件已存在'.encode())
            return
        try:
            fd = open(FILES + filename, 'wb')
        except:
            self.connfd.send('上传失败'.encode())
            return
        self.connfd.send(b'OK')

        # 接收文件
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                time.sleep(1)
                fd.close()
                print('上传完成')
                break
            fd.write(data)
        
        
#封装并发网络模型
def main():
    # 创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    print('Listen to port 8888...')
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit('退出服务器')
        except Exception as e:
            print('Error:', e)
            continue
        print('连接客户端:', addr)

        # 创建子进程
        pid = os.fork()
        if pid == 0:
            p = os.fork()
            if p == 0:
                sockfd.close()
                # 根据客户端请求执行操作
                ftp = FtpServer(connfd)  # 创建对象

                while True:
                    # 接收请求
                    data = connfd.recv(1024).decode()
                    if not data or data[0] == 'Q':
                        connfd.close()
                        sys.exit('客户端退出')
                    elif data[0] == 'L':
                        ftp.do_list()
                    elif data[0] == 'G':
                        filename = data.split(' ')[-1]
                        ftp.do_get(filename)
                    elif data[0] == 'P':
                        filename = data.split(' ')[-1]
                        ftp.do_put(filename)
            else:
                os._exit(0)
        else:
            connfd.close()
            os.wait()

    sockfd.close()

main()