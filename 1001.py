# 加法

try:
    while 1:
        data = input().split(' ')
        print(int(data[0]) + int(data[1]))
except EOFError:
    pass
