# 叠卡片

try:
    print('# Cards  Overhang')
    while 1:
        n = int(input())
        res = 0.0
        for i in range(n):
            res += 1 / 2 / (i + 1)
        print('%5d     %.3f' % (n, res))
except EOFError:
    pass

