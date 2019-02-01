# 计算密集型
def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

# IO密集型程序
def write():
    f = open('test', 'w')
    for i in range(1200000):
        f.write('hello wold\n')
    f.close()
def read():
    f = open('test')
    lines = f.readlines()
    f.close()


