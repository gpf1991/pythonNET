from socketserver import *

# 创建服务器类
class Server(ThreadingMixIn, UDPServer):
    pass

class Handler(DatagramRequestHandler):
    def handle(self):
        while True:
            # 接收消息
            data = self.rfile.readline()
            if not data:
                break
            print(data.decode())
            # 发送消息
            self.wfile.write(b'OK')

server = Server(('0.0.0.0', 8888), Handler)
server.serve_forever()
