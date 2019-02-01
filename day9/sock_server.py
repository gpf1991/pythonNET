from socketserver import *

# 创建服务器类
# class Server(ForkingMixIn, TCPServer):
# class Server(ThreadingMixIn, TCPServer):
class Server(ThreadingTCPServer):
    pass

# 具体请求处理类
class Handler(StreamRequestHandler):
    # 具体处理方法
    def handle(self):
        print('Connect form:', self.client_address)
        while True:
            # self.request就是accept返回的套接字
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'OK')

# 创建服务器对象，绑定处理类
server_addr = ('0.0.0.0', 8888)
server = Server(server_addr, Handler)
server.serve_forever() #启动服务




