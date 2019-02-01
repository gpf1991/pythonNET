from threading import Event

# 创建事件对象
e = Event()

e.set()  # 设置e
e.clear()  #　清除设置
print(e.is_set())

e.wait()

print('**********************')



