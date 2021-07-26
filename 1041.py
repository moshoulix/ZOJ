#  半圆覆盖最多点

class Point:
    def __init__(self, X, Y):
        self.x = X - center[0]
        self.y = Y - center[1]


while 1:
    temp = input().split(' ')
    center = int(temp[0]), int(temp[1])
    r = float(temp[2])
    if r < 0:
        break
    n = int(input())
    points = []
    for _ in range(n):
        temp = input().split(' ')
        points.append(Point(int(temp[0]), int(temp[1])))
    points_in_circle = [point for point in points
                        if pow(point.x, 2) + pow(point.y, 2) <= r * r]
    res = 0
    for a in points_in_circle:
        temp_res = 0
        for b in points_in_circle:
            if a.x * b.y - a.y * b.x >= 0:  # 叉乘判断半圆 
                temp_res += 1
        res = temp_res if temp_res > res else res
    print(res)
