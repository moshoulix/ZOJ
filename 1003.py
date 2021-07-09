# dfs

def dfs(a, b, k):
    global fa, fb
    if b == 1:
        fb = True
        if a == 1:
            fa = True
    if k == 1 or (fa and fb):
        return
    if a % k == 0:             # 把k气球给a 如果可以整除
        dfs(a//k, b, k-1)
    if b % k == 0:             # 把k气球给b 如果可以整除
        dfs(a, b//k, k-1)
    dfs(a, b, k-1)             # k气球不给


try:
    while 1:
        x = input().split(' ')
        x[0] = int(x[0])          # 用map总是无0返回，搞不懂
        x[1] = int(x[1])
        (a, b) = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
        fa = fb = False

        dfs(a, b, 100)
        if fb and not fa:
            print(b)
        else:
            print(a)
except EOFError:
    pass

