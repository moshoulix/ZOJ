# n维迷宫，第一行给定n，第二行是起点和终点，其余是路径，DFS

def dfs(St):
    global find
    temp = [j for j in road if j[0] == St]
    for j in temp:
        if j[1] == ed:
            find = True
            break
        dfs(j[1])
    return find


idx = 0
while 1:
    idx += 1
    n = int(input())
    if not n:
        break
    rd = list(map(int, input().split()))
    st = 0
    ed = 0

    x = []
    road = []
    while 1:
        x.append(list(map(int, input().split())))
        if x[-1][0] < 0:
            x.pop()
            break
        a = 0
        b = 0
        for i in range(0, n):
            a = a * 10 + x[-1][i]
            b = b * 10 + x[-1][i + n]
        road.append([a, b])

    for i in range(0, n):
        st = rd[i] + 10 * st
        ed = 10 * ed + rd[n + i]
    find = False
    if dfs(st):
        print('Maze #{} can be travelled'.format(idx))
    else:
        print('Maze #{} cannot be travelled'.format(idx))
