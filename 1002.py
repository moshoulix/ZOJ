# dfs + 回溯 可以贪心但没必要
# 0 代表 空
# 1 代表 障碍
# 2 代表 炮台

def int_city(point):
    if point == '.':
        return 0
    else:
        return 1


def legal(index):  # 判断当前位置是否能放炮台
    if city[index] == 0:

        up_index = index - n
        while up_index >= 0:
            if city[up_index] == 1:
                break
            elif city[up_index] == 0:
                up_index -= n
                continue
            elif city[up_index] == 2:
                return False

        down_index = index + n
        while down_index < n * n:
            if city[down_index] == 1:
                break
            elif city[down_index] == 0:
                down_index += n
                continue
            elif city[down_index] == 2:
                return False

        left_index = index - 1
        while (left_index + 1) % n > 0:
            if city[left_index] == 1:
                break
            elif city[left_index] == 0:
                left_index -= 1
                continue
            elif city[left_index] == 2:
                return False

        right_index = index + 1
        while right_index % n > 0:
            if city[right_index] == 1:
                break
            elif city[right_index] == 0:
                right_index += 1
                continue
            elif city[right_index] == 2:
                return False

        return True

    else:
        return False


def dfs(index):
    global max_bh, temp_bh  # max记录最多炮台 temp记录当前炮台
    if index == n * n:
        max_bh = temp_bh if temp_bh > max_bh else max_bh
        return

    if legal(index):         # 放炮台 如果合法
        city[index] = 2
        temp_bh += 1
        dfs(index + 1)
        temp_bh -= 1
        city[index] = 0

    dfs(index + 1)           # 不放炮台


while 1:
    n = int(input())
    if not n:
        break

    city = []
    max_bh = temp_bh = 0

    for row in range(n):
        temp_row = list(map(int_city, input()))
        city += temp_row
    dfs(0)
    print(max_bh)
