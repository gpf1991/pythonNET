from socket import *
import os, sys, time
import getpass

# 创建网络连接
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    # 连接套接字
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print('Error:', e)
        return
    
    # 进入一级界面
    while True:
        print('''
        =========Welcome=========
        -- 1.注册  2.登录  3.退出--
        =========================
        ''')
        # print('--------选择命令--------')
        # print('--------  login --------')
        # print('------- register -------')
        # print('--------  quit  --------')

        cmd = input('输入选项:')
        # if cmd not in ['1', '2', '3']:
        #     print('请输入正确选项')
        #     sys.stdin.flush() #清除标准输入
        #     continue
        if cmd.strip() == '1':
            do_register(s) #注册功能
        elif cmd.strip() == '2':
            do_login(s)
        elif cmd.strip() == '3':
            s.send(b'E')
            s.close()
            sys.exit('感谢使用')
        else:
            print('您输入有误，请输入正确选项')
            sys.stdin.flush()  #清除标准输入，防止粘连
            continue

def do_register(s):
    while True:
        name = input('请输入用户名:')
        passwd = getpass.getpass()
        passwd1 = getpass.getpass('Again:')

        if (' ' in name) or (' ' in passwd):
            print('用户名或密码不能有空格')
            continue
        if passwd != passwd1:
            print('两次密码不一致')
            continue

        msg = 'R %s %s' %(name, passwd)
        #发送请求
        s.send(msg.encode())
        #等待回复
        data = s.recv(1024).decode()
        if data == 'OK':
            print('注册成功')
            # login(s, name) #添加这一句表示直接进入二级界面
        elif data == 'EXISTS':
            print('用户名已存在，请重试')
        else:
            print('注册失败:', data)
        return

def do_login(s):
    while True:
        name = input('请输入用户名:')
        passwd = getpass.getpass()

        if (' ' in name) or (' ' in passwd):
            print('用户名或密码不能有空格')
            continue

        msg = 'L %s %s' %(name, passwd)
        #发送消息
        s.send(msg.encode())
        #接收反馈
        data = s.recv(128).decode()
        if data == 'OK':
            print('登录成功')
            login(s, name) #进入二级界面
        else:
            print('登录失败:', data) 
        return

def login(s, name):
    while True:
        print('''
        ===========查询系统===========
        -- 1.查词  2.历史记录  3.注销--
        ==============================
        ''')
        cmd = input('输入选项:')
        if cmd not in ['1', '2', '3']:
            print('您输入有误，请输入正确选项')
            sys.stdin.flush() #清除标准输入
            continue
        elif cmd.strip() == '1':
            do_query(s, name) 
        elif cmd.strip() == '2':
            do_hist(s, name)
        elif cmd.strip() == '3':
            return
        
def do_query(s, name):
    while True:
        word = input('请输入要查询的单词:')
        if word == '##':
            break
        msg = 'Q %s %s' %(word, name)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        if data == 'NOT EXISTS':
            print('查无此单词')
        else:
            print(word,':',data)

def do_hist(s, name):
    msg = 'H %s' %name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                time.sleep(0.1)
                return
            print(data, end='')
    

main()

