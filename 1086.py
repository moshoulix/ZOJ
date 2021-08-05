# 八进制转换为10进制，精确除法，模拟

try:
    while 1:
        temp_line = input()
        number = list(temp_line)[2:]
        res = 0
        for i in number:
            res = 8 * res + int(i)
        d = 8 ** len(number)
        temp = []
        while res:
            res *= 10
            temp.append(res // d)
            res = res % d

        print('{} [8] = 0.'.format(temp_line),
              ''.join(str(i) for i in temp),
              ' [10]',
              sep='')
except EOFError:
    pass
