# Dick 12 岁；Jane x3 岁；
# Spot x0岁的时候 Puff出生，x2岁的时候Yertle出生；puff x1岁的时候，yertle出生
# 已知 x0 + x1 + x2 = x3 + 12，求s、p、y的年龄，所有年龄向下取整
# Spot x0岁的时候 Puff出生就是理解为 s - p 为x0 或 x0 + 1

def find_age():
    c_min = (12 + x[3] - x[0] * 2 - x[1]) // 3 - 1
    for c in range(c_min, c_min + 3):
        for b in range(c + x[1], c + x[1] + 2):
            for a in range(c + x[2], c + x[2] + 2):
                if a + b + c == 12 + x[3] and x[0] <= a - b <= x[0] + 1:
                    return a, b, c


try:
    while 1:
        x = list(map(int, input().split(' ')))
        res = find_age()
        print(' '.join(str(age) for age in res))

except EOFError:
    pass
