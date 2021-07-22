# 组合数

def dfs(layer, y):
    if layer == 6:
        print(' '.join(str(num) for num in lotto))
        return
    for i in range(y + 1, n - 5 + layer):
        lotto.append(numbers[i])
        dfs(layer + 1, i)
        lotto.pop()


flag = 1
while 1:
    x = input().split(' ')
    if x[0] == '0':
        break

    if flag:
        flag = 0
    else:
        print()
    temp = []
    for X in x:
        temp.append(int(X))
    n = temp[0]
    numbers = temp[1:]
    numbers.sort()
    lotto = []
    dfs(0, -1)
