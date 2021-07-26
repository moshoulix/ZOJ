# 什么数学题 😅

from math import sqrt


temp = input().split(' ')
C = float(temp[2])
R = float(temp[1])
VS = float(temp[0])
for _ in range(int(temp[3])):
    x = float(input())
    VR = C * R * x * VS * sqrt(1 / (1 + pow(C * R * x, 2)))
    print('%.3f' % VR)
