# 算网格上周长  DFS 

def neighbor(a, b):  # 判断周围八个是否有X
    x = [a]
    y = [b]
    if a > 0:
        x.append(a - 1)
    if a < length - 1:
        x.append(a + 1)
    if b > 0:
        y.append(b - 1)
    if b < width - 1:
        y.append(b + 1)
    return [(X, Y) for X in x for Y in y if grid[X][Y] == 1]


def perimeters(a, b):  # 判断上下左右四个是否有X以计算周长
    per = 4
    if a > 0:
        per -= grid[a - 1][b]
    if a < length - 1:
        per -= grid[a + 1][b]
    if b > 0:
        per -= grid[a][b - 1]
    if b < width - 1:
        per -= grid[a][b + 1]
    return per


def dfs(a, b):  # 遍历标记点周围每个点，如果遍历过周长加上，flag变成1
    global res
    flag[a][b] = 1
    res += perimeters(a, b)
    for (aa, bb) in neighbor(a, b):
        if not flag[aa][bb]:
            dfs(aa, bb)


while 1:
    n = input().split(' ')
    if n[0] == '0':
        break
    length = int(n[0])
    width = int(n[1])
    grid = []
    for i in range(length):
        temp_line = []
        for j in input():
            if j == 'X':
                temp_line.append(1)
            else:
                temp_line.append(0)
        grid.append(temp_line)

    flag = [[0 for _ in range(width)] for _ in range(length)]
    res = 0
    dfs(int(n[2]) - 1, int(n[3]) - 1)
    print(res)

