# 给两个棋子的位置，求骑士最少走几步，BFS
# 直接用dp来记录最少步数，因为大多情况只和两个位置的相对关系有关
# dp:
# [0, 3, 2, 3, 2, 3, 4, 5]
# [3, 4, 1, 2, 3, 4, 3, 4]
# [2, 1, 4, 3, 2, 3, 4, 5]
# [3, 2, 3, 2, 3, 4, 3, 4]
# [2, 3, 2, 3, 4, 3, 4, 5]
# [3, 4, 3, 4, 3, 4, 5, 4]
# [4, 3, 4, 3, 4, 5, 4, 5]
# [5, 4, 5, 4, 5, 4, 5, 6]
# 注意到1，1处为4，但如果是b6,c7这样的虽然相对关系也是1,1，结果应该为2，因为b6,c7不在四个角上。其余并无特殊情况

def next_step(List):
    a, b = List[0], List[1]
    return [[x, y]for x, y in [[a+1, b+2], [a-1, b+2], [a+1, b-2], [a-1, b-2],
            [a+2, b-1], [a+2, b+1], [a-2, b-1], [a-2, b+1]]
            if 0 <= x <= 7 and 0 <= y <= 7]


dp = [[-1 for _ in range(8)] for _ in range(8)]  # 用dp来记录最少步数
dp[0][0] = 0
queue = [[0, 0]]
while queue:  # bfs
    temp = queue.pop(0)
    for step in next_step(temp):
        res = dp[temp[0]][temp[1]] + 1
        if dp[step[0]][step[1]] == -1:
            dp[step[0]][step[1]] = res
            dp[step[1]][step[0]] = res
            queue.append(step)

corner = ['a1', 'a8', 'h1', 'h8']
try:
    while 1:
        temp_line = input().split(' ')
        case = [abs(ord(temp_line[0][0]) - ord(temp_line[1][0])),
                abs(int(temp_line[0][1]) - int(temp_line[1][1]))]
        if case[0] == case[1] == 1:
            if temp_line[0] not in corner or temp_line[1] not in corner:
                print('To get from {} to {} takes {} knight moves.'.
                      format(temp_line[0], temp_line[1], 2))
                continue
        print('To get from {} to {} takes {} knight moves.'.
              format(temp_line[0], temp_line[1], dp[case[0]][case[1]]))

except EOFError:
    pass
