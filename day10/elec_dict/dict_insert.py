import pymysql

f = open('dict.txt')
# 创建数据库连接对象
db = pymysql.connect('localhost', 'root', '123456', 'dict')

cursor = db.cursor()  # 创建游标

for line in f:
    tmp = line.split(' ')
    word = tmp[0]
    interpret = ' '.join(tmp[1:]).strip()

    sql = '''insert into words (word, interpret)
        values("%s", "%s")''' %(word, interpret)
    
    try:
        cursor.execute(sql) #执行sql语句
        db.commit() #提交事务
    except Exception:
        print('Error:', e)
        db.rollback()
f.close()


# fr = open('dict.txt')
# fw = open( 'wt')
# d = {}
# while True:
#     word = fr.readlines().split(' ')[0]
#     interpret = fr.readlines().split(' ')[1:]
#     if not data:
#         time.sleep(0.1)
#         break
#     d[word] = interpret
#     fw.write()
