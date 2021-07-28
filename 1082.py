# 传播谣言最快，可以同时，输入的是几个联系人，和联系人可传播的路径及其权重
# 最短路径问题，floyd

while 1:
    n = int(input())
    if n == 0:
        break

    map_ = [[22 for _ in range(n)] for _ in range(n)]  # 初始化对角为0，其余为正无穷的权重矩阵
    for i in range(n):
        map_[i][i] = 0

    for i in range(n):
        temp_line = input().split(' ')
        temp = int(temp_line.pop(0))
        for j in range(temp):
            map_[i][int(temp_line[2 * j]) - 1] = int(temp_line[2 * j + 1])

    for k in range(n):  # floyd
        for i in range(n):
            for j in range(n):
                if map_[i][j] - map_[i][k] - map_[k][j] > 0:
                    map_[i][j] = map_[i][k] + map_[k][j]

    res = 22
    idx = -1
    for i in range(n):  # 看每行最大值的最小值
        temp_max = max(map_[i])
        if temp_max < res:
            idx = i
            res = temp_max
    if idx >= 0:
        print(idx + 1, res)
    else:
        print('disjoint')
