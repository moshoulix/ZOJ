# DP

num = 0
while 1:
    n, k = list((map(int, input().split(' '))))
    if not n:
        break
    pos = []
    for _ in range(n):
        pos.append(int(input()))
    inf = (pos[-1] - pos[0]) * n
    dp = [[0 for _ in range(n)] for _ in range(k)]
    # dp[b][a] 代表从第 0 到第 a 个站点，共用 b+1 个的最小距离
    dis = [[0 for _ in range(n)] for _ in range(n)]  # dis[a][b] 表示a到b的一个站的距离
    for i in range(n):
        for j in range(i, n):
            dis[i][j] = sum(abs(pos[x] - pos[(i + j) // 2]) for x in range(i, j + 1))

    dp[0] = dis[0]
    for j in range(1, k): # k-1 也行但懒得写
        for i in range(1, n):
            dp[j][i] = min(dp[j - 1][x] + dis[x + 1][i] for x in range(i))

    res = dp[-1][-1]
    num += 1
    print('Chain {}'.format(num))
    print('Total distance sum = {}'.format(res))
    print()
