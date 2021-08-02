# 货币兑换是否可套利 floyd

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if map_[i][j] < map_[i][k] * map_[k][j]:  # 注意这里是小于和乘法
                    map_[i][j] = map_[i][k] * map_[k][j]
                    if i == j:
                        return True
    return False

case = 0
while 1:
    n = int(input())
    if not n:
        break
    case += 1
    name = []
    for _ in range(n):
        name.append(input())
    m = int(input())
    map_ = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        map_[i][i] = 1
    for _ in range(m):
        temp_line = input().split(' ')
        a = name.index(temp_line[0])
        b = name.index(temp_line[2])
        map_[a][b] = float(temp_line[1])  # 蜜汁警告

    if floyd():
        print('Case {}: Yes'.format(case))
    else:
        print('Case {}: No'.format(case))
        
    try:   # 输入之间有空行
        n = input()
    except EOFError:
        pass
    
