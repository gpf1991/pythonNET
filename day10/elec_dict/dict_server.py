from socket import *
import os, sys
import pymysql
import signal
from time import ctime,sleep

# 定义一些全局变量
DICT_TEXT = './dict.txt'
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)


# 网络搭建
def main():
    # 创建数据库连接
    db = pymysql.connect('localhost','root','123456','dict')

    # 创建套接字
    s = socket()
    s.bind(ADDR)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.listen(5)
    # 处理僵尸
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    print('Listening to port 8000...')
    while True:
        try:
            c, addr = s.accept()
            print('连接客户端:', addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务端退出')
        except Exception as e:
            print('Error:', e)
            continue

        #创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            do_child(c, db) #子进程函数
            sys.exit(0)
        else:
            c.close()

def do_child(c, db):
    while True:
        data = c.recv(128).decode()
        print(c.getpeername(), ':', data)
        if (not data) or (data[0] == 'E'):
            c.close()
            sys.exit('客户端退出')
        elif data[0] == 'R':
            do_register(c, db, data)
        elif data[0] == 'L':
            do_login(c, db, data)
        elif data[0] == 'Q':
            do_query(c, db, data)
        elif data[0] == 'H':
            do_hist(c, db, data)


def do_register(c, db, data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor() #创建游标对象

    sql = "select * from user where name = '%s'" %name
    cursor.execute(sql) #执行sql语句
    r = cursor.fetchone() #取查询结果集中一笔数据

    if r != None:
        c.send(b'EXISTS')
        return

    # 插入用户
    sql = "insert into user (name, passwd)\
        values('%s', '%s')" %(name, passwd)

    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except Exception:
        db.rollback()
        c.send(b'FAILED')

def do_login(c, db, data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user where name='%s'\
        and passwd='%s'" %(name, passwd)
    #查找用户
    cursor.execute(sql)
    r = cursor.fetchone()

    if r != None:
        c.send(b'OK')
    else:
        c.send('用户名或密码不正确'.encode())
        
def do_query(c, db, data):
    l = data.split(' ')
    word = l[1]
    name = l[2]
    cursor = db.cursor()

    # 使用数据库表查词
    sql = "select interpret from words where word='%s'" %word
    #查找单词
    cursor.execute(sql)
    r = cursor.fetchone()
    # print(r)

    if r == None:
        c.send('NOT EXISTS'.encode())
    else:
        c.send(r[0].encode())
        # 把查词记录插入到历史记录表中
        sql = "insert into hist(name, word, time)\
        values('%s','%s','%s')" %(name, word, ctime())
        try:
            cursor.execute(sql)
            db.commit()
            print('insert succeeded')
        except Exception as e:
            print('Error:', e)
            db.rollback()


    # #插入历史记录
    # def insert_history():
    #     sql = "insert into hist(name, word, time)\
    #     values('%s','%s','%s')" %(name, word, ctime())
    #     try:
    #         cursor.execute(sql)
    #         db.commit()
    #     except Exception as e:
    #         db.rollback()

    # # 使用单词本查找
    # try:
    #     f = open(DICT_TEXT)
    # except:
    #     c.send(b'FAIL')
    #     return
    # for line in f:
    #     tmp = line.split(' ')[0]
    #     if tmp > word:  # tmp大于目标单词
    #         c.send(b'FAIL')
    #         f.close()
    #         return
    #     elif tmp == word:
    #         c.send(line.encode())
    #         insert_history()
    #         f.close()
    #         return
    # else:
    #     c.send(b'FAIL')
    #     f.close()


def do_hist(c, db, data):
    l = data.split(' ')
    name = l[1]
    cursor = db.cursor()
    sql = "select name,word,time from hist where name = '%s'" %name

    cursor.execute(sql)
    rs = cursor.fetchall()
    if not rs:
        c.send(b'FAIL')
        return
    else:
        c.send(b'OK')
        sleep(0.1)
    for r in rs:
        # c.send((r[0]+' ').encode())
        # c.send((r[1]+' ').encode())
        # c.send(r[2].encode())
        # c.send('\n'.encode())
        msg = '%s  %s %s \n' %(r[0], r[1], r[2])
        c.send(msg.encode())
        sleep(0.1)
    c.send(b'##')
    print('query is over')
        
main()