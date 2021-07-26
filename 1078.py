# 2 - 16进制判断回文

def basis(Number, x):   # 输出的是list 以防16进制输出14这种
    res = []
    temp = Number
    while temp > 0:
        res.append(temp % x)
        temp = temp // x
    return res


while 1:
    n = int(input())
    if n == 0:
        break
    Basis = []
    for X in range(2, 17):
        temp_1 = basis(n, X)
        temp_2 = temp_1[:]
        temp_2.reverse()
        if temp_1 == temp_2:
            Basis.append(X)
    if len(Basis) != 0:
        print('Number {} is palindrom in basis'.format(str(n)), ' '.join(str(i) for i in Basis))

    else:
        print('Number {} is not a palindrom'.format(str(n)))
