# 字典

dic = {}
while 1:  # 做一个字典
    temp_line = input().split(' ')
    if len(temp_line) == 1:
        break
    dic[temp_line[1]] = temp_line[0]

try:
    while 1:
        word = input()
        try:
            print(dic[word])
        except KeyError:  # 如果字典里没有
            print('eh')
except EOFError:
    pass
