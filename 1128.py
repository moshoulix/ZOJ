# 离散

idx = 0
while 1:
    idx += 1
    n = int(input())
    if not n:
        break

    sq = []
    for _ in range(0, n):
        sq.append(list(map(float, input().split(' '))))

    x = []
    y = []
    for i in range(0, n):
        x.append(sq[i][0])
        x.append(sq[i][2])
        y.append(sq[i][1])
        y.append(sq[i][3])
    x.sort()
    y.sort()
    res = 0.0
    map_ = [[0 for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]  # 一个网格，记录哪些小格被覆盖
    for square in sq:
        for i in range(x.index(square[0]), x.index(square[2])):
            for j in range(y.index(square[1]), y.index(square[3])):
                map_[i][j] = 1

    for i in range(2 * n - 1):  # 遍历被覆盖的网格以此加上面积
        for j in range(2 * n - 1):
            if map_[i][j]:
                res += (x[i + 1] - x[i]) * (y[j + 1] - y[j])

    print('Test case #{}'.format(idx))
    print('Total explored area: {:.2f}'.format(res))
    print()
