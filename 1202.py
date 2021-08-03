# 有各种容量的金库和相同容量的钻石，问组合数，钻石不同，容量相同的金库相同

from scipy.special import comb, perm
from collections import Counter

try:
    while 1:
        x = int(input())
        y = list(map(int, input().split(' ')))
        Sum = 0
        res = 1
        for i in y:
            Sum += i
        for i in y:
            res *= comb(Sum, i)
            Sum -= i

        dic = dict(Counter(y))
        for key, value in dic.items():
            res /= perm(value, value)

        print(int(res))
except EOFError:
    pass
