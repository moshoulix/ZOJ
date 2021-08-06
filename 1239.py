# 找规律 1 2 4 8 12 18 24 32 为平方数/2向下取整

n = int(input())
for _ in range(n):
    x = int(input())
    if x % 2:
        print(int(((x + 1) ** 2) / 2 - 1))
        continue
    print(int(((x + 1) ** 2 - 1) / 2 - 1))
