
def fun():
    print('生成器')
    yield 1
    yield 2
    print('生成器完成')

# 生成器对象
g = fun()
# 启动生成器
print(next(g))
print(next(g))
print(next(g))
