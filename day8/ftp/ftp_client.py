from socket import *
import time, sys

# 具体请求功能
class FtpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd
    
    # 查看文件列表
    def do_list(self):
        self.sockfd.send(b'L')  # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
        else:
            print(data)  # 打印无法操作的原因

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit('谢谢使用')

    def do_get(self, filename):
        self.sockfd.send(('G ' + filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            fd = open(filename, 'wb')
            while True:
                data = self.sockfd.recv(1024)
                # 到文件结尾
                if data == b'##':
                    print('下载完成')
                    break
                fd.write(data)
            fd.close()
        else:
            print(data) #打印无法操作原因

    def do_put(self, filename):
        try:
            fr = open(filename, 'rb')
        except Exception as e:
            print('文件不存在，请重试')
            print(e)
            return

        filename = filename.split('/')[-1] #如果文件名前面有路径则取最后的文件名
        self.sockfd.send(('P ' + filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = fr.read(1024)
                # 到文件结尾
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            fr.close()
            print('上传完毕')
        else:
            print(data) #打印无法操作原因


# 网络连接
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print('连接服务器失败:', e)
        return

    ftp = FtpClient(sockfd)

    while True:
        print('\n========命令选项===========')
        print('=======    list    =======')
        print('=======  get file  =======')
        print('=======  put file  =======')
        print('=======    quit    =======')
        print('==========================\n')

        cmd = input('输入命令>>')
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd.strip()[:3] == 'get':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_get(filename)
        elif cmd.strip()[:3] == 'put':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_put(filename)
        else:
            print('您输入有误，请重试')
            continue

    sockfd.close()

main()
