# 可加算式  集合{1,2,3}有1+2=3 求所有这样的算式 DFS

def dfs(idx):
    global flag
    sum_ = sum(numbers)
    if idx >= n:
        return
    if sum_ > max_:
        return
    if sum_ in case and len(numbers) > 1 and flag:
        temp = numbers[:]
        temp.append(sum_)
        res.append(temp)
    numbers.append(case[idx])
    flag = True
    dfs(idx + 1)
    numbers.pop()

    flag = False
    dfs(idx + 1)


def prt(Res):
    if Res:
        Res.sort(key=len)
        for i in Res:
            num = i.pop()
            print('+'.join(str(j) for j in i), '={}'.format(num), sep='')
    else:
        print('Can\'t find any equations.')


k = int(input())
for kk in range(k):
    case = list(map(int, input().split(' ')))
    n = case.pop(0)
    case.sort()
    max_ = case[-1]
    res = []
    numbers = []
    flag = True
    dfs(0)
    prt(res)
    print()
