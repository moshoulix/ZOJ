# 约瑟夫环

def josephus(a):
    res = 0
    for i in range(2, n):
        res = (res + a) % i
    return res != 0


while 1:
    n = int(input())
    if not n:
        break
    m = 1
    while josephus(m):
        m += 1
    print(m)
