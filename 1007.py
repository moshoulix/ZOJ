# 求和问题 没啥意思 https://blog.csdn.net/qust1508060414/article/details/50762415

for j in range(2001):
    res = 0.0
    temp = 0.0
    num = j * 0.001
    for i in range(1, 6000):
        temp += 1 / (i * (i + 1) * (i + 2) * (i + num))
    res += (1 - num) * ((2 - num) * temp + 0.25) + 1
    print('%.3f   %.12f' % (num, res))
