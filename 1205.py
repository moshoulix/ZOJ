# 20 进制加法

def number(m):  # 将一位的20进制变成10进制
    try:
        return int(m)
    except ValueError:
        return ord(m) - 87


def letter(n):  # 将一个20以内的数变成20进制
    if n < 10:
        return str(n)
    return chr(87 + n)


def add(m, n):
    res = ''
    for i in range(len(m)):
        m[i] = number(m[i])
    for i in range(len(n)):
        n[i] = number(n[i])
    flag = False  # 是否进位
    while m:  # 先m后n 因位m比n短
        temp = m.pop() + n.pop()
        if flag:
            temp += 1
            flag = False
        if temp > 19:
            temp -= 20
            flag = True
        res = letter(temp) + res
    while n:
        temp = n.pop()
        if flag:
            temp += 1
            flag = False
        if temp > 19:
            temp -= 20
            flag = True
        res = letter(temp) + res
    if flag:
        return '1' + res
    return res


try:
    while 1:
        a = list(input())
        b = list(input())
        a, b = (a, b) if len(a) <= len(b) else (b, a)
        print(add(a, b))
except EOFError:
    pass
