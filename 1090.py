# 给三个点的坐标，求圆的周长
# 外接圆半径公式　R = abc / (4 √p (p-a) (p-b) (p-c)) 其中 p = a + b + c / 2
from math import sqrt


def dist(x1, y1, x2, y2):
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


pi = 3.141592653589793
try:
    while 1:
        temp_row = input().split(' ')
        points = []
        for num in temp_row:
            points.append(float(num))
        a = dist(points[0], points[1], points[2], points[3])
        b = dist(points[0], points[1], points[4], points[5])
        c = dist(points[2], points[3], points[4], points[5])
        p = (a + b + c) / 2
        R = (a * b * c) / (4 * sqrt(p * (p - a) * (p - b) * (p - c)))
        C = 2 * pi * R
        print('%.2f' % C)
except EOFError:
    pass
