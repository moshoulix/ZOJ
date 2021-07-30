# 三个棋子，邻接矩阵，棋子只能在其他两个棋子之间路径相同的颜色的路径上移动 BFS

class State:
    def __init__(self, A, B, C, Result):
        self.s = [A, B, C]
        self.res = Result
        self.same = True if A == B == C else False


def can_move(state, II, J):  # 棋子II 可以移动到J
    p = state.s[II]
    lis = [0, 1, 2]
    lis.remove(II)
    return map_[p][J] == map_[state.s[lis[0]]][state.s[lis[1]]] or \
        map_[p][J] == map_[state.s[lis[1]]][state.s[lis[0]]]


def temp_flag(state, II, J):
    p = state.s[:]
    p[II] = J
    return p


def bfs():
    pieces = temp_line[1:]
    flag = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    flag[pieces[0] - 1][pieces[1] - 1][pieces[2] - 1] = 1
    queue = [State(pieces[0] - 1, pieces[1] - 1, pieces[2] - 1, 0)]
    while queue:
        temp = queue.pop(0)
        for i in range(3):  # 遍历三个棋子
            for j in range(n):  # 遍历棋子的下一个位置
                if j != temp.s[i] and can_move(temp, i, j):  # 需要检查 1 当前位置是否变化 2 是否有路径可移动
                    temp_f = temp_flag(temp, i, j)
                    if not flag[temp_f[0]][temp_f[1]][temp_f[2]]:  # 3 是否遍历过
                        flag[temp_f[0]][temp_f[1]][temp_f[2]] = 1
                        temp_list = temp.s[:]
                        temp_list[i] = j
                        temp_state = State(temp_list[0], temp_list[1], temp_list[2], temp.res + 1)
                        if temp_state.same:  # 成功 返回
                            return temp_state.res
                        queue.append(temp_state)  # 否则 加入到队列中
    return -1


while 1:
    temp_line = list(map(int, input().split(' ')))
    n = temp_line[0]
    if not n:
        break

    map_ = []
    for _ in range(n):
        map_.append(input().split(' '))

    if temp_line[1] == temp_line[2] == temp_line[3]:  # 就差这一段wa了，debug了半小时
        print(0)
        continue
    
    Res = bfs()
    if Res >= 0:
        print(Res)
    else:
        print('impossible')
