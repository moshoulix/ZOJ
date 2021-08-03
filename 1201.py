# 1 to 9 的排列 591826473 其中1的左边有2个大于1的数，2的左边有三个大于2的数
# 以此类推反演表为 236402210

def p1(n, li):
    arr = []
    for i in range(n):
        arr.append(int(li[i + 1]))
    res = [0] * n
    flag = {a for a in range(1, n + 1)}
    for i in range(n):
        flag.remove(arr[i])
        for j in range(arr[i]):
            if j + 1 in flag:
                res[j] += 1
    return res


def p2(n, li):
    arr = []
    for i in range(n):
        arr.append(int(li[i + 1]) + i + 1)
    flag = list(range(n))
    res = []
    for i in range(n):
        idx = arr.index(n)
        res.append(flag[idx] + 1)
        flag.remove(flag[idx])
        arr.remove(arr[idx])
        for j in range(idx):
            arr[j] += 1
    res.reverse()
    return res


while 1:
    x = int(input())
    if x == 0:
        break
    y = input().split(' ')
    if y[0] == 'P':
        Res = p1(x, y)
    else:
        Res = p2(x, y)

    print(' '.join(str(num) for num in Res))

