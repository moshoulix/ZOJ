# 最短路径问题  BFS

def solve(a, b):  # BFS
    queue = [[a, 0]]
    flag = [0 for _ in range(20)]
    flag[a] = 1
    while queue:
        temp = queue.pop(0)
        for point in range(20):
            if map_[temp[0]][point] and not flag[point]:
                if point == b:
                    return temp[1] + 1
                queue.append([point, temp[1] + 1])
                flag[point] = 1


try:
    idx = 0
    while 1:
        map_ = [[0 for _ in range(20)] for _ in range(20)]
        for i in range(19):
            for j in list(map(lambda x: int(x) - 1, input().split(' ')))[1:]:
                map_[i][j] = 1
                map_[j][i] = 1
        case_n = int(input())
        idx += 1
        print('Test Set #{}'.format(idx))
        for _ in range(case_n):
            temp_line = list(map(int, input().split(' ')))
            res = solve(temp_line[0] - 1, temp_line[1] - 1)
            print('{} to {}: {}'.format(temp_line[0], temp_line[1], res))
        print()
except EOFError:
    pass
