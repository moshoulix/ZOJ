# 前16行为点集，求输入与点集距离最近的点


def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


points = []
for _ in range(16):
    temp_line = input().split(' ')
    points.append([int(temp_line[0]), int(temp_line[1]), int(temp_line[2])])

while 1:
    temp_line = input().split(' ')
    color = [int(temp_line[0]), int(temp_line[1]), int(temp_line[2])]
    if color[0] == -1:
        break
    res = 0
    min_dist = 200000
    for point in points:
        temp_dist = dist(point, color)
        if temp_dist < min_dist:
            min_dist = temp_dist
            res = point

    print('({},{},{}) maps to ({},{},{})'.format(color[0], color[1], color[2],
                                                 res[0], res[1], res[2]))

