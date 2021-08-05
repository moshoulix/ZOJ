# 单词和数的混合列表，排序
# 要求数字位置是数字，字母的位置是字母，按照升序排列

while 1:
    temp_line = input().split(', ')
    if temp_line[0] == '.':
        break
    n = len(temp_line)
    temp_line[n - 1] = temp_line[n - 1].strip('.')
    numbers = []
    words = []
    flag = [0 for _ in range(n)]
    for i in range(n):
        try:
            numbers.append(int(temp_line[i]))
        except ValueError:
            words.append(temp_line[i])
            flag[i] = 1  # 记录单词位置

    numbers.sort()
    words.sort(key=lambda x: x.lower())  # 字符串应忽略大小写排序
    res = []
    for i in range(n):
        if flag[i]:
            res.append(words.pop(0))
        else:
            res.append(str(numbers.pop(0)))
    print(', '.join(i for i in res), '.', sep='')
